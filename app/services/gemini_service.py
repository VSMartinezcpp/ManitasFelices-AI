import os

from dotenv import load_dotenv

import google.generativeai as genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("No se encontró GEMINI_API_KEY en el archivo .env")

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

    respuesta = model.generate_content(prompt)

    return respuesta.text