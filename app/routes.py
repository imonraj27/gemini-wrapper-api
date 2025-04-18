from fastapi import APIRouter
from app.model import QuestionRequest, AnswerResponse
from app.quran_chain import get_quran_answer

router = APIRouter()

@router.post("/ask", response_model=AnswerResponse)
def ask_question(request: QuestionRequest):
    answer = get_quran_answer(request.question)
    return AnswerResponse(answer=answer)
