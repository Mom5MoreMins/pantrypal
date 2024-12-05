---
layout: post 
title: Redwood National Park
search_exclude: true
permalink: /national_parks/redwood
menu: nav/national_parks.html
---
<style>
    .container {
        display: flex;
        justify-content: center;
        width: 100%;
        max-width: 1200px;
        padding: 20px;
        box-sizing: border-box;
    }
    .form-container {
        display: flex;
        flex-direction: column;
        max-width: 800px;
        width: 100%;
        background-color: #2C3E50;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        color: #ECF0F1;
    }
    .form-container label {
        margin-bottom: 5px;
    }
    .form-container input, .form-container textarea {
        margin-bottom: 10px;
        padding: 10px;
        border-radius: 5px;
        border: none;
        width: 100%;
    }
    .form-container button {
        padding: 10px;
        border-radius: 5px;
        border: none;
        background-color: #34495E;
        color: #ECF0F1;
        cursor: pointer;
    }
</style>

<div class="container">
    <div class="form-container">
        <h2>Add New Post to Redwood National Park</h2>
        <form id="postForm">
            <label for="title">Title:</label>
            <input type="text" id="title" name="title" required>
            <label for="comment">Comment:</label>
            <textarea id="comment" name="comment" required></textarea>
            <input type="hidden" id="group_id" name="group_id" value="national parks">
            <input type="hidden" id="channel_id" name="channel_id" value="17">
            <button type="submit">Add Post</button>
        </form>
    </div>
</div>

<div class="container">
    <div id="data" class="data">
        <div class="left-side">
            <p id="count"></p>
        </div>
        <div class="details" id="details"></div>
    </div>
</div>

<script type="module">
    import { pythonURI, fetchOptions } from '{{ site.baseurl }}/assets/js/api/config.js';

    /**
     * Handle form submission for adding a post
     */
    document.getElementById('postForm').addEventListener('submit', async function(event) {
        event.preventDefault();

        // Extract data from form
        const title = document.getElementById('title').value;
        const comment = document.getElementById('comment').value;
        const groupId = document.getElementById('group_id').value;
        const channelId = document.getElementById('channel_id').value;

        // Create API payload
        const postData = {
            title: title,
            comment: comment,
            group_id: groupId,
            channel_id: channelId
        };

        try {
            // Send POST request to backend
            const response = await fetch(`${pythonURI}/api/post`, {
                ...fetchOptions,
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(postData)
            });

            if (!response.ok) {
                throw new Error('Failed to add post: ' + response.statusText);
            }

            alert('Post added successfully!');
            document.getElementById('postForm').reset();
            fetchData(channelId);
        } catch (error) {
            console.error('Error adding post:', error);
            alert('Error adding post: ' + error.message);
        }
    });

    /**
     * Fetch and display posts
     */
    async function fetchData(channelId) {
        try {
            const response = await fetch(`${pythonURI}/api/posts/filter`, {
                ...fetchOptions,
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ channel_id: channelId })
            });
            if (!response.ok) {
                throw new Error('Failed to fetch posts: ' + response.statusText);
            }

            const postData = await response.json();
            document.getElementById('count').innerHTML = `<h2>Posts Count: ${postData.length || 0}</h2>`;
            const detailsDiv = document.getElementById('details');
            detailsDiv.innerHTML = '';

            postData.forEach(post => {
                const postElement = document.createElement('div');
                postElement.className = 'post-item';
                postElement.innerHTML = `
                    <h3>${post.title}</h3>
                    <p><strong>Comment:</strong> ${post.comment}</p>
                `;
                detailsDiv.appendChild(postElement);
            });
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    }

    // Fetch posts on page load
    fetchData(17);
</script>
