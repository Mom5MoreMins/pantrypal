---
layout: post 
title: Camping Chatroom
search_exclude: true
permalink: /camping/page2
---
<style>
    body {
        font-family: Arial, sans-serif;
        background-color: #181818;
        color: #e0e0e0;
        display: flex;
        flex-direction: column;
        align-items: center;
        min-height: 100vh;
        overflow-x: hidden;
    }
    .top-sections-wrapper {
        display: flex;
        justify-content: space-between;
        width: 100%;
        max-width: 1000px;
        gap: 20px;
        margin-top: 20px;
    }
    .chatroom-container {
        background-color: #2b2b2b;
        padding: 20px;
        border-radius: 8px;
        border: 2px solid #6b705c;
        flex: 1;
    }
    .chatroom-container h2 {
        color: #6b705c;
        text-align: center;
        margin-bottom: 10px;
    }
    #username, #message {
        width: 100%;
        padding: 10px;
        margin: 5px 0;
        border-radius: 4px;
        border: 1px solid #333;
        background-color: #333;
        color: #e0e0e0;
    }
    .message-form button {
        width: 100%;
        padding: 10px;
        border: none;
        border-radius: 4px;
        background-color: #6b705c;
        color: #1b1b1b;
        font-weight: bold;
        cursor: pointer;
        text-shadow: 0px 2px 8px rgba(255, 209, 102, 0.6);
    }
</style>

<div class="chatroom-container">
    <h2>All Things Camping!</h2>
    <div class="chat-area" id="messages">
        <!-- Messages will appear here -->
    </div>
    <form class="message-form" id="chat-form">
        <input type="text" id="username" placeholder="Your Name" required>
        <input type="text" id="message" placeholder="Type a message..." maxlength="200" required>
        <button type="submit">Send</button>
    </form>
</div>

<script type="module">
    import { pythonURI, fetchOptions } from '../assets/js/api/config.js';

    async function fetchPosts() {
        try {
            const response = await fetch(`${pythonURI}/api/posts`, fetchOptions);
            if (!response.ok) {
                throw new Error("Failed to fetch posts from the backend.");
            }
            const posts = await response.json();
            renderPosts(posts);
        } catch (error) {
            console.error("Error fetching posts:", error);
        }
    }

    function renderPosts(posts) {
        document.getElementById('postsWrapper').innerHTML = posts.map(post => {
            const username = post.username || "Anonymous"; // Default to "Anonymous" if undefined
            const content = typeof post.content === 'string' ? post.content : JSON.stringify(post.content); // Display content as JSON if it's an object

        }).join('');
    }

    async function addPost(event) {
        event.preventDefault();
        const username = document.getElementById('usernameInput').value || "Anonymous";
        const content = document.getElementById('postInput').value;
        const postData = { username, content };

        try {
            const response = await fetch(`${pythonURI}/api/posts`, {
                ...fetchOptions,
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(postData)
            });
            if (!response.ok) {
                throw new Error("Failed to add post to the backend.");
            }
            document.getElementById('postForm').reset();
            fetchPosts(); // Refresh posts after adding a new one
        } catch (error) {
            console.error("Error adding post:", error);
        }
    }

    document.addEventListener('DOMContentLoaded', () => {
        fetchPosts();
        
        document.getElementById('postForm').addEventListener('submit', addPost);

        document.getElementById('chat-form').addEventListener('submit', function(event) {
            event.preventDefault();
            const username = document.getElementById('username').value || "Anonymous";
            const message = document.getElementById('message').value;
            const timestamp = new Date().toLocaleTimeString();
            const messageHtml = `<p><span class="username">${username}</span>: ${message} <span class="timestamp">[${timestamp}]</span></p>`;
            document.getElementById("messages").innerHTML += messageHtml;
            event.target.reset();
        });
    });

</script>

