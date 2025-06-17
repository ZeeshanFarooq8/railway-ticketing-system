from pydantic import BaseModel

class TrainCreate(BaseModel):
    name: str
    capacity: int

class TrainOut(BaseModel):
    id: int
    name: str
    capacity: int

    class Config:
        orm_mode = True
        from_attributes = True
