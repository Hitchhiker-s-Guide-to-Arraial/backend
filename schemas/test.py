from pydantic import BaseModel, Field

"""
Schema para o modelo de Test

o Schema é usado para validar os dados de entrada e saída da API, 
    garantindo que os dados estão no formato correto.
    
O TestSchema é usado para criar novos testes 
o UpdateTestDescriptionSchema é usado para atualizar a descrição de um teste existente, dai incluir o id
"""
class TestSchema(BaseModel):
    name: str
    price: float
    
    # exemplo de um campo com um valor de exemplo para mostrar na documentação/ swagger
    description: str = Field(..., example="This is a sample description.")
    
    # exemplo de um campo com um valor por defeito
    available: bool = Field(..., default=True)

class UpdateTestDescriptionSchema(BaseModel):
    id: int
    description: str = Field(..., example="This is a sample description.")