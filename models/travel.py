from fastapi import Depends
from typing import Optional
from decimal import Decimal

from sqlalchemy import Column, Boolean, Numeric, Integer, String, Float, ForeignKey
from sqlalchemy.orm import Session, relationship

from db.database import Base, get_db

"""
Travel model + helper functions.
"""

class Travel(Base):
    __tablename__ = "travels"

    id = Column(Integer, primary_key=True, index=True)
    total_price = Column(Numeric(10, 2), nullable=False, default=Decimal("0.00"))
    total_expenses = Column(Numeric(10, 2), nullable=False, default=Decimal("0.00"))
    qty_passengers = Column(Integer, nullable=False, default=1)
    is_finished = Column(Boolean, nullable=False, default=False)
    is_deleted = Column(Boolean, nullable=False, default=False)
    id_user = Column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="travels")
    
    
    
    def travel_by_user(user_id: int, db: Session = Depends(get_db)):
        """
        Retorna uma travel específica pertencente a um user.
        """
        return db.query(Travel).filter(Travel.id_user == user_id).first()   


    def update_travel(self, db: Session, *, total_price: Optional[Decimal] = None,
                      total_expenses: Optional[Decimal] = None, is_finished: Optional[bool] = None, qty_passengers: Optional[int] = None):
        """
        Retorna todas as travels pertencentes a um user.
        """
        if total_price is not None:
            self.total_price = total_price
        if total_expenses is not None:
            self.total_expenses = total_expenses
        if is_finished is not None:
            self.is_finished = is_finished
        if qty_passengers is not None:
            self.qty_passengers = qty_passengers

        db.add(self)
        db.commit()
        db.refresh(self)
        return self

    def delete_travel(self, db: Session):
        """
        Retorna uma travel específica pertencente a um user.
        """
        return db.query(Travel).filter(Travel.id == self.id).first()   

    def __repr__(self):
        return f"<Travel id={self.id} total_price={self.total_price} total_expenses={self.total_expenses} finished={self.is_finished} deleted={self.is_deleted} id_user={self.id_user} qty_passengers={self.qty_passengers}>"


def create_travel(db: Session, *, total_price: Decimal = Decimal("0.00"), total_expenses: Decimal = Decimal("0.00"),
                  is_finished: bool = False, qty_passengers: Optional[int] = 1, id_user: int) -> Travel:
    """
    Create and persist a new Travel row.
    """
    new = Travel(
        total_price=total_price,
        total_expenses=total_expenses,
        is_finished=is_finished,
        is_deleted=False,
        qty_passengers=qty_passengers,
        id_user=id_user
    )
    db.add(new)
    db.commit()
    db.refresh(new)
    return new


def get_travel_by_id(db: Session, travel_id: int, include_deleted: bool = False) -> Optional[Travel]:
    q = db.query(Travel).filter(Travel.id == travel_id)
    if not include_deleted:
        q = q.filter(Travel.is_deleted == False)
    return q.first()


def get_all_travels(db: Session, include_deleted: bool = False):
    q = db.query(Travel)
    if not include_deleted:
        q = q.filter(Travel.is_deleted == False)
    return q.all()

def get_all_travels_by_user(db: Session, user_id: int, include_deleted: bool = False):
        """
        Retorna todas as travels pertencentes a um user.
        """
        q = db.query(Travel).filter(Travel.id_user == user_id)
        if not include_deleted:
            q = q.filter(Travel.is_deleted == False)
        return q.all()  
