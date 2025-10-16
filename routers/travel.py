from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from db.database import get_db
from schemas.travel import TravelRead
from services import travelService
from services.travelService import travel_by_user, all_travels_by_user

"""
Ficheiro de Router do Test

Nos ficheiros de router definimos os endpoints da API, para ser acessiveis.
"""

# Importante incluir o router para depois ir para a main.py e a tag é usada na documentação/ swagger
router = APIRouter(prefix="/travels", tags=["Travels"])
MESSAGE_NOT_FOUND = "Travel not found"

@router.get("/user/{user_id}/{travel_id}", response_model=TravelRead)
def read_user_travel(user_id: int, travel_id: int, db: Session = Depends(get_db)):
    travel = travelService.travel_by_user(db, user_id=user_id, travel_id=travel_id)
    if not travel:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Travel not found for user")
    return travel


@router.get("/{user_id}", response_model=TravelRead)
def read_user_travel(user_id: int, db: Session = Depends(get_db)):
    travel = travelService.all_travels_by_user(db, user_id=user_id)
    if not travel:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Travel not found for user"
        )
    return travel