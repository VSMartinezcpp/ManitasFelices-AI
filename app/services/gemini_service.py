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

    # Si el recuperador no encontró información,
    # evitamos hacer una petición innecesaria a Gemini.
    if not contexto.strip():
        return "No encontré esa información dentro del documento."

    prompt = f"""
Eres un asistente especializado en Lengua de Señas Mexicana (LSM).

Responde únicamente utilizando la información del CONTEXTO.

Reglas:
- No inventes información.
- No uses conocimientos externos.
- Si el contexto no contiene la respuesta, responde exactamente:
"No encontré esa información dentro del documento."
- Responde de forma clara, breve y en español.

========================
CONTEXTO
========================

{contexto}

========================
PREGUNTA
========================

{pregunta}
"""

    respuesta = model.generate_content(prompt)

    return respuesta.text.strip()