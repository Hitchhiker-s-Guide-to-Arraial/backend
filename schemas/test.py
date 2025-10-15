from pydantic import BaseModel, Field


class TestSchema(BaseModel):
    name: str
    price: float
