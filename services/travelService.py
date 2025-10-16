from sqlalchemy.orm import Session

from models.travel import create_travel, get_travel_by_id, get_all_travels, get_all_travels_by_user
from models.travel import Travel as TravelModel
from schemas.travel import TravelCreate, TravelUpdate
from db.database import get_db
from fastapi import Depends

def create_travel_service(travel: TravelCreate, db: Session = Depends(get_db)) -> TravelModel:
    return create_travel(db=db, total_price=travel.total_price, total_expenses=travel.total_expenses, is_finished=travel.is_finished, id_user=travel.id_user, qty_passengers=travel.qty_passengers)

def list_travels_service(db: Session = Depends(get_db)):
    return get_all_travels(db=db)

def get_travel_service(travel_id: int, db: Session = Depends(get_db)):
    return get_travel_by_id(db=db, travel_id=travel_id)

def update_travel_service(travel_id: int, travel: TravelUpdate, db: Session = Depends(get_db)):
    t = get_travel_by_id(db=db, travel_id=travel_id)
    if not t:
        return None
    return t.update_travel(db=db, total_price=travel.total_price, total_expenses=travel.total_expenses, is_finished=travel.is_finished)

def delete_travel_service(travel_id: int, db: Session = Depends(get_db)):
    t = get_travel_by_id(db=db, travel_id=travel_id)
    if not t:
        return None
    return t.delete_travel(db=db)

def travel_by_user(db: Session, user_id: int):
    """
    Retorna uma travel específica pertencente a um user.
    """
    return TravelModel.travel_by_user(user_id, db)


def all_travels_by_user(db: Session, user_id: int):
    """
    Retorna todas as travels pertencentes a um user.
    """
    return get_all_travels_by_user(db, user_id)
