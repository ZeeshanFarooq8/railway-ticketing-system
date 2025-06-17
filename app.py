from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from db import SessionLocal
from Routers import train

app = FastAPI()

# Dependency


app.include_router(train.router)

@app.get("/")
def root():
    return {"message": "Railway Ticketing API Running"}
