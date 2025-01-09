---
layout: post 
title: Camping Posts
search_exclude: true
permalink: /camping/page2
menu: nav/camping.html
---

<style>
    .container {
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;
        max-width: 1200px;
        padding: 20px;
        box-sizing: border-box;
    }

    .form-container, .post-item {
        display: flex;
        flex-direction: column;
        width: 100%; 
        max-width: 800px; 
        background-color: #a4ac86;
        box-shadow: 0 4px 8px 0 #e9edc9, 0 6px 20px 0 #e9edc9;
        padding: 20px;
        border-radius: 10px;
        border: 3px solid #3a5a40;
        color: #414833;
        margin-bottom: 20px;
        box-sizing: border-box; 
    }

    .post-item h3, .post-item p {
        margin: 0 0 10px;
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
        background-color: #a4ac86;
        color: #414833;
        cursor: pointer;
    }
    .details {
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;
        max-width: 1200px;
        padding: 20px;
        box-sizing: border-box;
    }

    .post-item h3 {
        margin: 0 0 10px;
    }
    .post-item p {
        margin: 5px 0;
    }

</style>

# Choose a biome to post about!
<!-- try new post function -->


<div class="container">
    <div class="form-container">
  <h2>Create a Post</h2>
  <form id="postForm">
    <label for="title">Title:</label>
    <input type="text" id="title" name="title" required>
    <p></p>
    <label for="comment">Comment:</label>
    <textarea id="comment" name="comment" required></textarea>
    <!-- Dropdowns for Group and Channel Selection -->
    <div class="dropdown-container">
      <label for="group-select">Group:</label>
      <select id="group-select" name="group">
        <option value="camping">Camping</option>
      </select>
      <label for="channel-select">Channel:</label>
      <select id="channel-select" name="channel">
        <option value=5>Tundra</option> <!-- original had both this and other parts with data-channel-id for the value portion. didn't work for my version so changed to value. this was how it is in the one channel post function -->
        <option value=6>Forest</option>
        <option value=7>Aquatic</option>
        <option value=8>Desert</option>
      </select>
    </div>

    <button type="submit">Add Post</button>
  </form>
  </div>

  <script>
  // Toggle visibility of item lists
  function toggleItems(id) {
    const selectedItem = document.getElementById(id);
    const currentState = selectedItem.style.display;
    selectedItem.style.display = currentState === 'none' ? 'block' : 'none';
  }

  // Handle item selection
  function selectItem(button, type, category) {
    const color = type === 'most' ? 'green' : 'red';
    button.style.backgroundColor = color;
    button.style.color = 'white';

    // Show the post form
    const formContainer = document.getElementById('form-container');
    formContainer.style.display = 'block';

    // Pre-fill form data based on the selected category
    document.getElementById('title').value = `${category} - ${type} favorite`;
    document.getElementById('comment').value = `I selected ${button.innerText} as my ${type} favorite because`;
    // Set the group to "camping" and set the category for the dropdown
    document.getElementById('group-select').value = 'camping';
    document.getElementById('channel-select').value = category;

    const channelID = button.getAttribute('data-channel-id');
    document.getElementById('postForm').setAttribute('data-channel-id', channelID); // Save the channel ID to the form
  }
</script>

<script type="module">
  import { pythonURI, fetchOptions } from '{{ site.baseurl }}/assets/js/api/config.js';

  // Fetch all arguments for a specific channel
  async function fetchArguments(channelId) {
    try {
      const response = await fetch(`${pythonURI}/api/posts/filter`, {
        ...fetchOptions,
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ channel_id: channelId })
      });

      if (!response.ok) throw new Error('Failed to fetch arguments: ' + response.statusText);

      const argumentsData = await response.json();
      argumentContainer.innerHTML = ""; // Clear existing arguments

      argumentsData.forEach(arg => {
        const card = document.createElement("div");
        card.classList.add("argument-card");

        const text = document.createElement("p");
        text.innerHTML = `<strong>${arg.user_name}:</strong> ${arg.comment}`; // Adjusted to match backend response structure

        card.appendChild(text);
        argumentContainer.appendChild(card);
      });
    } catch (error) {
      console.error('Error fetching arguments:', error);
    }
  }

  // Handle item selection
  function selectItem(button, type, category) {
    const color = type === 'most' ? 'green' : 'red';
    button.style.backgroundColor = color;
    button.style.color = 'white';

    // Create a post when an item is selected
    if (type === 'most') {
      document.getElementById('group-select').value = "camping";
      document.getElementById('channel-select').value = category;

      const postForm = document.getElementById('form-container');
      postForm.style.display = "block"; // Display post 
    }
  }

  // Handle form submission
  document.getElementById('postForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const title = document.getElementById('title').value;
    const comment = document.getElementById('comment').value;
    const group = document.getElementById('group-select').value;
    const channel = document.getElementById('channel-select').value;
    const channelID = document.getElementById('channel-select').value; // changed from original- now this will use the channel value that is chosen from channel select instead of data-channel-id
    const postData = {
      "title": title, 
      "comment": comment,
      "channel_id": channelID 
    }

    console.log(postData) // add this temporarily to see what comes up in inspect console 

    try {
      const response = await fetch(`${pythonURI}/api/post`, {
        ...fetchOptions,
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(postData)
      });

      if (!response.ok) throw new Error('Failed to add post: ' + response.statusText);
      alert("Post added successfully!");

    } catch (error) {
      console.error('Error adding post:', error);
    }
  });
</script>


