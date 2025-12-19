from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db import SessionLocal
from ..models import Memory
from ..schemas import MemoryOut

router = APIRouter(prefix="/content", tags=["content"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/memories", response_model=list[MemoryOut])
def list_memories(db: Session = Depends(get_db)):
    # Seed demo data if empty
    if not db.query(Memory).count():
        db.add_all([
            Memory(title="Morning Tea", text="She taught me the perfect chai.", image="https://picsum.photos/400?1"),
            Memory(title="Road Trip", text="Singing 90s hits all the way.", image="https://picsum.photos/400?2"),
            Memory(title="Birthday Cake", text="Secret recipe, infinite love.", image="https://picsum.photos/400?3"),
        ])
        db.commit()
    return db.query(Memory).all()
