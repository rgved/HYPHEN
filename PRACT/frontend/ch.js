const input = document.getElementById("user-input");
const chatBox = document.getElementById("chat-box");

// Send message on Enter key
input.addEventListener("keydown", function (event) {
  if (event.key === "Enter") {
    event.preventDefault();
    sendMessage();
  }
});

async function sendMessage() {
  const text = input.value.trim();
  if (!text) return;

  // Add user message
  addMessage(text, "user");
  input.value = "";

  // Show typing indicator
  const typingMsg = addMessage("Typing...", "gemini");

  try {
    const response = await fetch("http://localhost:5000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        message: text,
        context: "ML recommended: SIP, Risk: Medium, Horizon: Long"
      })
    });

    const data = await response.json();

    // Remove typing indicator
    chatBox.removeChild(typingMsg);

    // Add Gemini response
    addMessage(data.reply, "gemini");

  } catch (error) {
    chatBox.removeChild(typingMsg);
    addMessage(
      "⚠️ Unable to connect to Gemini backend. Please try again.",
      "gemini"
    );
  }
}

function addMessage(text, sender) {
  const msg = document.createElement("div");
  msg.className = `message ${sender}`;
  msg.textContent = text;
  chatBox.appendChild(msg);
  chatBox.scrollTop = chatBox.scrollHeight;
  return msg; // IMPORTANT: allows removal of typing indicator
}
