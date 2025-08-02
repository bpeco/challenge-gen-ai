from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from app.schemas.prediction_schemas import FeaturesInput, Prediction
from typing import Optional
from config import MODEL_PATH, THRESHOLD
import numpy as np
import joblib
from contextlib import asynccontextmanager


model = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        loaded_model = joblib.load(MODEL_PATH)
        model['rfc_model'] = loaded_model
        yield
    
    except FileNotFoundError:
        raise HTTPException(500, "Model not found")
    
    except:
        raise HTTPException(500, "Error while loading the model.")


app = FastAPI(title='Titanic Suvivor Predictos', 
              version='1.0.0',
              lifespan=lifespan)


@app.get("/health")
def health():
    return {
        "status": "ok",
        "model_loaded": bool(model.get('rfc_model'))
    }

@app.post('/predict', status_code=200)
def predict(input: FeaturesInput) -> Prediction:

    input_arr = np.array([[
        input.pclass,
        input.sex,
        input.age,
        input.sibsp,
        input.parch,
        input.fare,
        input.embarked
    ]])

    try:

        score = model['rfc_model'].predict_proba(input_arr)[0][1]
        decision = 1 if score >= THRESHOLD else 0
        decision_description = 'Sobrevivió' if decision == 1 else 'No sobrevivió'

        prediction_result = Prediction(score=score,
                                       decision=decision,
                                       description=decision_description)
        
        return prediction_result
        

    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error en la predicción: {e}')
