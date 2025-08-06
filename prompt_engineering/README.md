# Challenge 2: Prompt Engineering con RAG

Este proyecto implementa diferentes técnicas de prompt engineering aplicadas a un sistema RAG básico para el dominio fintech.

> **Desarrollado por:** Bautista Peco

> **Proyecto:** Challenge GenAI - Prompt Engineering

> **Fecha:** Agosto 2025

## 📁 Estructura del proyecto

```
prompt_engineering/
├── notebooks/                          # Jupyter notebooks principales
│   ├── 01_rag_prompt_testing.ipynb     # Testing inicial y comparación
│   └── 02_prompt_evaluation.ipynb      # Evaluación de prompts
├── prompts/
│   └── prompts_fintech.py              # Definición de prompts
├── utils/
│   └── evaluation_dataset.py           # Dataset de evaluación
├── 01_mock_fintech_info.pdf           # Documento base inventado
└── pyproject.toml                      # Dependencias
```

## 🚀 Cómo ejecutar

### 1. Configurar entorno

```bash
cd prompt_engineering
uv sync
uv shell
```

### 2. Variables de entorno

Crear archivo `.env`:
```
OPENAI_API_KEY=api_key
```

### 3. Orden de ejecución

1. **Primero**: `notebooks/01_rag_prompt_testing.ipynb`
   - Implementación RAG básica
   - Testing exploratorio de 4 técnicas de prompt
   - Comparación visual de resultados
   - Genera archivos: `documents.pkl`

2. **Segundo**: `notebooks/02_prompt_evaluation.ipynb`
   - Evaluación con LLM-as-a-Judge
   - Evaluación cuantitativa con RAGAS
   - Análisis comparativo completo
   - Visualizaciones finales

## 🎯 Técnicas evaluadas

1. **Prompt básico**
2. **Con rol específico**
3. **One-shot learning**
4. **Chain-of-thought**

## ⚠️ Disclaimers importantes

### 📄 Documento inventado
El PDF `01_mock_fintech_info.pdf` es un documento completamente ficticio creado para este experimento. No representa información real de ninguna empresa fintech.

### 🔍 No es demostración de conocimientos RAG
Este proyecto se enfoca específicamente en **prompt engineering**. La implementación RAG es deliberadamente básica (FAISS + chunks simples) para mantener el foco en las técnicas de prompting.

### 🚫 HITL (Human-in-the-Loop) no incluido
No se implementó intervención humana dado que:
- No hay información sensible
- No se ejecutan acciones reales

En casos reales con información financiera o acciones críticas, HITL sería obligatorio.