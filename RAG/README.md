## Introducción

En este repositorio presento la **arquitectura RAG** que diseñé para el tercer challenge de Ueno Bank, usando servicios de AWS y un motor de orquestación basado en LangGraph. Mi objetivo es mostrar:

1. Cómo creo y mantengo la Knowledge Base.  
2. El flujo de ingesta y actualización de documentos.  
3. El esquema general de la aquitectura RAG.
4. Un *deep-dive* de la etapa de retrieval.  
5. La capa de exposición de la aplicación vía API.  
6. El flujo en vivo desde la petición del empleado hasta la respuesta final.

Más adelante, en la sección de **“Mejoras propuestas”**, detallo cómo podríamos llevar esto hacia un diseño más “agentic” con MCPs.

---

## Etapa 1: Knowledge Base Creation  (Anexo)

> **Nota:** La creación inicial de la KB está documentada como anexo para no sobrecargar el flujo principal.

En dicho anexo explico cómo diseñé la KB en Bedrock:
- Conecto a S3/RDS como datasource.
- Selecciono **Titan Text Embeddings v2** (1024‑dim, soporte multilingüe, optimizado para RAG, buena precisión y más barato que la v1).
- Configuro chunking y OpenSearch Serverless como backend vectorial.

![Diagrama - Creación Knowledge Base](resources/1-creacion-KB.png)

---

## Etapa 2: Ingesta y Actualización

**Propósito**: mantener la KB sincronizada sin intervención manual.


- **Amazon S3 / RDS**: Almacenan PDFs y tablas estructuradas que disparan eventos.
- **Amazon SQS**: Recibe los eventos de S3; actúa como búfer, permite *batch N* mensajes por lote y ofrece reintentos automáticos.
- **DLQ (Dead-Letter Queue)**: Cola asociada a SQS donde terminan los mensajes que Lambda no pudo procesar después de los reintentos; facilita auditoría y reprocesos.
- **AWS Lambda (Container Image)**: Se activa por lotes desde SQS, extrae el contenido, llama a **Amazon Bedrock** para generar embeddings y envía los vectores.
- **OpenSearch Service (VectorStore)**: Indexa los embeddings y metadatos para consultas semánticas posteriores.

![Diagrama - Ingresa + Actualización](resources/2-ingesta-actualizacion.png)

---

## Etapa 3: Arquitectura RAG

**Propósito**: procesar la pregunta del usuario con posibilidad de omitier retrieval si no es necesario, o enriquecerla con contexto.

![Diagrama - Arquitectura RAG](resources/3-arquitectura.png)

- **Router LLM (Claude 3 Haiku)**: decide si la consulta requiere retrieval o se atiende con LLM ligero. Elegí Claude 3.5 Haiku porque es rápido, barato y suficiente para tareas de clasificación simples.
- **Query Re‑Writer (Claude 3 Haiku)**: limpia y normaliza la pregunta para mejorar la recuperación; nuevamente seleccioné Claude 3.5 Haiku debido al objetivo de este nodo. Necesito:
    - (1) comprensión semántica suficiente para detectar intención y extraer el core de la query del usuario
    - (2) baja latencia para no penalizar el tiempo total de respuesta
    - (3) coste muy bajo porque el router lo va a invocar en la mayoría de las interacciones.
- **Retriever + Re‑Ranker**: Bedrock KB + OpenSearch traen top‑25 <i>(traigo documentos por demás para ejecutar después un re-ranker y seleccionar menos)</i> y el re‑ranker de Bedrock selecciona top‑5. Es decir utilizo Bedrock para Retrieve y Rerank.
- **LLM Final (Claude 3 Sonnet)**: genera respuesta final combinando el contexto recuperado; elegí Sonnet por su buen equilibrio entre razonamiento (≈87 % MMLU - [Fuente Anthropic](https://www.anthropic.com/news/claude-4)) y coste moderado.
- **Light LLM**: si no fuera necesario tener que pasar por la etapa de retrieve, elijo nuevamnete un modelo ligero que responde directamente consultas sencillas.


Esta arquitectura va a estar orquestada mediante LangGraph. Una representación de la misma podría ser la siguiente:


![Diagrama - LangGraph](resources/langgraph.png)

---

## Etapa 4: Deep‑Dive en el retrieve 

**Propósito**: ilustrar cómo funciona internamente la etapa del retrieve

![Diagrama - Etapa Retrieve](resources/4-retrieve-stage.png)


1. Recordar que el input de este nodo es el prompt optimizado.
2. Se calcula embedding con **Titan Text Embeddings v2**
3. Se ejecuta búsqueda KNN sobre **OpenSearch Serverless**, obteniendo top‑25.
4. Se aplica re-ranking con Bedrock y se extraen top‑5.
5. Estos documentos pasan al nodo final de generación.

---

## Etapa 5: Exposición de la Aplicación

**Propósito**: proveer un único endpoint seguro para consultas internas.

![Diagrama - Etapa Flujo en vivo](resources/5-exposicion.png)


- Empaqueté la aplicación como un **Docker Container** que incluye:
  - definición del grafo LangGraph (nodos y estado).
  - runtime de LangGraph para ejecutar el pipeline.
- Contenedor desplegado en **Amazon ECR**.
- **API Gateway (HTTP API)** expone endpoint `POST /query` por ejemplo con autenticación JWT.
- **Lambda (Container Image)** invocado desde API Gateway ejecuta el container, dispara el flujo, llama a Bedrock y devuelve la respuesta.



> **Nota**: En este paso de la exposición de la aplicación, tenía dos opciones:
> -  ***Lambda con Container Image*** (opción elegida)
> -  ***App Runner*** (podría ser iteración en el futuro). Las ventajas de App Runner es que no tengo cold-start para evitar latencia pero no escala a cero por lo que concurriría en costos a pesar de no estar utilizando el servicio. Dado que el usuario final de esta aplicación van a ser empelados, decidí optar por perder un poco de latencia (por lo menos en una primera etapa) pero no estar concurriendo en costos constantemente. Si fuese el caso donde el usuario final sean usuarios propiamente dichos de Ueno Bank, entonces la latencia es menos negociable y sería un mejor camino elegir App Runner.

---


## Etapa 6: Flujo en vivo

**Propósito**: mostrar el recorrido completo desde el usuario hasta la respuesta.

![Diagrama - Etapa Flujo en vivo](resources/6-flujo-en-vivo.png)

- Empleado hace POST /query desde front, con JWT.
- API Gateway valida autenticación e invoca Lambda.
- Lambda arranca el contenedor y el LangGraph Runtime:
    - router → rewriter → retrieve → re-ranker → LLM final o ligera si no hay retrieval.


---


## 7. Propuesta de Métricas de Evaluación del Retrieve

**Propósito**: medir objetivamente la calidad del sistema de recuperación.

> En el caso de tener alguna especie de *ground-truth* con pares de preguntas-documentos, entonces podría utilizar las siguientes métricas para evaluar la performance del **retriever** :

-  **Precision@K**: proporción de documentos relevantes entre los top-K.
- **Recall@K**: cobertura de los documentos relevantes totales.
- **MRR (Mean Reciprocal Rank)**: promedio del recíproco del ranking del primer documento relevante.
- **MAP@K (Mean Average Precision)**: precisión promedio acumulada hasta K documentos por consulta.


---

## 8. Roadmap de Mejoras

- Incorporar flujo **agentic** con múltiples agentes coordinados por LangGraph.
- Implementar **Bedrock Guardrails** para enforcing de grounding y seguridad.
- Exponer modo **streaming** con tokens incrementales desde el LLM final.