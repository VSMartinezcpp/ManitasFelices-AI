import os

from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("No se encontró GEMINI_API_KEY.")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def preguntar_gemini(contexto, pregunta):

    prompt = f"""
Eres un asistente especializado en Lengua de Señas Mexicana.

Tu trabajo es responder únicamente utilizando el contexto proporcionado.

Si la respuesta no aparece en el contexto responde exactamente:

"No encontré esa información dentro del documento."

======================
CONTEXTO
======================

{contexto}

======================
PREGUNTA
======================

{pregunta}
"""

    try:

        respuesta = model.generate_content(prompt)

        return respuesta.text

    except Exception as e:

        if "429" in str(e):
            return (
                "⏳ El asistente ha recibido muchas solicitudes en un corto período de tiempo.\n\n"
                "Por favor, espera aproximadamente un minuto e inténtalo nuevamente."
            )

        return (
            "❌ Ocurrió un error al generar la respuesta.\n\n"
            f"Detalle técnico: {e}"
        )