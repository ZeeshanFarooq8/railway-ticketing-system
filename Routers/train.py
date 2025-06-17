from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import SessionLocal
from db import get_db
import Model
import schemas
from Routers import train

router = APIRouter(prefix="/trains", tags=["Trains"])

@router.post("/", response_model=schemas.TrainOut)
def create_train(train: schemas.TrainCreate, db: Session = Depends(get_db)):
    db_train = db.query(Model.Train).filter(Model.Train.name == train.name).first()
    if db_train:
        raise HTTPException(status_code=400, detail="Train already exists")
    new_train = Model.Train(name=train.name, capacity=train.capacity)
    db.add(new_train)
    db.commit()
    db.refresh(new_train)
    return new_train

@router.get("/", response_model=list[schemas.TrainOut])
def get_all_trains(db: Session = Depends(get_db)):
    return db.query(models.Train).all()
