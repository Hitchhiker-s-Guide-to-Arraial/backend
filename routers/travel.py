from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from db.database import get_db
from services.testService import new_test, get_all_tests, get_test_by_id, delete_test, update_test
from schemas.test import TestSchema, UpdateTestDescriptionSchema

"""
Ficheiro de Router do Test

Nos ficheiros de router definimos os endpoints da API, para ser acessiveis.
"""

# Importante incluir o router para depois ir para a main.py e a tag é usada na documentação/ swagger
router = APIRouter(prefix="/travels", tags=["Travels"])
MESSAGE_NOT_FOUND = "Travel not found"


@router.post("/create_travel", status_code=201)
# Aqui por exemplo usamos o TestSchema para validar o input de criarmos um teste
async def create_travel(test: TestSchema, db: Session = Depends(get_db)):
    return JSONResponse(status_code=201, content=jsonable_encoder(new_test(test=test, db=db).to_dict()))

@router.get("/travels")
async def get_all_travels(db: Session = Depends(get_db)):
    return JSONResponse(status_code=200, content=jsonable_encoder([test.to_dict() for test in get_all_tests(db=db)]))

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
