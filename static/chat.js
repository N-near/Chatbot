const input = document.getElementById("chat-input");
const sendButton = document.getElementById("send-btn");
const messages = document.getElementById("chat-messages");

function addMessage(text, sender) {
    const message = document.createElement("div");
    message.className = `message ${sender}`;

    if (sender === "bot") {
        const avatar = document.createElement("img");
        avatar.src = messages.dataset.botAvatar;
        avatar.alt = "Cinnamobot";
        avatar.className = "avatar";
        message.appendChild(avatar);
    }

    const bubble = document.createElement("div");
    bubble.className = "bubble";
    // textContent muestra el mensaje como texto, no ejecuta HTML escrito por el usuario.
    bubble.textContent = text;
    message.appendChild(bubble);
    messages.appendChild(message);
    messages.scrollTop = messages.scrollHeight;
}

async function sendMessage() {
    const messageText = input.value.trim();
    if (!messageText || sendButton.disabled) return;

    addMessage(messageText, "user");
    input.value = "";
    sendButton.disabled = true;

    try {
        const response = await fetch("/api/mensaje", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ mensaje: messageText }),
        });
        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "No se pudo procesar el mensaje.");
        }

        addMessage(data.respuesta, "bot");
    } catch (error) {
        addMessage(`No pude conectar con el chatbot: ${error.message}`, "bot");
    } finally {
        sendButton.disabled = false;
        input.focus();
    }
}

sendButton.addEventListener("click", sendMessage);
input.addEventListener("keydown", (event) => {
    if (event.key === "Enter") sendMessage();
});
