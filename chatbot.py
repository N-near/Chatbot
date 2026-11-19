"""Coordina la lógica de conversación sin depender de una interfaz gráfica."""

from intencion import deteccion_intenciones
from respuestas import responder


class Chatbot:
    """Mantiene el estado de una conversación durante la sesión actual."""

    def __init__(self, ultima_respuesta=None, usar_ia=False):
        # Permite restaurar el contexto de sesión que entrega una interfaz web.
        self.ultima_respuesta = ultima_respuesta
        # Turtle conserva el modo de reglas; Flask puede activar Gemini.
        self.usar_ia = usar_ia

    def procesar_mensaje(self, mensaje):
        """Recibe texto y devuelve la respuesta que debe mostrar la interfaz."""
        intenciones_detectadas = deteccion_intenciones(mensaje)

        # Repetir es una acción determinista: no hace falta consultar el modelo.
        if self.usar_ia and "repeticion" not in intenciones_detectadas:
            from servicio_ia import generar_respuesta

            respuesta = generar_respuesta(mensaje)
        else:
            respuesta = responder(intenciones_detectadas, self.ultima_respuesta)

        self.ultima_respuesta = respuesta
        return respuesta
