from pydantic import BaseModel, Field

# Al no poder obtener los nombres de las features del modelo, opté por deducirlo a partir de los valores del ejemplo en "challenge-genai.ipynb"
# Hay una extra-assumption que estoy haciendo que es suponer que 0 = female y 1 = male
class FeaturesInput(BaseModel):
    pclass: int = Field(..., description="Passenger class (1 = 1st, 2 = 2nd, 3 = 3rd)")
    sex: int = Field(..., description="Sex (0 = female, 1 = male)")
    age: float = Field(..., description="Age in years")
    sibsp: int = Field(..., description="Number of siblings/spouses aboard")
    parch: int = Field(..., description="Number of parents/children aboard")
    fare: float = Field(..., description="Passenger fare")
    embarked: int = Field(..., description="Port of Embarkation (0 = Southampton, 1 = Cherbourg, 2 = Queenstown)")



class Prediction(BaseModel):
    score: float = Field(..., description="Prediction result")
    decision: int = Field(..., description="Final result according to models's score and threshold")
    description: str = Field(..., description="Description of final result")