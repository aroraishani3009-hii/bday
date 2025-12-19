from sqlalchemy import Column, Integer, String, Text
from .db import Base

class Memory(Base):
    __tablename__ = "memories"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(120), nullable=False)
    text = Column(Text, nullable=False)
    image = Column(String(255), nullable=True)
