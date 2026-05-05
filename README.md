# Incident Management System (SRE Assignment)

## Overview
A lightweight system designed to ingest high-volume signals and create incidents using debouncing logic to prevent alert storms.

## Features
- Signal ingestion API
- Debouncing (10-second window)
- Incident lifecycle management
- RCA required before closure
- MTTR tracking

## Tech Stack
- FastAPI
- SQLite
- SQLAlchemy
- HTML (basic frontend)

## Architecture
Client → FastAPI → Debounce Logic → SQLite DB

## How to Run

```bash
cd backend
pip install -r requirements.txt
python -m uvicorn app:app --reload


## API Usage

### Create Signal
POST /signals?component=database

### Get Incidents
GET /incidents

### Close Incident
POST /incidents/1/rca?rca=Database overload

---

## SRE Concepts Applied
- Alert deduplication using debouncing logic
- Incident lifecycle management (OPEN → CLOSED)
- Basic backpressure handling to avoid alert storms

---

## Trade-offs
- SQLite used instead of distributed database
- In-memory debouncing resets on restart
- Minimal frontend for demonstration

---

## Future Improvements
- Integrate Kafka for event streaming
- Use Redis for distributed caching
- Deploy using Docker & Kubernetes
