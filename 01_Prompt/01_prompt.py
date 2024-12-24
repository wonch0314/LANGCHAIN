from langchain_core.prompts import PromptTemplate

template_question = """
    [question]
    {question}
"""

template_context = """
    [context]
    {context}
"""

prompt_template_question = PromptTemplate.from_template(template_question)
prompt_template_context = PromptTemplate.from_template(template_context)

combined_template = prompt_template_context + prompt_template_question
"""
    input_variables=['context', 'question']
    input_types={}
    partial_variables={}
    template='
        [context]
        {context}
        
        [question]
        {question}
    '
"""

combined_template.format(context="my context", question ="my question")
"""
    [context]
    my context

    [question]
    my question
"""