WITH published_entries AS (
    SELECT
        DISTINCT entry_id
    FROM
        public.polls_pollprogress
    WHERE
        published != 0
)
SELECT
    pe.id AS entry_id,
    pen.entry_name,
    pe.poll_id,
    pp.poll_name,
    pe.description,
    pe.year_from,
    pe.year_to,
    pe.region_id,
    ae.expert_id,
    CASE 
        WHEN aues.expert_source_name IS NOT NULL THEN aues.expert_source_name
        ELSE au.expert_name 
    END AS expert_name,
    ae.editor_id,
    COALESCE(aure.regionaleditor_name, aume.managingeditor_name) AS editor_name,
    pe.date_created,
    pe.date_modified,
    pd.data_source
FROM
    public.polls_entity pe
LEFT JOIN
    (SELECT id AS user_id, CONCAT(first_name, ' ', last_name) AS expert_name FROM public.auth_user) au
    ON pe.created_by_id = au.user_id
LEFT JOIN
    (SELECT id AS expert_id, editor_id, user_id FROM public.accounts_expert) ae
    ON au.user_id = ae.user_id
LEFT JOIN
    (SELECT id AS editor_id, user_id FROM public.accounts_managingeditor) ame
	ON (ae.editor_id = ame.editor_id)
LEFT JOIN
    (SELECT id as user_id, CONCAT(first_name, ' ', last_name) as managingeditor_name FROM public.auth_user) aume
	ON (ame.user_id = aume.user_id)
LEFT JOIN
    (SELECT id AS editor_id, user_id FROM public.accounts_regionaleditor) are
	ON (ae.editor_id = are.editor_id)
LEFT JOIN
    (SELECT id as user_id, CONCAT(first_name, ' ', last_name) as regionaleditor_name FROM public.auth_user) aure
	ON (are.user_id = aure.user_id)
LEFT JOIN
    (SELECT id AS poll_id, name AS poll_name FROM public.polls_poll) pp
    ON pe.poll_id = pp.poll_id
LEFT JOIN
    (SELECT id AS entry_id, name AS entry_name FROM public.polls_entityname) pen
    ON pe.name_id = pen.entry_id
LEFT JOIN
    (SELECT id AS data_source_id, name AS data_source FROM public.polls_datasource) pd
ON (pe.data_source_id = pd.data_source_id) 
LEFT JOIN
    (SELECT id AS expert_source_id, user_id FROM public.accounts_expert) aees
	ON (pe.expert_source_id = aees.expert_source_id) 
LEFT JOIN
    (SELECT id AS user_id, CONCAT(first_name, ' ', last_name) AS expert_source_name FROM public.auth_user) aues
	ON (aees.user_id = aues.user_id) 
WHERE
    pe.id IN (SELECT entry_id FROM published_entries)
    AND pp.poll_name != 'Polity'
ORDER BY
    pe.id;