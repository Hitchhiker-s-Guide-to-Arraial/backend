from fastapi import Depends
from sqlalchemy.orm import Session

from db.database import get_db
from schemas.expenses import ExpenseSchema
from models.expenses import Expenses as ExpensesModel, create_expense


# def new_test(test: TestSchema, db: Session = Depends(get_db)):
#     # Exemplo. Neste caso podiamos colocar aqui alguma lógica de validação ou transformação dos dados
#     # antes de criar o novo teste
#     return create_test(test=test, db=db)


def get_expenses_by_travel(travel_id: int, db: Session = Depends(get_db)):
    return db.query(ExpensesModel).where(ExpensesModel.travel_id == travel_id)


# def get_test_by_id(test_id: str, db: Session = Depends(get_db)):
#     return db.query(TestModel).filter(TestModel.id == test_id).first()

# def delete_test(test_id: str, db: Session = Depends(get_db)):
#     test_toBe_deleted = db.query(TestModel).filter(TestModel.id == test_id).first()
#     if test_toBe_deleted:
#         test_toBe_deleted.delete_test(test_id=test_id, db=db)
#     return test_toBe_deleted

# def update_test(test_id: str, test: UpdateTestDescriptionSchema, db: Session = Depends(get_db)):
#     test_toBe_updated = db.query(TestModel).filter(TestModel.id == test_id).first()
#     if test_toBe_updated:
#         test_toBe_updated.update_test(test_id=test_id, test=test, db=db)
#     return test_toBe_updated