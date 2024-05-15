SELECT first_question_id AS question_id, 
       second_question_id AS related_question_id 
FROM public.polls_questionrelation 
ORDER BY first_question_id;