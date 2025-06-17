from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from db import Base
from datetime import datetime

class Train(Base):
    __tablename__ = "trains"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    capacity = Column(Integer)

    routes = relationship("Route", back_populates="train")
    schedules = relationship("Schedule", back_populates="train")


class Route(Base):
    __tablename__ = "routes"
    id = Column(Integer, primary_key=True, index=True)
    train_id = Column(Integer, ForeignKey("trains.id"))
    source = Column(String)
    destination = Column(String)
    distance_km = Column(Integer)

    train = relationship("Train", back_populates="routes")
    schedules = relationship("Schedule", back_populates="route")


class Schedule(Base):
    __tablename__ = "schedules"
    id = Column(Integer, primary_key=True, index=True)
    train_id = Column(Integer, ForeignKey("trains.id"))
    route_id = Column(Integer, ForeignKey("routes.id"))
    departure_time = Column(DateTime)
    arrival_time = Column(DateTime)

    train = relationship("Train", back_populates="schedules")
    route = relationship("Route", back_populates="schedules")
    tickets = relationship("Ticket", back_populates="schedule")


class Passenger(Base):
    __tablename__ = "passengers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    phone = Column(String)

    tickets = relationship("Ticket", back_populates="passenger")


class Ticket(Base):
    __tablename__ = "tickets"
    id = Column(Integer, primary_key=True, index=True)
    passenger_id = Column(Integer, ForeignKey("passengers.id"))
    schedule_id = Column(Integer, ForeignKey("schedules.id"))
    seat_number = Column(String)
    booking_time = Column(DateTime, default=datetime.utcnow)

    passenger = relationship("Passenger", back_populates="tickets")
    schedule = relationship("Schedule", back_populates="tickets")
