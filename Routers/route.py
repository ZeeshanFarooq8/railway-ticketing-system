from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
import Model
import schemas

router = APIRouter(prefix="/routes", tags=["Routes"])

@router.post("/", response_model=schemas.RouteOut)
def create_route(route: schemas.RouteCreate, db: Session = Depends(get_db)):
    train = db.query(Model.Train).filter(Model.Train.id == route.train_id).first()
    if not train:
        raise HTTPException(status_code=404, detail="Train not found")

    new_route = Model.Route(
        source=route.source,
        destination=route.destination,
        duration=route.duration,
        fare=route.fare,
        train_id=route.train_id
    )
    db.add(new_route)
    db.commit()
    db.refresh(new_route)
    return new_route

@router.get("/", response_model=list[schemas.RouteOut])
def get_all_routes(db: Session = Depends(get_db)):
    return db.query(Model.Route).all()
