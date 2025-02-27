---
layout: post 
title: Choose a biome to post about!
search_exclude: true
permalink: /camping/page2
menu: nav/camping.html
---

<style>
    /* Shared Flex Container */
    .flex-column-centered {
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;
        padding: 20px;
        box-sizing: border-box;
    }

    /* Shared Form and Post Styles */
    .form-container, .post-item {
        display: flex;
        flex-direction: column;
        width: 100%;
        max-width: 800px;
        background-color: #545e75;
        box-shadow: 0 4px 8px 0 #f0f6f6, 0 6px 20px 0 #f0f6f6;
        padding: 20px;
        border-radius: 10px;
        border: 3px solid #545e75;
        color: #c9cad9;
        margin-bottom: 20px;
        box-sizing: border-box;
    }

    /* Text Styling for Post Items */
    .post-item h3, .post-item p {
        margin: 0 0 10px;
        width: 100%;
    }

    /* Styling for Form Labels */
    .form-container label {
        margin-bottom: 5px;
    }

    /* Styling for Form Inputs and Textareas */
    .form-container input, .form-container textarea {
        margin-bottom: 10px;
        padding: 10px;
        border-radius: 5px;
        border: none;
        width: 100%;
    }

    /* Button Styling for Form */
    .form-container button {
        padding: 10px;
        border-radius: 5px;
        border: none;
        background-color: #545e75;
        color: #c9cad9;
        cursor: pointer;
    }

    /* Shared Container for Details Section */
    .details {
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;
        max-width: 1200px;
        padding: 20px;
        box-sizing: border-box;
    }

    .button {
        display: block !important; /* Force the button to display */
    }


    .image-scroller {
        width: 100%;
        overflow-x: scroll;
        overflow-y: hidden;
        white-space: nowrap;
        background-color:rgb(35, 41, 51);
        border: 1px solid #545e75;
        border-radius: 10px;
        box-shadow: 0 4px 8px 0 #f0f6f6, 0 6px 20px 0 #f0f6f6;
        margin: 20px auto;
        padding: 10px 0;
    }

    .image-scroller img {
        display: inline-block;
        width: 400px;
        height: 300px;
        margin-right: 10px;
        border-radius: 5px;
        object-fit: cover;
    }

</style>



<div class="image-scroller">
    <img src="{{ site.baseurl }}/images/camping/beachcamping.jpg" alt="Beach Biome">
     <img src="{{ site.baseurl }}/images/camping/desertcamping.png" alt="Desert Biome" style="margin-left: 10px;">
    <img src="{{ site.baseurl }}/images/camping/forestcamping.jpg" alt="Forest Biome">
    <img src="{{ site.baseurl }}/images/camping/tundracamping.jpg" alt="Tundra Biome">
</div>


<div class="container">
    <div class="form-container">
  <h2>Create a Post</h2>
  <form id="postForm">
    <input type="text" id="title" name="title" required placeholder="Title">
    <textarea id="comment" name="comment" required placeholder="Comment"></textarea>
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

  <div>
    <p id="count"></p>
    <div class="details" id="details"></div>
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
  // delete function in its own script tag to put it in a global scope/independent 
  import { pythonURI, fetchOptions } from '{{ site.baseurl }}/assets/js/api/config.js';

    console.log('deletePost function is defined:', typeof deletePost === 'function');
    
    //attatch deletePost defintion to global window so that deletePost can still globally be defined under a script module 
    window.deletePost = async function deletePost(postId) {
      
      const token = localStorage.getItem('token'); 
        try {
          
            const response = await fetch(`${pythonURI}/api/campingPost`, {
              ...fetchOptions,
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`
                },
                body: JSON.stringify({ id: postId })
            });

            if (!response.ok) {
                throw new Error('Failed to delete post: ' + response.statusText);
            }

            const data = await response.json();
            console.log('Post deleted successfully:', data.message);

            // Remove the deleted post from the UI
            document.querySelector(`#post-${postId}`).remove();

            // Update post count
            document.getElementById('count').innerHTML = `<h4>Total Posts: ${posts.length || 0}</h4>`;

        } catch (error) {
            console.error('Error deleting post:', error);
        }
    }
</script>

<script type="module">
document.addEventListener('DOMContentLoaded', async () => {
    const channelSelect = document.getElementById('channel-select');
    const selectedChannelId = channelSelect.value; // Get the selected channel from dropdown
    await fetchData(selectedChannelId); // Fetch posts BEFORE anything else
});

  import { pythonURI, fetchOptions } from '{{ site.baseurl }}/assets/js/api/config.js';

  // Fetch all arguments for a specific channel
  async function fetchArguments(channelId) {
    try {
      const response = await fetch(`${pythonURI}/api/campingPosts/filter`, {
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
      const response = await fetch(`${pythonURI}/api/campingPost`, {
        ...fetchOptions,
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(postData)
      });

      if (!response.ok) throw new Error('Failed to add post: ' + response.statusText);
      alert("Post added successfully!");

      await fetchData(channelID); // Refresh posts for the current channel

    } catch (error) {
      console.error('Error adding post:', error);
    }
  });

async function fetchPost(channelId) {
    try {
        // Fetch posts from the endpoint
        const response = await fetch(`${pythonURI}/api/campingPost`, {
            ...fetchOptions,
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ channel_id: channelId, user_id: userId }) // Adjust payload as needed
        });

        if (!response.ok) {
            throw new Error('Failed to fetch posts: ' + response.statusText);
        }

        // Parse the response to get the posts data
        const posts = await response.json();

        // Update the total posts count
        const countDiv = document.getElementById('count');
        countDiv.innerHTML = `<h4>Total Posts: ${posts.length || 0}</h4>`;

        // Clear and update the details section with the fetched posts
        const detailsDiv = document.getElementById('details');
        detailsDiv.innerHTML = ''; // Clear existing content

        // Loop through the posts and display them
        posts.forEach(post => {
            const postElement = document.createElement('div');
            postElement.className = 'post-item';
            postElement.style.marginBottom = '20px';
            postElement.id = `post-${post.id}`;

            // Create the delete button
            const deleteButton = `<button onclick="deletePost(${post.id})">Delete</button>`;

            // Add post content
            postElement.innerHTML = `
                <h3>${post.title}</h3>
                <p style="font-size: 0.9rem; color: #000000;"><em>${post.user_name}</em></p>
                <p>${post.comment}</p>
                ${deleteButton}
            `;

            detailsDiv.appendChild(postElement);
        });
    } catch (error) {
        console.error('Error fetching posts:', error);
    }
}


    /**
     * Fetch and display posts
     */
  async function fetchData(channelId) {
    try {
      const response = await fetch(`${pythonURI}/api/campingPosts/filter`, {
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
        document.getElementById('count').innerHTML = `<h4>Total Posts: ${postData.length || 0}</h4>`;
        const detailsDiv = document.getElementById('details');
        detailsDiv.innerHTML = '';

        postData.forEach(post => {
            const postElement = document.createElement('div');
            postElement.className = 'post-item';
            postElement.style.marginBottom = "20px";
            postElement.id = `post-${post.id}`;

             // Create the delete button
            const deleteButton = `<button onclick="deletePost(${post.id})">Delete</button>`;
            postElement.innerHTML = `
                <h3>${post.title}</h3>
                <p style="font-size: 0.9rem; color: #000000;"><em>${post.user_name}</em></p>
                <p>${post.comment}</p>
                ${deleteButton}
            `;

            postElement.innerHTML = `
                <h3>${post.title}</h3>
                <p style="font-size: 0.9rem; color: #000000;"><em>${post.user_name}</em></p>
                <p>${post.comment}</p>
                ${deleteButton}
            `;

            detailsDiv.appendChild(postElement);
        });
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

window.deletePost = async function deletePost(postId) {
    const token = localStorage.getItem('token');  // Get token from localStorage
    try {
        const response = await fetch(`${pythonURI}/api/campingPost`, {
            ...fetchOptions,
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`  
            },
            body: JSON.stringify({ id: postId })  // Send the postId to delete the specific post
        });

        if (!response.ok) {
            throw new Error('Failed to delete post: ' + response.statusText);
        }

        const data = await response.json();
        console.log('Post deleted successfully:', data.message);

        //remove post from dom by postid
        document.querySelector(`#post-${postId}`).remove();  
    } catch (error) {
        console.error('Error deleting post:', error);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const channelSelect = document.getElementById('channel-select');
    const selectedChannelId = channelSelect.value; // Get the selected channel from dropdown
    fetchData(selectedChannelId); // Fetch posts for the selected channel
});

document.getElementById('channel-select').addEventListener('change', function () {
    const selectedChannelId = this.value; // Get the selected channel
    fetchData(selectedChannelId); // Fetch posts for the new selection
});


</script>


