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
  position: relative;
}

.chatbox-input input {
  flex-grow: 1;
  padding: 10px 80px 10px 10px; /* Adjusted padding to make space for the green text */
  border: none;
  outline: none;
  font-size: 16px;
}

.chatbox-input button {
  background: #556B2F;
  color: white;
  border: none;
  padding: 10px 15px;
  cursor: pointer;
}

/* Green text style */
.green-text {
  position: absolute;
  right: 100px; /* Adjust this value as per your layout */
  top: 50%;
  transform: translateY(-50%);
  color: #6B8E23; /* Olive green */
  font-size: 14px;
  font-weight: bold;
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

/* User's message bubble (aligned to the far right) */
.chat-message-user {
  background-color: #d4f8d4; /* Light green */
  color: #000; /* Black text */
  align-self: flex-end; /* Align to the right */
  text-align: right; /* Align text inside to the right */
  max-width: 75%; /* Maximum width for the bubble */
  border-bottom-right-radius: 0; /* Flat bottom-right corner */
  margin-left: auto; /* Push the message to the rightmost side */
}

/* Hide buttons by default */
.update-button,
.delete-button {
  display: none;
  position: absolute;
  top: 100%; /* Positions the buttons slightly below the message */
  padding: 3px 8px; /* Smaller padding for a smaller button size */
  font-size: 10px; /* Smaller font size */
  border-radius: 8px; /* Smaller radius for a compact look */
  border: none;
  cursor: pointer;
  transform: translateY(-10px); /* Slight overlap below the message */
}

/* Show buttons when hovering over the message */
.chat-message-container {
  position: relative;
}

.chat-message-container:hover .update-button,
.chat-message-container:hover .delete-button {
  display: inline-block;
}

/* Position update and delete buttons below the messages */
.update-button {
  right: 60px;
  background-color: rgba(255, 255, 255, 0.7);
}

.delete-button {
  right: 10px;
  background-color: rgba(255, 0, 0, 0.7);
  color: white;
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
    // 📍 Define the API base URL here to keep it dynamic
    const API_BASE_URL = "http://127.0.0.1:8102/api"; // Update as needed

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

    // Function to create a message element with update and delete buttons
    function createMessage(text, className, messageId) {
        const messageContainer = document.createElement('div');
        messageContainer.classList.add('chat-message-container');

        const message = document.createElement('div');
        message.classList.add('chat-message', className);
        message.textContent = text;
        message.dataset.messageId = messageId;

        const updateButton = document.createElement('button');
        updateButton.textContent = 'Update';
        updateButton.classList.add('update-button');
        updateButton.addEventListener('click', () => updateMessage(messageId));

        const deleteButton = document.createElement('button');
        deleteButton.textContent = 'Delete';
        deleteButton.classList.add('delete-button');
        deleteButton.addEventListener('click', () => deleteMessage(messageId));

        messageContainer.appendChild(message);
        messageContainer.appendChild(updateButton);
        messageContainer.appendChild(deleteButton);

        return messageContainer;
    }

    // Function to scroll to the bottom of the chatbox
    function scrollToBottom(content) {
        content.scrollTop = content.scrollHeight;
    }

    // Function to send message
    async function sendMessage() {
        const input = document.querySelector('.chatbox-input input');
        const content = document.querySelector('.chatbox-content');
        const message = input.value.trim();

        if (message) {
            input.value = '';

            try {
                // Send message to backend using dynamic API base URL
                const response = await fetch(`${API_BASE_URL}/chatbot`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ user_input: message }),
                });

                if (!response.ok) {
                    throw new Error('Failed to send message: ' + response.statusText);
                }

                const data = await response.json();
                console.log('Backend Response:', data); // Debugging

                // Use the backend-provided ID to create the user message
                const userMessage = createMessage(`You: ${message}`, 'chat-message-user', data.user_message_id);
                content.appendChild(userMessage);

                // Display the AI response with the correct ID
                const aiMessage = createMessage(`RangerAI: ${data.model_response}`, 'chat-message-ai', data.ai_message_id);
                content.appendChild(aiMessage);

                scrollToBottom(content);
            } catch (error) {
                console.error('Error sending message:', error);
            }
        }
    }

    // Function to update a message
    async function updateMessage(messageId) {
        const newText = prompt('Enter the updated message:');
        if (newText) {
            try {
                const response = await fetch(`${API_BASE_URL}/chatbot/update/${messageId}`, {
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ new_text: newText }),
                });

                if (!response.ok) {
                    throw new Error('Failed to update message: ' + response.statusText);
                }

                const messageElement = document.querySelector(`[data-message-id="${messageId}"]`);
                if (messageElement) {
                    messageElement.textContent = newText;
                }
            } catch (error) {
                console.error('Error updating message:', error);
            }
        }
    }

    // Function to delete a message
    async function deleteMessage(messageId) {
        try {
            const response = await fetch(`${API_BASE_URL}/chatbot/delete/${messageId}`, {
                method: 'DELETE',
            });

            if (!response.ok) {
                throw new Error('Failed to delete message: ' + response.statusText);
            }

            const messageElement = document.querySelector(`[data-message-id="${messageId}"]`);
            if (messageElement) {
                messageElement.remove();
            }
        } catch (error) {
            console.error('Error deleting message:', error);
        }
    }

    // Event listener for the send button
    document.querySelector('.chatbox-input button').addEventListener('click', sendMessage);

    // Event listener for the Enter key
    document.querySelector('.chatbox-input input').addEventListener('keypress', function (e) {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });
</script>
</body>
