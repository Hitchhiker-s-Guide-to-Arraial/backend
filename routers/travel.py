from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from typing import List
from uuid import UUID

from db.database import get_db
from services.testService import new_test, get_all_tests, get_test_by_id, delete_test, update_test
from schemas.test import TestSchema, UpdateTestDescriptionSchema
from schemas.travel import TravelCreate, TravelOut, TravelUpdate
from services.travelService import create_travel_service, list_travels_service, get_travel_service, update_travel_service, delete_travel_service

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
def get_travel(travel_id: UUID, db=Depends(get_db)):
    t = get_travel_service(travel_id=travel_id, db=db)
    if not t:
        raise HTTPException(status_code=404, detail="Travel not found")
    return t

@router.put("/{travel_id}", response_model=TravelOut)
def update_travel(travel_id: UUID, travel: TravelUpdate, db=Depends(get_db)):
    t = update_travel_service(travel_id=travel_id, travel=travel, db=db)
    if not t:
        raise HTTPException(status_code=404, detail="Travel not found")
    return t

@router.delete("/{travel_id}", response_model=TravelOut)
def delete_travel(travel_id: UUID, db=Depends(get_db)):
    t = delete_travel_service(travel_id=travel_id, db=db)
    if not t:
        raise HTTPException(status_code=404, detail="Travel not found")
    return t

"""
Ficheiro de Router do Test

Nos ficheiros de router definimos os endpoints da API, para ser acessiveis.


@router.post("/test")
# Aqui por exemplo usamos o TestSchema para validar o input de criarmos um teste
async def create_test(test: TestSchema, db: Session = Depends(get_db)):
    return JSONResponse(status_code=201, content=jsonable_encoder(new_test(test=test, db=db).to_dict()))

@router.put("/test/{test_id}")
async def modify_test(test_id: str, test: UpdateTestDescriptionSchema, db: Session = Depends(get_db)):
    existing_test = get_test_by_id(test_id=test_id, db=db)
    if not existing_test:
        raise HTTPException(status_code=404, detail=MESSAGE_NOT_FOUND)
    existing_test.update_test(test_id=test_id, test=test, db=db)
    return JSONResponse(status_code=200, content=jsonable_encoder(existing_test.to_dict()))

@router.delete("/test/{test_id}")
async def delete_test_router(test_id: str, db: Session = Depends(get_db)):
    existing_test = get_test_by_id(test_id=test_id, db=db)
    if not existing_test:
        raise HTTPException(status_code=404, detail=MESSAGE_NOT_FOUND)
    existing_test.delete_test(db=db)
    return JSONResponse(status_code=200, content=jsonable_encoder({"message": "DELETE DATA SUCCESS"}))


@router.get("/test")
async def fetch_all_tests(db: Session = Depends(get_db)):
    return JSONResponse(status_code=200, content=jsonable_encoder([test.to_dict() for test in get_all_tests(db=db)]))

@router.get("/test/{test_id}")
async def fetch_test_by_id(test_id: str, db: Session = Depends(get_db)):
    existing_test = get_test_by_id(test_id=test_id, db=db)
    if not existing_test:
        raise HTTPException(status_code=404, detail=MESSAGE_NOT_FOUND)
    return JSONResponse(status_code=200, content=jsonable_encoder(existing_test.to_dict()))
"""