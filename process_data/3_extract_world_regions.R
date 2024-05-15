# Extract world region
Sys.setenv(PATH="/usr/bin:/bin")
library(tidyverse)
library(rnaturalearth)
library(rnaturalearthdata)
library(sf)

# Load functions
# Extract cleaned country data from Natural Earth Data
extract_countries <- function(){
  
  # Load country data
  world <- ne_countries(scale = "medium", returnclass = "sf") %>%
    select(name, sovereignt, iso_a3, geometry)
  
  # Split France from country data and split into separate regions
  france <- world %>% 
    filter(iso_a3 == "FRA") %>%
    st_cast("POLYGON") %>%
    mutate(id = row_number()) %>%
    mutate(name = case_when(
      id == 1 ~ "Réunion",
      id == 2 ~ "Mayotte",
      id == 3 ~ "French Guiana",
      id == 4 ~ "Martinique",
      id == 5 ~ "Guadeloupe",
      id == 6 ~ "Guadeloupe",
      id == 7 ~ "Guadeloupe",
      TRUE ~ name)) %>%
    mutate(iso_a3 = case_when(
      id == 1 ~ "REU",
      id == 2 ~ "MYT",
      id == 3 ~ "GUF",
      id == 4 ~ "MTQ",
      id == 5 ~ "GLP",
      id == 6 ~ "GLP",
      id == 7 ~ "GLP",
      TRUE ~ iso_a3)) %>%
    group_by(name, sovereignt, iso_a3) %>%   
    summarise(geometry = st_union(geometry), .groups = "keep")
  
  # Rejoin with other country data
  world <- world %>%
    filter(iso_a3 != "FRA") %>%
    bind_rows(france)
}

# Extract country data
countries <- extract_countries() |>
  mutate(id = row_number())

# Write CSV file
st_write(countries, "countries.gpkg", delete_layer = TRUE)
