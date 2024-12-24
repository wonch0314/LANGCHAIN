from langchain_openai import ChatOpenAI
import os

# https://platform.openai.com/docs/overview <= 에서 openai api key 발급 (Token 충전 필요)
os.environ["OPENAI_API_KEY"]="{openai에서 발급받은 api key}"


gpt4o = ChatOpenAI(model="gpt-4o-mini")
gpt4o.invoke("HELLO GPT, WHAT CAN YOU DO FOR ME?")
"""
    Hello! I can assist you with a variety of tasks, including:

    1. **Answering Questions**: I can provide information on a wide range of topics, from science and history to technology and art.    
    2. **Writing Assistance**: I can help you draft essays, emails, reports, or creative writing pieces.
    3. **Learning Support**: I can explain concepts, summarize information, or help with study techniques.
    4. **Recommendations**: I can suggest books, movies, or music based on your interests.
    5. **Problem Solving**: I can assist with brainstorming ideas or troubleshooting issues.
    6. **Language Practice**: I can help you practice a new language or improve your writing skills.

    Just let me know what you need help with!
"""