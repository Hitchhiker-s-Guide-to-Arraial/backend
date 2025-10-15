from fastapi import Depends
from sqlalchemy.orm import Session

from db.database import get_db
from schemas.test import TestSchema
from models.test import Test as TestModel, create_test


def new_test(test: TestSchema, db: Session = Depends(get_db)):
    return create_test(test=test, db=db)


def get_all_tests(db: Session = Depends(get_db)):
    return db.query(TestModel).filter().all()


def get_test_by_id(test_id: str, db: Session = Depends(get_db)):
    return db.query(TestModel).filter(TestModel.id == test_id).first()

def delete_test(test_id: str, db: Session = Depends(get_db)):
    test_toBe_deleted = db.query(TestModel).filter(TestModel.id == test_id).first()
    if test_toBe_deleted:
        test_toBe_deleted.delete_test(test_id=test_id, db=db)
    return test_toBe_deleted

def update_test(test_id: str, test: TestSchema, db: Session = Depends(get_db)):
    test_toBe_updated = db.query(TestModel).filter(TestModel.id == test_id).first()
    if test_toBe_updated:
        test_toBe_updated.update_test(test_id=test_id, test=test, db=db)
    return test_toBe_updated