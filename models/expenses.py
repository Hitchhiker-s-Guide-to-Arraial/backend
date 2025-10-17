from fastapi import Depends
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import Session

from db.database import Base, get_db
from schemas.expenses import ExpenseSchema


class Expenses(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True, index=True)
    travel_id = Column(Integer, foreign_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float, index=True)
    type = Column(String, index=True)
    
    def get_expenses_by_travel(travel_id: int, db: Session = Depends(get_db)):
       return db.query(Expenses).where(Expenses.travel_id == travel_id)
    
    def to_dict(self):
        return {
            "id": self.id,
            "travel_id": self.travel_id,
            "name": self.name,
            "price": self.price,
            "type": self.type
        }

def create_expense(expense: ExpenseSchema, db: Session = Depends(get_db)) -> int:
    db_expense = Expenses(travel_id=expense.travel_id, name=expense.name, price=expense.price, type=expense.type)
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense.price