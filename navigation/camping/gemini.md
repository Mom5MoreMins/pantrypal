---
layout: post 
title: Camping Home
search_exclude: true
permalink: /camping/gemini
menu: nav/camping.html
---

<style>
  /* Style for the chat button */
  .chat-button {
    position: fixed;
    bottom: 60px; /* Moved up slightly */
    right: 60px; /* Moved left slightly */
    width: 70px; /* Adjusted for a perfect square */
    height: 70px; /* Same as width */
    border-radius: 50%;
    background: #6B8E23; /* Earthy olive green */
    border: none;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    cursor: pointer;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .chat-button img {
    width: 50px; /* Smaller to fit square button */
    height: 50px;
  }

  /* Style for the chatbox container */
  .chatbox {
    position: fixed;
    bottom: 120px; /* Adjusted to align with moved chat button */
    right: 60px; /* Matches the chat button's new position */
    width: 300px;
    max-height: 400px;
    background: #fff;
    border: 1px solid #ddd;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    border-radius: 8px;
    display: none;
    flex-direction: column;
    overflow: hidden;
  }

  /* Header of the chatbox */
  .chatbox-header {
    background: #556B2F; /* Earthy olive green */
    color: white;
    padding: 10px;
    font-size: 16px;
    text-align: center;
  }

  /* Chatbox content area */
  .chatbox-content {
    flex-grow: 1;
    padding: 10px;
    overflow-y: auto;
    background-color: #f9f9f9;
  }

  /* Chatbox input area */
  .chatbox-input {
    border-top: 1px solid #ddd;
    display: flex;
  }

  .chatbox-input input {
    flex-grow: 1;
    padding: 10px;
    border: none;
    outline: none;
  }

  .chatbox-input button {
    background: #556B2F; /* Earthy olive green */
    color: white;
    border: none;
    padding: 10px 15px;
    cursor: pointer;
  }
.chat-message {
  padding: 8px 12px;
  margin: 5px 0;
  border-radius: 10px;
  max-width: 80%;
  word-wrap: break-word;
}
.chat-message-user {
  background-color: #d4f8d4; /* Light green */
  align-self: flex-start;
  color: #000; /* Set text color to black */
}
/* Chatbox content flexbox fix */
.chatbox-content div {
  display: flex;
  flex-direction: column;
  .chat-message-ai {
  background-color: #d2b48c; /* Light brown */
  align-self: flex-start;
  color: #000; /* Black text for contrast */
}
}
</style>

<body>
  <!-- Chat Button -->
  <button class="chat-button" onclick="toggleChatbox()">
    <img src="https://img.freepik.com/premium-vector/camping-lantern-icon-clipart-avatar-logotype-isolated-vector-illustration_955346-193.jpg" alt="Ranger Hat">
  </button>

  <!-- Chatbox -->
  <div class="chatbox" id="chatbox">
    <div class="chatbox-header">Chat with Us!</div>
    <div class="chatbox-content">
      <p>Hello! How can I assist you today?</p>
    </div>
    <div class="chatbox-input">
      <input type="text" placeholder="Type a message..." />
      <button>Send</button>
    </div>
  </div>
<script>
  // Function to toggle the chatbox visibility
  function toggleChatbox() {
    const chatbox = document.getElementById('chatbox');
    const content = document.querySelector('.chatbox-content'); // Chatbox content area
    if (chatbox.style.display === 'none' || chatbox.style.display === '') {
      chatbox.style.display = 'flex';
      showChatbotMessage(content);
    } else {
      chatbox.style.display = 'none';
    }
  }
  // Function to show the initial chatbot message
  function showChatbotMessage(content) {
    if (!content.parentElement.dataset.chatbotMessageShown) {
      const chatbotMessage = createMessage("AI: Hello, how can I help you?", 'chat-message-ai');
      content.appendChild(chatbotMessage);
      // Scroll to the latest message
      scrollToBottom(content);
      // Prevent multiple chatbot messages
      content.parentElement.dataset.chatbotMessageShown = true;
    }
  }
  // Function to send a user's message
  function sendMessage() {
    const input = document.querySelector('.chatbox-input input'); // Input field
    const content = document.querySelector('.chatbox-content'); // Chatbox content area
    const message = input.value.trim(); // Get input value and trim whitespace
    if (message) {
      const userMessage = createMessage(`You: ${message}`, 'chat-message-user');
      content.appendChild(userMessage);
      // Scroll to the latest message and clear the input field
      scrollToBottom(content);
      input.value = '';
    }
  }
  // Utility function to create a message element
  function createMessage(text, className) {
    const message = document.createElement('div');
    message.classList.add('chat-message', className);
    message.textContent = text;
    return message;
  }
  // Utility function to scroll to the bottom of the chatbox
  function scrollToBottom(content) {
    content.scrollTop = content.scrollHeight;
  }
  // Initialize event listeners
  document.addEventListener('DOMContentLoaded', () => {
    const input = document.querySelector('.chatbox-input input');
    const sendButton = document.querySelector('.chatbox-input button');
    if (input) {
      input.addEventListener('keypress', function (event) {
        if (event.key === 'Enter') {
          event.preventDefault();
          sendMessage();
        }
      });
    }
    if (sendButton) {
      sendButton.addEventListener('click', sendMessage);
    }
  });
</script>
