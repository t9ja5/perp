from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class Application(Base):
    __tablename__ = "application"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("student.id"))
    company_id = Column(Integer, ForeignKey("company.id"))
    status = Column(String, default="applied")

    student = relationship("Student")
    company = relationship("Company")