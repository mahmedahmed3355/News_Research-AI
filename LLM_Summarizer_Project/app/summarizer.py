
# app/summarizer.py
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(openai_api_key=openai_api_key, temperature=0.3, model="gpt-4")

summarize_prompt = PromptTemplate(
    input_variables=["text"],
    template="من فضلك لخّص النص التالي بلغة عربية فصيحة، ووضح النقاط الرئيسية باختصار:\n\n{text}"
)

def summarize_text(text: str) -> str:
    prompt = summarize_prompt.format(text=text)
    return llm.predict(prompt)

