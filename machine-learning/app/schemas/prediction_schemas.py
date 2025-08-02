from pydantic import BaseModel, Field
from typing import Literal

# Al no poder obtener los nombres de las features del modelo, opté por deducirlo a partir de los valores del ejemplo en "challenge-genai.ipynb"
# Hay una extra-assumption que estoy haciendo que es suponer que 0 = female y 1 = male
# Esta misma explicación se encuentra en el README.md

# Pydantic Object para las features de input para la predicción
class FeaturesInput(BaseModel):
    pclass: Literal[1, 2, 3] = Field(..., description="Passenger class (1 = 1st, 2 = 2nd, 3 = 3rd)")
    sex: Literal[0, 1] = Field(..., description="Sex (0 = female, 1 = male)")
    age: float = Field(..., ge=0, description="Age in years")
    sibsp: int = Field(..., ge=0, description="Number of siblings/spouses aboard")
    parch: int = Field(..., ge=0, description="Number of parents/children aboard")
    fare: float = Field(..., ge=0, description="Passenger fare")
    embarked: Literal[0, 1, 2] = Field(..., description="Port of Embarkation (0 = Southampton, 1 = Cherbourg, 2 = Queenstown)")


# Pydantic Object para el resultado de la predicción
class Prediction(BaseModel):
    score: float = Field(..., description="Prediction result")
    decision: int = Field(..., description="Final result according to models's score and threshold")
    description: str = Field(..., description="Description of final result")