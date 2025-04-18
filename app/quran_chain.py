from dotenv import load_dotenv
load_dotenv()
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-001", temperature=0.5)

prompt = PromptTemplate(
    input_variables=["question"],
    template="Please provide an answer from the Quran for the following question: {question}. Answer should be based only on Quranic teachings. Answer in Bengali even when you don't know."
)

chain = prompt | llm

def get_quran_answer(question: str) -> str:
    print(question)
    response = chain.invoke({"question": question})
    print(response)
    return response.content
