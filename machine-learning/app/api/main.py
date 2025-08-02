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


# Se carga el modelo al levantar la app
@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        loaded_model = joblib.load(MODEL_PATH)
        model['rfc_model'] = loaded_model
        yield
    
    except FileNotFoundError:
        raise HTTPException(500, "Modelo no encontrado.")
    
    except:
        raise HTTPException(500, "Error al intentar cargar el modelo.")


app = FastAPI(title='Titanic Suvivor Predictor', 
              version='1.0.0',
              lifespan=lifespan)


# Endpoint para validar el estado de la app
@app.get("/health")
def health():
    return {
        "status": "ok",
        "model_loaded": bool(model.get('rfc_model'))
    }


# Endpoint para predecir
@app.post('/predict', status_code=200)
def predict(input: FeaturesInput) -> Prediction:

    # Conversión para la predicción
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

        # Estructura del resultado final
        prediction_result = Prediction(score=score,
                                       decision=decision,
                                       description=decision_description)
        
        return prediction_result
        

    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error en la predicción: {e}')
