from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # 👈 Import this
from app.routes import router

app = FastAPI(title="Quran AI API")

# 👇 Add CORS middleware before including routes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 👈 Or specify exact origins like ["https://yourfrontend.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
