SELECT DISTINCT 
    b1.question_id, q1.question_name, q2.parent_question_id, q2.parent_question, b1.entry_id,
    CASE WHEN text_input is null THEN a1.name
         ELSE CONCAT(a1.name, ': ', text_input)
    END as answer,
    a1.value,
    CASE WHEN parent_text_input is null THEN parent_name
         ELSE CONCAT(parent_name, ': ', parent_text_input)
    END as parent_answer,
    b3.parent_answer_value, b1.notes, b1.year_from, b1.year_to, 
    concat(branching_question_name, ' ', string_agg(branching_question, ', ' ORDER BY branching_question)) AS branching_question,
    b1.region_id, e1.expert_id, e2.expert_name, e1.editor_id, COALESCE(e3.regionaleditor_name, e4.managingeditor_name) AS editor_name,
    a3.date_published, b1.date_created, b1.date_modified
FROM  
    public.polls_answer a1
LEFT JOIN
    public.polls_templateanswer ta
ON (a1.template_answer_id = ta.id) 
LEFT JOIN
    public.polls_baseanswerset b1
ON (a1.base_answer_set_id = b1.id) 
LEFT JOIN
    (SELECT baseanswerset_ptr_id AS baseanswerset_id, parent_answerset_id, published, date_published FROM public.polls_answerset) a3
ON (b1.id = a3.baseanswerset_id) 
LEFT JOIN
    (SELECT id AS question_id, name AS question_name, parent_question_id FROM public.polls_question) q1
ON (b1.question_id = q1.question_id) 
LEFT JOIN
    (SELECT id AS parent_question_id, name AS parent_question FROM public.polls_question) q2
ON (q1.parent_question_id = q2.parent_question_id) 
LEFT JOIN
    (SELECT id AS expert_id, user_id, editor_id FROM public.accounts_expert) e1
ON (b1.expert_id = e1.expert_id) 
LEFT JOIN
    (SELECT id AS user_id, CONCAT(first_name, ' ', last_name) AS expert_name FROM public.auth_user) e2
ON (e1.user_id = e2.user_id) 
LEFT JOIN
    (SELECT id AS editor_id, user_id FROM public.accounts_regionaleditor) re
ON (e1.editor_id = re.editor_id)
LEFT JOIN
    (SELECT id as user_id, CONCAT(first_name, ' ', last_name) as regionaleditor_name FROM public.auth_user) e3
ON (re.user_id = e3.user_id)
LEFT JOIN
    (SELECT id AS editor_id, user_id FROM public.accounts_managingeditor) me
ON (e1.editor_id = me.editor_id)
LEFT JOIN
    (SELECT id as user_id, CONCAT(first_name, ' ', last_name) as managingeditor_name FROM public.auth_user) e4
ON (me.user_id = e4.user_id)
left join 
    (SELECT baseanswerset_id, branch_id FROM public.polls_baseanswerset_branches) br1
ON (b1.id = br1.baseanswerset_id) 
LEFT JOIN
    (SELECT id AS branch_id, name AS branching_question, branching_question_id FROM public.polls_branch) br2
ON (br1.branch_id = br2.branch_id) 
LEFT JOIN
    (SELECT id AS branching_question_id, name AS branching_question_name FROM public.polls_branchingquestion) br3
ON (br2.branching_question_id = br3.branching_question_id) 
LEFT JOIN
    (SELECT id, name_id, description AS entry_description, data_source_id FROM public.polls_entity) en1
ON (b1.entry_id = en1.id)
LEFT JOIN
    (SELECT id AS name_id, name AS entry_name FROM public.polls_entityname) en2
ON (en1.name_id = en2.name_id)
LEFT JOIN
    (SELECT id AS data_source_id, name AS data_source FROM public.polls_datasource) en3
ON (en1.data_source_id = en3.data_source_id) 
LEFT JOIN
    (SELECT id AS parentanswer_id, name AS parent_name, text_input AS parent_text_input, value AS parent_answer_value FROM public.polls_answer) b3
ON (a3.parent_answerset_id = b3.parentanswer_id) 
LEFT JOIN
    (SELECT id AS poll_id, name AS poll FROM public.polls_poll) p1
ON (b1.poll_id = p1.poll_id) 
WHERE a3.published IS TRUE 
  AND p1.poll != 'Polity' 
  AND b1.history_parent_id IS NULL
GROUP by b1.question_id, q1.question_name, a1.name, a1.value, b1.notes, a1.text_input, en3.data_source, b1.entry_id, b1.region_id, b1.year_from, b1.year_to, br3.branching_question_name, e1.expert_id, e2.expert_name, e1.editor_id, editor_name, q2.parent_question_id, q2.parent_question, b3.parent_answer_value, b3.parent_name, b3.parent_text_input, b1.date_modified, b1.date_created, a3.date_published 
ORDER BY b1.entry_id ASC;