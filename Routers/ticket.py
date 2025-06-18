from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
from Model import Ticket, Passenger, Schedule
from schemas import TicketCreate, TicketOut

router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"]
)

@router.post("/", response_model=TicketOut)
def book_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):
    passenger = db.query(Passenger).filter(Passenger.id == ticket.passenger_id).first()
    schedule = db.query(Schedule).filter(Schedule.id == ticket.schedule_id).first()

    if not passenger:
        raise HTTPException(status_code=404, detail="Passenger not found")
    if not schedule:
        raise HTTPException(status_code=404, detail="Schedule not found")

    new_ticket = Ticket(**ticket.dict())
    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)
    return new_ticket

@router.get("/", response_model=list[TicketOut])
def get_all_tickets(db: Session = Depends(get_db)):
    return db.query(Ticket).all()

@router.get("/{ticket_id}", response_model=TicketOut)
def get_ticket_by_id(ticket_id: int, db: Session = Depends(get_db)):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket