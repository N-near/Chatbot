import os

from flask import Flask, jsonify, render_template, request, session
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from chatbot import Chatbot
from servicio_ia import ConfiguracionGeminiError, ServicioGeminiError


app = Flask(__name__)
# En despliegues, configura FLASK_SECRET_KEY con un valor privado y aleatorio.
app.secret_key = os.environ["FLASK_SECRET_KEY"]
app.config["MAX_CONTENT_LENGTH"] = 8 * 1024

# El límite por IP evita llamadas accidentales repetidas a la API.
limiter = Limiter(
    get_remote_address,
    app=app,
    storage_uri=os.environ.get("RATELIMIT_STORAGE_URI", "memory://"),
)


@app.get("/")
def pagina_principal():
    return render_template("main.html")


@app.errorhandler(413)
def solicitud_demasiado_grande(_error):
    return jsonify({"error": "El mensaje enviado es demasiado grande."}), 413


@app.errorhandler(429)
def demasiadas_solicitudes(_error):
    return jsonify({"error": "Espera un momento antes de enviar otro mensaje."}), 429


@app.post("/api/mensaje")
@limiter.limit("10 per minute")
def procesar_mensaje():
    datos = request.get_json(silent=True)
    if not isinstance(datos, dict) or not isinstance(datos.get("mensaje"), str):
        return jsonify({"error": "Envía un campo 'mensaje' de tipo texto."}), 400

    mensaje = datos["mensaje"].strip()
    if not mensaje:
        return jsonify({"error": "El mensaje no puede estar vacío."}), 400
    if len(mensaje) > 1000:
        return jsonify({"error": "El mensaje no puede superar 1000 caracteres."}), 413

    # La sesión del navegador conserva la última respuesta para la intención repetir.
    chatbot = Chatbot(
        ultima_respuesta=session.get("ultima_respuesta"),
        usar_ia=True,
    )
    try:
        respuesta = chatbot.procesar_mensaje(mensaje)
    except ConfiguracionGeminiError as error:
        return jsonify({"error": str(error)}), 503
    except ServicioGeminiError:
        app.logger.exception("No se pudo obtener una respuesta de Gemini.")
        return jsonify({
            "error": "El servicio de IA no está disponible ahora. Intenta de nuevo."
        }), 502

    session["ultima_respuesta"] = chatbot.ultima_respuesta
    return jsonify({"respuesta": respuesta})


if __name__ == "__main__":
    app.run(debug=False)
