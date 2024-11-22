---
layout: base
title: CipherDiscussion
search_exclude: true
permalink: share_and_care/cipherdiscussion
---
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cipher Discussion</title>
    <style>
        /* General Styling */
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: Arial, sans-serif;
            background-color: #121212;
            color: #f0f0f0;
            display: flex;
            flex-direction: column;
            align-items: center;
            min-height: 100vh;
            overflow-x: hidden;
        }
        header { 
            padding: 20px;
            width: 100%;
            max-width: 1000px;
            background-color: #1a1a1a;
            text-align: center;
            border-bottom: 5px solid #d91e18;
        }
        header h1 { 
            font-size: 2.8rem; 
            color: #d91e18; 
            text-shadow: 0px 2px 10px rgba(217, 30, 24, 0.7);
        }
        header p { 
            color: #b0b0b0; 
            font-size: 1rem; 
        }
        .main-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 30px;
            margin-top: 20px;
            width: 100%;
            max-width: 1000px;
        }
        .content-section {
            width: 100%;
            background-color: #1f1f1f;
            padding: 20px;
            border: 3px solid #d91e18;
        }
        .content-section h2 {
            color: #d91e18;
            margin-bottom: 10px;
            text-align: center;
            text-shadow: 0px 2px 8px rgba(217, 30, 24, 0.7);
        }
        .content-section form input, .content-section form textarea, .content-section form button {
            width: 100%;
            margin-top: 10px;
            padding: 10px;
            border: none;
            background-color: #2e2e2e;
            color: #f0f0f0;
        }
        .content-section form button {
            background-color: #d91e18;
            color: #1a1a1a;
            font-weight: bold;
            cursor: pointer;
        }
        .posts-wrapper {
            margin-bottom: 20px;
        }
        .chatroom-container .chat-area {
            background-color: #2e2e2e;
            padding: 15px;
            height: 200px;
            overflow-y: auto;
            margin-bottom: 10px;
        }
        .chatroom-container form input, .chatroom-container form button {
            padding: 10px;
            border: none;
            background-color: #2e2e2e;
            color: #f0f0f0;
            margin-top: 5px;
        }
        .chatroom-container form button {
            background-color: #d91e18;
            color: #1a1a1a;
            font-weight: bold;
            cursor: pointer;
        }
        .post {
            background-color: #2e2e2e;
            padding: 15px;
            margin-bottom: 10px;
        }
        .post-header {
            font-weight: bold;
            margin-bottom: 5px;
            color: #d91e18;
        }
    </style>
</head>
<body>

<header>
    <h1>Welcome to Cipher Discussion!</h1>
    <p>Share ideas, solve ciphers, and connect with others!</p>
</header>

<div class="main-container">
    <div class="content-section posts-wrapper" id="postsWrapper">
        <h2>Community Posts</h2>
        <!-- Posts will be dynamically loaded here -->
    </div>
    <div class="content-section">
        <h2>Add a New Post</h2>
        <form id="postForm">
            <input type="text" id="usernameInput" placeholder="Enter your username" required>
            <textarea id="postInput" placeholder="What's on your mind?" required></textarea>
            <button type="submit">Post</button>
        </form>
    </div>
</div>

<div class="content-section chatroom-container">
    <h2>Live Chatroom</h2>
    <div class="chat-area" id="messages">
        <!-- Messages will appear here -->
    </div>
    <form id="chat-form">
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
            const username = post.username || "Anonymous"; 
            const content = typeof post.content === 'string' ? post.content : JSON.stringify(post.content);

            return `
                <div class="post" data-post-id="${post.id}">
                    <div class="post-header">${username}</div>
                    <p>${content}</p>
                </div>`;
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

</body>
</html>
