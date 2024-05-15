SELECT
    petg.entry_id AS entry_id,
    pet.name AS entry_tag,
    petg.entrytag_id AS entrytag_id,
    pet.parent_tag_id AS parent_tag_id,
    pet.level AS level,
    pet."path" as path,
    pet.approved as approved
FROM
    polls_entity_tags petg
JOIN
    polls_entitytag pet ON petg.entrytag_id = pet.id	
ORDER BY
    petg.entry_id;
