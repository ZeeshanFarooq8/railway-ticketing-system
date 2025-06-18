from pydantic import BaseModel
from pydantic import BaseModel, EmailStr
from datetime import datetime

class TrainCreate(BaseModel):
    name: str
    capacity: int

class TrainOut(BaseModel):
    id: int
    name: str
    capacity: int

    class Config:
        from_attributes = True  # only this for Pydantic v2

class RouteCreate(BaseModel):
    source: str
    destination: str
    duration: str
    fare: int
    train_id: int

class RouteOut(BaseModel):
    id: int
    source: str
    destination: str
    duration: str
    fare: int
    train_id: int

    class Config:
        from_attributes = True  # only this


class PassengerCreate(BaseModel):
    name: str
    age: int
    email: EmailStr

class PassengerOut(BaseModel):
    id: int
    name: str
    age: int
    email: EmailStr

    class Config:
        from_attributes = True


class TicketCreate(BaseModel):
    passenger_id: int
    schedule_id: int
    seat_number: str

class TicketOut(BaseModel):
    id: int
    passenger_id: int
    schedule_id: int
    seat_number: str
    booking_time: datetime

    class Config:
        from_attributes = True

class ScheduleCreate(BaseModel):
    train_id: int
    route_id: int
    departure_time: datetime
    arrival_time: datetime

class ScheduleOut(BaseModel):
    id: int
    train_id: int
    route_id: int
    departure_time: datetime
    arrival_time: datetime

    class Config:
        from_attributes = True
