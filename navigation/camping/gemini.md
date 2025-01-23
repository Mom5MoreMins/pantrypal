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
    bottom: 60px;
    right: 60px;
    width: 70px;
    height: 70px;
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
    width: 50px;
    height: 50px;
  }

  /* Style for the chatbox container */
  .chatbox {
    position: fixed;
    bottom: 120px;
    right: 60px;
    width: 600px;
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
    background: #556B2F;
    color: white;
    border: none;
    padding: 10px 15px;
    cursor: pointer;
  }

  /* Chatbox content area */
  .chatbox-content {
    flex-grow: 1;
    padding: 10px;
    overflow-y: auto; /* Allows scrolling if content exceeds the container height */
    background-color: #f9f9f9;
    display: flex; /* Enable flexbox layout */
    flex-direction: column; /* Stack messages vertically */
    gap: 8px; /* Add spacing between messages */
  }

  /* Shared message bubble style */
  .chat-message {
    padding: 10px 15px;
    margin: 0; /* Remove external margin since spacing is controlled by gap */
    border-radius: 18px;
    word-wrap: break-word;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.15);
    display: inline-block; /* Make the bubble only as wide as its content */
  }

  /* AI's message bubble (on the left now) */
  .chat-message-ai {
    background-color: #f4a460; /* Sandy brown */
    color: #000; /* Black text */
    align-self: flex-start; /* Align to the left */
    text-align: left; /* Align text inside to the left */
    max-width: 75%; /* Maximum width for the bubble */
    border-bottom-left-radius: 0; /* Flat bottom-left corner */
  }

  /* User's message bubble (on the right now) */
  .chat-message-user {
    background-color: #d4f8d4; /* Light green */
    color: #000; /* Black text */
    align-self: flex-end; /* Align to the right */
    text-align: left; /* Align text inside to the left */
    max-width: 75%; /* Maximum width for the bubble */
    border-bottom-right-radius: 0; /* Flat bottom-right corner */
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
    <div class="chatbox-content"></div>
    <div class="chatbox-input">
      <input type="text" placeholder="Type a message..." />
      <button>Send</button>
    </div>
  </div>
<script>
    // Chatbot message visibility flag
    let chatbotMessageShown = false;
    // Function to toggle the chatbox visibility
    function toggleChatbox() {
        const chatbox = document.getElementById('chatbox');
        const content = document.querySelector('.chatbox-content');
        if (chatbox.style.display === 'none' || chatbox.style.display === '') {
            chatbox.style.display = 'flex';
            showChatbotMessage(content);
        } else {
            chatbox.style.display = 'none';
        }
    }
    // Function to show the initial chatbot message
    function showChatbotMessage(content) {
        if (!chatbotMessageShown) {
            const chatbotMessage = createMessage("RangerAI: Hello, how can I help you?", 'chat-message-ai');
            content.appendChild(chatbotMessage);
            scrollToBottom(content);
            chatbotMessageShown = true;
        }
    }
    // Function to create a message element
    function createMessage(text, className) {
        const message = document.createElement('div');
        message.classList.add('chat-message', className);
        message.textContent = text;
        return message;
    }
    // Function to scroll to the bottom of the chatbox
    function scrollToBottom(content) {
        content.scrollTop = content.scrollHeight;
    }
    // Function to fetch Gemini API response
    async function fetchGeminiResponse(userInput) {
        try {
            const response = await fetch(`http://127.0.0.1:8887/api/chatbot`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ user_input: userInput })
            });
            if (!response.ok) {
                throw new Error('Failed to fetch Gemini response: ' + response.statusText);
            }
            const data = await response.json();
            return data.model_response;
        } catch (error) {
            console.error('Error fetching Gemini response:', error);
            return null;
        }
    }
    // Function to send a message
    function sendMessage() {
        const input = document.querySelector('.chatbox-input input');
        const content = document.querySelector('.chatbox-content');
        const message = input.value.trim();
        if (message) {
            // Display user message
            const userMessage = createMessage(`You: ${message}`, 'chat-message-user');
            content.appendChild(userMessage);
            scrollToBottom(content);
            input.value = '';
            // Fetch AI response
            fetchGeminiResponse(message).then((response) => {
                const aiMessage = createMessage(
                    response ? `RangerAI: ${response}` : 'Error: No response received.',
                    'chat-message-ai'
                );
                content.appendChild(aiMessage);
                scrollToBottom(content);
            }).catch(() => {
                const errorMessage = createMessage('Error: Failed to connect to the AI service.', 'chat-message-ai');
                content.appendChild(errorMessage);
                scrollToBottom(content);
            });
        } else {
            alert('Please enter a message before sending.');
        }
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
