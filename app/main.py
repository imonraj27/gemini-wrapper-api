from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Quran AI API")

app.include_router(router)
