from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

import os
os.environ["OPENAI_API_KEY"] = "{openai api key}"

gpt = ChatOpenAI(model = "gpt-4o-mini")

template = """
    [question]
    {question}

    [context]
    {context}
"""
prompt_template_context = PromptTemplate.from_template(template)

template_value = prompt_template_context.format(
    question = "메로나는 무슨 맛이야?",
    context = "메로나는 한국에서 파는 아이스크림이야"
)
"""
    [question]
    메로나는 무슨 맛이야?

    [context]
    메로나는 한국에서 파는 아이스크림이야
"""

response = gpt.invoke(template_value)
response.content
"""
    메로나는 주로 멜론 맛의 아이스크림으로 유명하죠. 달콤하고 상큼한 
    멜론의 맛이 특징이며, 부드러운 식감으로 많은 사람들에게 사랑받고  있습니다.
    또한, 메로나는 다양한 과일 맛 버전도 출시되고 있어 여러 가지 맛을 즐길 수 있습니다.
"""