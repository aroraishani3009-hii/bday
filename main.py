from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import content, contact
from .db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Dynamic Site API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(content.router)
app.include_router(contact.router)
