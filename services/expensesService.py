from fastapi import Depends
from sqlalchemy.orm import Session

from db.database import get_db
from schemas.expenses import ExpenseSchema
from schemas.travel import TravelUpdate
from models.expenses import Expenses as ExpensesModel, create_expense
from models.travel import get_travel_by_id
from services.travelService import update_travel_service


# def new_test(test: TestSchema, db: Session = Depends(get_db)):
#     # Exemplo. Neste caso podiamos colocar aqui alguma lógica de validação ou transformação dos dados
#     # antes de criar o novo teste
#     return create_test(test=test, db=db)


def get_expenses_by_travel(travel_id: int, db: Session = Depends(get_db)):
    return db.query(ExpensesModel).where(ExpensesModel.travel_id == travel_id).all()


def update_expenses(travel_id: int, is_finished:bool, expenses: list[ExpenseSchema], db: Session = Depends(get_db)):
    value = float(get_travel_by_id(db, travel_id, False).total_expenses)
    added_value = 0.0
    for e in expenses:
        added_value += create_expense(e, db)
    travel_update = TravelUpdate(is_finished = is_finished, total_expenses = value+added_value)
    update_travel_service(travel_id, travel_update, db)
    