from pydantic import BaseModel
from uuid import UUID
from decimal import Decimal
from typing import Optional

class TravelBase(BaseModel):
    total_price: Optional[Decimal] = Decimal("0.00")
    total_expenses: Optional[Decimal] = Decimal("0.00")
    is_finished: Optional[bool] = False

class TravelCreate(TravelBase):
    pass

class TravelUpdate(BaseModel):
    total_price: Optional[Decimal] = None
    total_expenses: Optional[Decimal] = None
    is_finished: Optional[bool] = None

class TravelOut(TravelBase):
    id: UUID
    is_deleted: bool

    class Config:
        orm_mode = True