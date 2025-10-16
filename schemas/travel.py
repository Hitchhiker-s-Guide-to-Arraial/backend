from pydantic import BaseModel
from typing import Optional, List


# ===================
# TRANSPORT SCHEMAS
# ===================
class TransportBase(BaseModel):
    departure: str
    destination: str
    price: float
    type: str


class TransportCreate(TransportBase):
    pass


class TransportRead(TransportBase):
    id: int

    class Config:
        orm_mode = True


# ===================
# ACCOMMODATION SCHEMAS
# ===================
class AccommodationBase(BaseModel):
    type: str
    lodging_price: float
    meal_price: float


class AccommodationCreate(AccommodationBase):
    pass


class AccommodationRead(AccommodationBase):
    id: int

    class Config:
        orm_mode = True


# ===================
# TRAVEL SCHEMAS
# ===================
class TravelBase(BaseModel):
    total_price: float = 0
    total_expenses: float = 0
    qty_passangers: int
    is_finished: bool = False
    is_deleted: bool = False


class TravelCreate(TravelBase):
    transports: Optional[List[TransportCreate]] = []
    accommodations: Optional[List[AccommodationCreate]] = []


class TravelRead(TravelBase):
    id: int
    transports: List[TransportRead] = []
    accommodations: List[AccommodationRead] = []
    


    class Config:
        orm_mode = True
