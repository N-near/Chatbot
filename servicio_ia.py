"""Acceso al modelo Gemini, separado de la interfaz y de las reglas del bot."""

import os

from google import genai
from google.genai import types


MODELO_GEMINI = "gemini-3.8-flash"

INSTRUCCIONES_SISTEMA = """
Eres Cinnamobot, un chatbot amigable y educativo que conversa en español.
Responde de forma clara y adecuada a la pregunta; explica los conceptos paso a
paso cuando ayude a aprender. Si falta contexto, pregunta antes de asumir.
No inventes datos, fuentes ni citas. Si no sabes algo o requiere información
actual que no puedes consultar, dilo claramente en vez de presentarlo como un
hecho verificado. Mantén las respuestas breves y útiles.
""".strip()


class ConfiguracionGeminiError(Exception):
    """Indica que falta la clave de API necesaria para usar Gemini."""


class ServicioGeminiError(Exception):
    """Indica que Gemini no pudo generar una respuesta utilizable."""


def generar_respuesta(mensaje):
    """Envía un mensaje a Gemini y devuelve el texto generado."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ConfiguracionGeminiError(
            "Configura GEMINI_API_KEY en el entorno antes de usar el chat web."
        )

    try:
        with genai.Client(api_key=api_key) as cliente:
            respuesta = cliente.models.generate_content(
                model=MODELO_GEMINI,
                contents=mensaje,
                config=types.GenerateContentConfig(
                    system_instruction=INSTRUCCIONES_SISTEMA,
                    max_output_tokens=300,
                    temperature=0.3,
                ),
            )
    except Exception as error:
        raise ServicioGeminiError(
            "Gemini no pudo procesar el mensaje en este momento."
        ) from error

    texto = (respuesta.text or "").strip()
    if not texto:
        raise ServicioGeminiError("Gemini devolvió una respuesta vacía.")

    return texto
