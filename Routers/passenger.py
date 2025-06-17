from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
from Model import Passenger
from schemas import PassengerCreate, PassengerOut

router = APIRouter(
    prefix="/passengers",
    tags=["Passengers"]
)

@router.post("/", response_model=PassengerOut)
def create_passenger(passenger: PassengerCreate, db: Session = Depends(get_db)):
    db_passenger = Passenger(**passenger.dict())
    db.add(db_passenger)
    db.commit()
    db.refresh(db_passenger)
    return db_passenger

@router.get("/", response_model=list[PassengerOut])
def get_all_passengers(db: Session = Depends(get_db)):
    return db.query(Passenger).all()
