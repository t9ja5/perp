from sqlalchemy import Column, Integer, String, Float
from app.db.base import Base

class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    roll_no = Column(String, unique=True, nullable=False)
    cgpa = Column(Float)
    department = Column(String)