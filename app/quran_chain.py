from dotenv import load_dotenv
load_dotenv()
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-001", temperature=0.5)

prompt = PromptTemplate(
    input_variables=["question"],
    template="Please provide an answer from the Quran or authentic islamic sources(Hadid) or from both for the following question: {question}. Answer should be based only on Quranic teachings or islamic authentic sources(Hadid). Answer in Bengali even when you don't know. Don't answer and refuse respectfully if the question is not related to Quran/Hadid in anyway."
)

chain = prompt | llm

def get_quran_answer(question: str) -> str:
    print(question)
    response = chain.invoke({"question": question})
    print(response)
    return response.content
