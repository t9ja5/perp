from sqlalchemy import Column, Integer, String
from app.db.base import Base

class PlacementCoordinator(Base):
    __tablename__ = "placement_coordinator"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    department = Column(String)
    role = Column(String, default="admin")