
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from Model import Schedule
from schemas import ScheduleCreate, ScheduleOut

router = APIRouter(
    prefix="/schedules",
    tags=["Schedules"]
)

@router.post("/", response_model=ScheduleOut)
def create_schedule(schedule: ScheduleCreate, db: Session = Depends(get_db)):
    new_schedule = Schedule(**schedule.dict())
    db.add(new_schedule)
    db.commit()
    db.refresh(new_schedule)
    return new_schedule

@router.get("/", response_model=list[ScheduleOut])
def get_all_schedules(db: Session = Depends(get_db)):
    return db.query(Schedule).all()

@router.get("/{schedule_id}", response_model=ScheduleOut)
def get_schedule(schedule_id: int, db: Session = Depends(get_db)):
    return db.query(Schedule).filter(Schedule.id == schedule_id).first()
