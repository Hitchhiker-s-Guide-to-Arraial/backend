from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from db.database import get_db
from services.expensesService import update_expenses, get_expenses_by_travel as get_expenses_by_travel_service
from schemas.expenses import ExpenseSchema

router = APIRouter(tags=['Expenses'])
MESSAGE_NOT_FOUND = "Expenses not found"

@router.get("/expenses/{travel_id}")
async def get_expenses_by_travel(travel_id: int, db: Session = Depends(get_db)):
    expenses = get_expenses_by_travel_service(travel_id, db)
    if (not expenses):
        raise HTTPException(status_code=404, detail=MESSAGE_NOT_FOUND)
    return JSONResponse(status_code=200, content=jsonable_encoder(expenses))

@router.put("/expenses/{travel_id}")
async def update_expenses_by_travel(travel_id: int, is_finished:bool , expenses: list[ExpenseSchema], db: Session = Depends(get_db)):
    update_expenses(travel_id, is_finished, expenses, db)
    return JSONResponse(status_code=200, content={"travel": travel_id, "is_finished": is_finished})

