from fastapi import Depends
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import Session

from db.database import Base, get_db
from schemas.test import TestSchema

class Test(Base):
    __tablename__ = 'tests'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float, index=True)
    
    def get_test_by_id(test_id: int, db: Session = Depends(get_db)):
        return db.query(Test).filter(Test.id == test_id).first()
    
    def get_all_tests(db: Session = Depends(get_db)):
        return db.query(Test).all()

    def delete_test(test_id: int, db: Session = Depends(get_db)):
        db_test = db.query(Test).filter(Test.id == test_id).first()
        if db_test:
            db.delete(db_test)
            db.commit()
        return db_test

    def update_test(test_id: int, test: TestSchema, db: Session = Depends(get_db)):
        db_test = db.query(Test).filter(Test.id == test_id).first()
        if db_test:
            db_test.name = test.name
            db_test.price = test.price
            db.commit()
            db.refresh(db_test)
        return db_test
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price
        }

def create_test(test: TestSchema, db: Session = Depends(get_db)):
    db_test = Test(name=test.name, price=test.price)
    db.add(db_test)
    db.commit()
    db.refresh(db_test)
    return db_test