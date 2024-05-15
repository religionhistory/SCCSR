import numpy as np
import pandas as pd
import geopandas as gpd
from shapely import wkt
import pygeos

# Countries and World Regions
countries_gdf = gpd.read_file("countries.gpkg")
world_regions = pd.read_csv("../data_raw/world_regions.csv")
countries_regions = countries_gdf.merge(world_regions, on="iso_a3", how="left")

# If no associated world region we cannot use it
countries_regions = countries_regions.dropna()
countries_regions = countries_regions.rename(
    {"Country": "country", "World.Region": "world_region"}, axis=1
)

# Load the gis data
region_data = pd.read_csv("../data_raw/region_data.csv")

# We are only interested in the region data that is present in our data
# This would be eitehr in entrydata or answerset
entrydata = pd.read_csv("../data_raw/entry_data.csv")
answerset = pd.read_csv("../data_raw/answerset.csv")
region_entrydata = entrydata["region_id"].unique()
region_answerset = answerset["region_id"].unique()
region_total = np.union1d(region_entrydata, region_answerset)
region_data = region_data[region_data["region_id"].isin(region_total)]
region_data = region_data[region_data["gis_region"].notnull()]

# now we create geopandas dataframe
region_data["geometry"] = region_data["gis_region"].apply(wkt.loads)
region_gdf = gpd.GeoDataFrame(region_data, geometry="geometry")
region_gdf = region_gdf.set_crs("EPSG:4326")

# find intersections
intersection = gpd.overlay(
    countries_regions, region_gdf, how="intersection", keep_geom_type=False
)

# get mode world region for overlapping cases
region_intersection_mode = (
    intersection.groupby(["region_id", "region_name"])["world_region"]
    .agg(lambda x: x.mode()[0])
    .reset_index()
)

# fix cases with no overlap (find nearest)
non_overlapping = region_gdf[~region_gdf["region_id"].isin(intersection["region_id"])]
countries_regions_pygeos = pygeos.from_shapely(countries_regions["geometry"])
non_overlapping_pygeos = pygeos.from_shapely(non_overlapping["geometry"])

non_overlapping["id"] = np.nan
for idx, geometry in enumerate(non_overlapping_pygeos):
    distances = pygeos.distance(geometry, countries_regions_pygeos)
    closest_country_idx = np.argmin(distances)
    non_overlapping.iloc[idx, non_overlapping.columns.get_loc("id")] = (
        closest_country_idx
    )

non_overlapping["id"] = non_overlapping["id"].astype(int)
non_overlapping = non_overlapping[["region_id", "region_name", "id"]].drop_duplicates()

# merge on countries regions
non_overlapping = non_overlapping.merge(countries_regions, on="id", how="left")
non_overlapping = non_overlapping[["region_id", "region_name", "world_region"]]

# concatenate with the intersection data
unique_world_region = pd.concat([region_intersection_mode, non_overlapping])
unique_world_region["region_id"].nunique()  # 1255

# add back information from region_data
region_data = region_data[
    ["region_id", "region_name", "region_description", "gis_region", "completed"]
].drop_duplicates()
unique_world_region_metadata = unique_world_region.merge(
    region_data, on=["region_id", "region_name"], how="inner"
)
unique_world_region_metadata = unique_world_region_metadata.sort_values("region_id")

# re-order columns
unique_world_region_metadata = unique_world_region_metadata[
    [
        "region_id",
        "region_name",
        "region_description",
        "gis_region",
        "completed",
        "world_region",
    ]
]

# save data
unique_world_region_metadata.to_csv("../data_clean/region_data.csv", index=False)
