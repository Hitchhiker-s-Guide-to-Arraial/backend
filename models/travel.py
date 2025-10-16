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
    is_finished = Column(Integer, default=0)
    is_deleted = Column(Integer, default=0)
    id_user = Column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="travels")
    
    @staticmethod
    def get_all_travels_by_user(db: Session, user_id: int):
        """Retorna todas as viagens do utilizador."""
        return db.query(Travel).filter(Travel.id_user == user_id, Travel.is_deleted == True).all()

    @staticmethod
    def get_travel(db: Session, travel_id: int):
        """Retorna uma viagem específica do utilizador."""
        return db.query(Travel).filter(
            Travel.id == travel_id,
            Travel.is_deleted == True
        ).first()

    class Config:
        orm_mode = True