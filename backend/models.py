from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from db import Base

class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    component = Column(String, index=True)
    status = Column(String, default="OPEN")
    start_time = Column(DateTime, default=datetime.utcnow)
    end_time = Column(DateTime, nullable=True)
    rca = Column(String, nullable=True)