import streamlit as st

from app.services.gemini_service import preguntar_gemini
from app.services.retriever_service import buscar_contexto
from app.services.vector_service import cargar_vectorstore


st.set_page_config(
    page_title="Manitas Felices AI",
    page_icon="🖐️",
    layout="wide"
)

#  Cargar Base Vectorial 

try:
    cargar_vectorstore()
except Exception as e:
    st.error(f"No se pudo cargar la base vectorial.\n\n{e}")
    st.stop()

# Sidebar 

st.sidebar.title("🖐️ Manitas Felices AI")

pagina = st.sidebar.radio(
    "Menú",
    [
        "🏠 Inicio",
        "🤖 Asistente IA",
        "ℹ️ Acerca del proyecto"
    ]
)

# Inicio 

if pagina == "🏠 Inicio":

    st.title("🖐️ Manitas Felices AI")

    st.subheader("Asistente Inteligente basado en IA")

    st.write("""
Bienvenido a **Manitas Felices AI**.

Este proyecto utiliza la técnica **Retrieval-Augmented Generation (RAG)** para responder preguntas sobre la **Lengua de Señas Mexicana (LSM)** utilizando una base de conocimiento en formato PDF.

### ¿Qué puedes hacer?

- Consultar información sobre Lengua de Señas Mexicana.
- Obtener respuestas fundamentadas en la base de conocimiento.
- Explorar una aplicación práctica de Inteligencia Artificial orientada a la accesibilidad.

Selecciona **Asistente IA** en el menú para comenzar.
""")

# Asistente 

elif pagina == "🤖 Asistente IA":

    st.title("🤖 Asistente Inteligente")

    pregunta = st.text_input(
        "Escribe tu pregunta",
        placeholder="Ejemplo: ¿Qué es la Lengua de Señas Mexicana?"
    )

    if st.button("Preguntar"):

        if pregunta.strip():

            with st.spinner("Analizando la base de conocimiento..."):

                try:

                    contexto = buscar_contexto(pregunta)

                    respuesta = preguntar_gemini(
                        contexto,
                        pregunta
                    )

                    st.success(respuesta)

                except Exception as e:

                    st.error(f"Error: {e}")

        else:

            st.warning("Por favor, escribe una pregunta.")

# Acerca 

elif pagina == "ℹ️ Acerca del proyecto":

    st.title("ℹ️ Acerca del proyecto")

    st.write("""
**Manitas Felices AI** es un asistente basado en Inteligencia Artificial que utiliza un sistema **RAG (Retrieval-Augmented Generation)** para responder preguntas utilizando una base de conocimiento en formato PDF.

### Desarrollador

**Valentin Martinez**

### Tecnologías utilizadas

- Python
- Streamlit
- LangChain
- ChromaDB
- Sentence Transformers
- Google Gemini
- Oracle Cloud Infrastructure (OCI)

### Objetivo

Demostrar cómo un modelo de Inteligencia Artificial puede consultar una base de conocimiento específica para generar respuestas precisas y contextualizadas.
""")