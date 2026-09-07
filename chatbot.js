async function sendMessage() {
    let userInput = document.getElementById("user-input").value;
    let chatBox = document.getElementById("chat-box");

    // Show user message in chat
    chatBox.innerHTML += `<p><strong>You:</strong> ${userInput}</p> `;

    // Send message to Flask backend
    let response = await fetch("http://127.0.0.1:5000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userInput })
    });

    let data = await response.json();
    
    // Show bot response in chat
    chatBox.innerHTML += `<p><strong>Chatbot:</strong> ${data.response}</p>`;

    // Clear input field
    document.getElementById("user-input").value = "";
}
