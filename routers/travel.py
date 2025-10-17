from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from typing import List


from db.database import get_db
from schemas.travel import TravelCreate, TravelOut, TravelUpdate, TravelRead
from services.travelService import create_travel_service, list_travels_service, get_travel_service, update_travel_service, delete_travel_service, travel_by_user, all_travels_by_user


# Importante incluir o router para depois ir para a main.py e a tag é usada na documentação/ swagger

router = APIRouter(prefix="/travels", tags=["travels"])
MESSAGE_NOT_FOUND = "Travel not found"

@router.post("/", response_model=TravelOut, status_code=status.HTTP_201_CREATED)
def create_travel(travel: TravelCreate, db=Depends(get_db)):
    created = create_travel_service(travel=travel, db=db)
    return created

@router.get("/", response_model=List[TravelOut])
def list_travels(db=Depends(get_db)):
    return list_travels_service(db=db)

@router.get("/{travel_id}", response_model=TravelOut)
def get_travel(travel_id: int, db=Depends(get_db)):
    t = get_travel_service(travel_id=travel_id, db=db)
    if not t:
        raise HTTPException(status_code=404, detail="Travel not found")
    return t

@router.put("/{travel_id}", response_model=TravelOut)
def update_travel(travel_id: int, travel: TravelUpdate, db=Depends(get_db)):
    t = update_travel_service(travel_id=travel_id, travel=travel, db=db)
    if not t:
        raise HTTPException(status_code=404, detail="Travel not found")
    return t

@router.delete("/{travel_id}", response_model=TravelOut)
def delete_travel(travel_id: int, db=Depends(get_db)):
    t = delete_travel_service(travel_id=travel_id, db=db)
    if not t:
        raise HTTPException(status_code=404, detail="Travel not found")
    return t

@router.get("/user/{user_id}", response_model=List[TravelRead])
def read_user_travel(user_id: int, db: Session = Depends(get_db)):
    travels = all_travels_by_user(db, user_id)
    if not travels:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Travel not found for user")
    return travels

