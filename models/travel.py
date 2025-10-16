from typing import Optional
import uuid
from decimal import Decimal

from sqlalchemy import Column, Boolean, Numeric
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Session

from db.database import Base

"""
Travel model + helper functions.

Columns:
- id
- total_price
- total_expenses
- is_finished
- is_deleted
"""

class Travel(Base):
    __tablename__ = "travels"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    total_price = Column(Numeric(12, 2), nullable=False, default=Decimal("0.00"))
    total_expenses = Column(Numeric(12, 2), nullable=False, default=Decimal("0.00"))
    is_finished = Column(Boolean, nullable=False, default=False)
    is_deleted = Column(Boolean, nullable=False, default=False)

    def update_travel(self, db: Session, *, total_price: Optional[Decimal] = None,
                      total_expenses: Optional[Decimal] = None, is_finished: Optional[bool] = None):
        """
        Update provided fields on this Travel instance and commit.
        """
        if total_price is not None:
            self.total_price = total_price
        if total_expenses is not None:
            self.total_expenses = total_expenses
        if is_finished is not None:
            self.is_finished = is_finished

        db.add(self)
        db.commit()
        db.refresh(self)
        return self

    def delete_travel(self, db: Session):
        """
        Soft-delete: mark is_deleted True and commit.
        """
        self.is_deleted = True
        db.add(self)
        db.commit()
        db.refresh(self)
        return self

    def __repr__(self):
        return f"<Travel id={self.id} total_price={self.total_price} total_expenses={self.total_expenses} finished={self.is_finished} deleted={self.is_deleted}>"


def create_travel(db: Session, *, total_price: Decimal = Decimal("0.00"), total_expenses: Decimal = Decimal("0.00"),
                  is_finished: bool = False) -> Travel:
    """
    Create and persist a new Travel row.
    """
    new = Travel(
        total_price=total_price,
        total_expenses=total_expenses,
        is_finished=is_finished,
        is_deleted=False
    )
    db.add(new)
    db.commit()
    db.refresh(new)
    return new


def get_travel_by_id(db: Session, travel_id: uuid.UUID, include_deleted: bool = False) -> Optional[Travel]:
    q = db.query(Travel).filter(Travel.id == travel_id)
    if not include_deleted:
        q = q.filter(Travel.is_deleted == False)
    return q.first()


def get_all_travels(db: Session, include_deleted: bool = False):
    q = db.query(Travel)
    if not include_deleted:
        q = q.filter(Travel.is_deleted == False)
    return q.all()