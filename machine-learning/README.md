# API de Predicción de Supervivencia del Titanic

API desarrollada con FastAPI para predecir la supervivencia de pasajeros del Titanic utilizando un modelo Random Forest pre-entrenado.

> **Desarrollado por:** Bautista Peco  

> **Proyecto:** Challenge GenAI - Machine Learning

> **Fecha:** Agosto 2025

## Modelo Entrenado

El modelo utilizado (`modelo_titanic.joblib`) es un Random Forest que predice la supervivencia (`survived`) basándose en características del pasajero como clase, edad, sexo, número de acompañantes y tarifa pagada.

## Funcionalidades

### Endpoints Disponibles

- **POST `/predict`**: Recibe datos de un pasajero y retorna la predicción de supervivencia
- **GET `/health`**: Health check de la aplicación y verificación de carga del modelo

### Validación de Datos

Validación completa usando Pydantic para los siguientes campos:

- `pclass`: Clase del pasajero (1 = 1st, 2 = 2nd, 3 = 3rd)
- `sex`: Sexo (0 = female, 1 = male)
- `age`: Edad en años
- `sibsp`: Número de hermanos/cónyuges a bordo
- `parch`: Número de padres/hijos a bordo
- `fare`: Tarifa pagada por el ticket
- `embarked`: Puerto de embarque (0 = Southampton, 1 = Cherbourg, 2 = Queenstown)

**Suposición sobre los datos de entrada**: Al no poder obtener los nombres de las features del modelo, se dedujeron a partir de los valores del ejemplo en "notebooks/challenge-genai.ipynb". Se asume que para el campo `sex`: 0 = female y 1 = male.

### Respuesta de Predicción

La API retorna (en caso de una predicción exitosa):
- `score`: Probabilidad de supervivencia (0.0 - 1.0)
- `decision`: Decisión binaria (0=No sobrevivió, 1=Sobrevivió)
- `description`: Descripciín legible del resultado

## Instalación y Ejecución

### [Opción 1] Ejecución Local

```bash
# -- Paso 1 > Instalar dependencias con uv
uv sync

# -- Paso 2 > Ejecutar la aplicación
uv run uvicorn app.api.main:app --host 0.0.0.0 --port 8000 --reload
```

### [Opción 2] Ejecución con Docker

```bash
# -- Paso 1 > Construir imagen
docker build -t titanic-api .

# -- Paso 2 > Ejecutar contenedor
docker run --name titanic-container -p 8000:8000 titanic-api
```

## Uso de la API

### Verificar Estado
```bash
curl http://localhost:8000/health
```

### Realizar Predicción
```bash
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{
       "pclass": 3,
       "sex": 1,
       "age": 22.0,
       "sibsp": 1,
       "parch": 0,
       "fare": 7.25,
       "embarked": 0
     }'
```

**Respuesta esperada:**
```json
{
  "score": 0.123,
  "decision": 0,
  "description": "No sobrevivió"
}
```

## Documentación Automática

La API cuenta con documentación automática generada por FastAPI:

- **Swagger UI**: `http://localhost:8000/docs`

## Estructura del Proyecto

```
.
├── app
│   ├── api
│   │   └── main.py                  # Aplicación FastAPI principal
│   └── schemas
│       └── prediction_schemas.py    # Modelos de validación Pydantic
├── artifacts
│   └── modelo_titanic.joblib        # Modelo ML pre-entrenado
├── config.py                        # Configuración de variables constantes de la aplicación
├── Dockerfile                       # Configuración de contenedor
├── notebooks                        # Notebooks
│   ├── challenge-genai-original.ipynb
│   └── challenge-genai.ipynb
├── pyproject.toml                   # Dependencias del proyecto
├── README.md
└── uv.lock                          # Dependencias del proyecto
```

## Tecnologías Utilizadas

- **FastAPI**: Framework web moderno y rápido
- **Pydantic**: Validación de datos y serialización
- **Docker**: Containerización para despliegue
- **uv**: Gestión de dependencias de Python