from fastapi import FastAPI, HTTPException
from db import Base, engine, SessionLocal
from models import Incident
from logic import should_create_incident
from datetime import datetime

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "working"}

@app.post("/signals")
def ingest_signal(component: str):
    db = SessionLocal()

    if not should_create_incident(component):
        return {"message": "Signal ignored (debounced)"}

    incident = Incident(component=component)
    db.add(incident)
    db.commit()
    db.refresh(incident)

    return {"incident_id": incident.id}

@app.get("/incidents")
def get_incidents():
    db = SessionLocal()
    return db.query(Incident).all()

@app.post("/incidents/{id}/rca")
def add_rca(id: int, rca: str):
    db = SessionLocal()
    incident = db.query(Incident).get(id)

    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")

    incident.rca = rca
    incident.status = "CLOSED"
    incident.end_time = datetime.utcnow()

    db.commit()

    return {"message": "Incident closed with RCA"}