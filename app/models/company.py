from sqlalchemy import Column, Integer, String, Float
from app.db.base import Base

class Company(Base):
    __tablename__ = "companY"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    package = Column(Float)
    position = Column(String)
    eligibility_criteria = Column(String)