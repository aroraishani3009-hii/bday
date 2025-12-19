from fastapi import APIRouter
from ..schemas import ContactIn
from ..db import SessionLocal

router = APIRouter(prefix="/contact", tags=["contact"])

@router.post("/send")
def send_message(payload: ContactIn):
    # Stub: integrate email provider or store in DB
    # For now, just acknowledge
    return {"status": "ok", "received": payload.dict()}
