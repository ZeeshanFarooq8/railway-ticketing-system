from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from db import SessionLocal
from Routers import train, passenger
from Routers import route
from Routers import schedule
from Routers import ticket


app = FastAPI()

# Dependency


app.include_router(train.router)
app.include_router(route.router)
app.include_router(passenger.router)
app.include_router(ticket.router)
app.include_router(schedule.router)

app.include_router(ticket.router)

# @app.get("/")
# def root():
#     return {"message": "Railway Ticketing API Running"}
