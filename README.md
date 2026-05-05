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
