---
layout: post 
title: Camping Home
search_exclude: true
permalink: /camping/gemini
menu: nav/camping.html
---

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Chatbox</title>
  <style>
    /* Style for the chat button */
    .chat-button {
      position: fixed;
      bottom: 20px;
      right: 20px;
      width: 60px;
      height: 60px;
      border-radius: 50%;
      background: #556B2F; /* Olive green */
      border: none;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
      cursor: pointer;
      display: flex;
      justify-content: center;
      align-items: center;
    }

    .chat-button img {
      width: 40px;
      height: 40px;
    }

    /* Style for the chatbox container */
    .chatbox {
      position: fixed;
      bottom: 90px;
      right: 20px;
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
      background: #4CAF50;
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
      background: #4CAF50;
      color: white;
      border: none;
      padding: 10px 15px;
      cursor: pointer;
    }
  </style>
</head>
<body>
  <!-- Chat Button -->
  <button class="chat-button" onclick="toggleChatbox()">
    <img src="/images/rangerhat.jpg" alt="Ranger Hat">
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
      if (chatbox.style.display === 'none' || chatbox.style.display === '') {
        chatbox.style.display = 'flex';
      } else {
        chatbox.style.display = 'none';
      }
    }
  </script>
</body>
</html>
