from pydantic import BaseModel, Field

class ExpenseSchema(BaseModel):
    travel_id: int
    name: str
    price: float
    type: str
    

    