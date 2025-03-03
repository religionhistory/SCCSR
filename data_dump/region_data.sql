SELECT distinct 
	grgr.id AS region_id, 
       grgr.name AS region_name,
       grgr.description as region_description,
       ST_AsText(grgr.geom) AS gis_region,
       grgr.completed as completed,
       grgrt.region_tag_id,
       grgt.region_tag_name,
       grgt.parent_tag_id,
       grgt."path"
FROM public.gis_regions_gis_region grgr
left join
	(select region_id, gis_tag_id as region_tag_id from public.gis_regions_gis_region_tags) grgrt
	on grgr.id = grgrt.region_id
left join 
	(select id as region_tag_id, name as region_tag_name, parent_tag_id, "path" from public.gis_regions_gis_tag) grgt
	on grgrt.region_tag_id = grgt.region_tag_id
ORDER BY id;