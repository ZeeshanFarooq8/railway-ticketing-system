from pydantic import BaseModel

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
