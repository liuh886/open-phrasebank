# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from model import create_tables
from router import router

app = FastAPI()

create_tables()  # Create database tables at startup

app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
