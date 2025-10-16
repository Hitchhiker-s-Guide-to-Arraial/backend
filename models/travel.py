from fastapi import Depends
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from db.database import Base, get_db


class Travel(Base):
    __tablename__ = "travels"

    id = Column(Integer, primary_key=True, index=True)
    total_price = Column(Float, nullable=False)
    total_expenses = Column(Float, nullable=False)
    qty_passengers = Column(Integer, nullable=False)
    is_finished = Column(Integer, default=0)
    is_deleted = Column(Integer, default=0)
    id_user = Column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="travels")
    
    def get_all_travels_by_user(user_id: int, db: Session = Depends(get_db)):
        """
        Retorna todas as travels pertencentes a um user.
        """
        return db.query(Travel).filter(Travel.id_user == user_id).all()
    
    
    def travel_by_user(user_id: int, travel_id: int, db: Session = Depends(get_db)):
        """
        Retorna uma travel específica pertencente a um user.
        """
        return db.query(Travel).filter(Travel.id == travel_id, Travel.id_user == user_id).first()   

    class Config:
        orm_mode = True
