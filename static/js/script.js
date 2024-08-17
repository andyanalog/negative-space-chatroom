document.addEventListener('DOMContentLoaded', () => {
    const chatContainer = document.getElementById('chat-container');
    const messageInput = document.getElementById('message');
    const sendButton = document.getElementById('send-button');

    sendButton.addEventListener('click', sendMessage);
    messageInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

    async function sendMessage() {
        const message = messageInput.value;
        if (message.trim() === '') return;

        // Agregar mensaje del usuario al chat
        chatContainer.innerHTML += `<div class="message user-message">You: ${message}</div>`;
        messageInput.value = '';

        // Enviar mensaje al servidor
        const response = await fetch('/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message })
        });
        const data = await response.json();

        // Agregar respuesta del bot al chat
        chatContainer.innerHTML += `<div class="message bot-message">${data.response}</div>`;
        chatContainer.scrollTop = chatContainer.scrollHeight;
    }
});
