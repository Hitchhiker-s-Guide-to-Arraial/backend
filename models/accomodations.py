from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Accommodation(Base):
    __tablename__ = "accommodations"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String(50), nullable=False)
    lodging_price = Column(Numeric(10, 2), nullable=False)
    meal_price = Column(Numeric(10, 2), nullable=False)
    travel_id = Column(Integer, ForeignKey("travels.id"))

    travel = relationship("Travel", back_populates="accommodations")