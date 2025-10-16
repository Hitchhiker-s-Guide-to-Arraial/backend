from sqlalchemy.orm import Session
from models.travel import Travel

def get_travel(db: Session, user_id: int, travel_id: int):
    """
    Retorna uma travel específica pertencente a um user.
    """
    return Travel.get_travel(travel_id, db)


def all_travels_by_user(db: Session, user_id: int):
    """
    Retorna todas as travels pertencentes a um user.
    """
    return Travel.get_all_travels_by_user(user_id, db)