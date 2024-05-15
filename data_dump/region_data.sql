SELECT id AS region_id, 
       name AS region_name,
       description as region_description,
       geom AS gis_region,
       completed as completed 
FROM public.gis_regions_gis_region grgr  
ORDER BY id;