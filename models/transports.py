from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base


class Transport(Base):
    __tablename__ = "transports"

    id = Column(Integer, primary_key=True, index=True)
    departure = Column(String(100), nullable=False)
    destination = Column(String(100), nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    type = Column(String(50), nullable=False)
    travel_id = Column(Integer, ForeignKey("travels.id"))

    # Relação inversa (se definires em Travel)
    travel = relationship("Travel", back_populates="transports")