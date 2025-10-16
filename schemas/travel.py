from pydantic import BaseModel
from decimal import Decimal
from typing import Optional, List

class TravelBase(BaseModel):
    total_price: Optional[Decimal] = Decimal("0.00")
    total_expenses: Optional[Decimal] = Decimal("0.00")
    is_finished: Optional[bool] = False
    is_deleted: Optional[bool] = False
    qty_passengers: int

class TravelCreate(TravelBase):
    id_user: int

class TravelUpdate(BaseModel):
    total_price: Optional[Decimal] = None
    total_expenses: Optional[Decimal] = None
    is_finished: Optional[bool] = None

class TravelOut(TravelBase):
    id: int
    is_deleted: bool

    class Config:
        orm_mode = True

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


""""
class TravelCreate(TravelBase):
    transports: Optional[List[TransportCreate]] = []
    accommodations: Optional[List[AccommodationCreate]] = []
"""

class TravelRead(TravelBase):
    id: int
    transports: List[TransportRead] = []
    accommodations: List[AccommodationRead] = []
    


    class Config:
        orm_mode = True
