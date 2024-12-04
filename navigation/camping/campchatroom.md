---
layout: post 
title: Camping Chatroom
search_exclude: true
permalink: /camping/page2
---
<style>
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f9;
}
.chatroom {
    max-width: 600px;
    margin: 20px auto;
    padding: 10px;
    border: 1px solid #ccc;
    background: #414833;
    border-radius: 5px;
}
.messages {
    height: 300px;
    overflow-y: auto;
    margin-bottom: 10px;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
    background: #a5a58d;
}
.message {
    margin-bottom: 15px;
}
.message strong {
    display: block;
    color: #333;
    margin-bottom: 5px;
}
.message p {
    margin: 0;
    padding: 5px;
    background: #f0f0f0;
    border-radius: 5px;
    color: #555;
}
.chat-form {
    display: flex;
    gap: 10px;
}
.chat-form input[type="text"] {
    flex: 1;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
}
.chat-form button {
    padding: 10px;
    border: none;
    border-radius: 5px;
    background: #007bff;
    color: #fff;
    cursor: pointer;
}
.chat-form button:hover {
    background: #0056b3;
}
</style>


<div class="chatroom">
    <h2>All things camping!</h2>
    <div class="messages" id="messages"></div>
    <form id="chat-form" class="chat-form">
      <input type="text" id="message-input" placeholder="Type your message..." required />
      <button type="submit">Send</button>
    </form>
</div>

  <script>
    const apiUrl = "https://your-backend-url.com/api"; // replace w backend API URL
    const username = "LoggedInUsername"; // replace w actual username from  login system

    // fetch and display messages
    async function loadMessages() {
      try {
        const response = await fetch(`${apiUrl}/messages`);
        const messages = await response.json();
        const messagesContainer = document.getElementById("messages");
        messagesContainer.innerHTML = ""; // clears existing messages
        messages.forEach(msg => {
          const messageElement = document.createElement("div");
          messageElement.classList.add("message");
          messageElement.innerHTML = `<strong>${msg.username}</strong><p>${msg.text}</p>`;
          messagesContainer.appendChild(messageElement);
        });
        messagesContainer.scrollTop = messagesContainer.scrollHeight; // autoscroll
      } catch (error) {
        console.error("Error loading messages:", error);
      }
    }

    // message submission
    document.getElementById("chat-form").addEventListener("submit", async (e) => {
      e.preventDefault();
      const messageInput = document.getElementById("message-input");
      const messageText = messageInput.value.trim();
      if (!messageText) return;

      try {
        const response = await fetch(`${apiUrl}/messages`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ username, text: messageText })
        });
        if (response.ok) {
          messageInput.value = ""; // clear input
          loadMessages(); // refresh
        } else {
          console.error("Failed to send message:", response.statusText);
        }
      } catch (error) {
        console.error("Error sending message:", error);
      }
    });

    // load messages 
    setInterval(loadMessages, 3000); // Refreshes messages every 3 sec

    // initial load
    loadMessages();
  </script>
