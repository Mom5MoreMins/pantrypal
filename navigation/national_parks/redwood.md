---
layout: post 
title: Redwood National Park
search_exclude: true
permalink: /national_parks/redwood
menu: nav/national_parks.html
---

<div class="post-form-container" id="post-form" style="display: none;">
  <h2>Post a Review</h2>
  <form id="postForm">
    <label for="title">Title:</label>
    <input type="text" id="title" name="title" required>
    <p></p>
    <label for="comment">Comment:</label>
    <textarea id="comment" name="comment" required></textarea>
    <button type="submit">Add Review</button>
  </form>
</div>

<div id="post-list" class="post-list-container">
  <!-- Fetched posts will be displayed here -->
</div>


<script>
  document.addEventListener('DOMContentLoaded', () => {
    // Show the post form by default
    const formContainer = document.getElementById('post-form');
    formContainer.style.display = 'block';

    // Pre-fill form fields with default values for Redwood National Park
    document.getElementById('title').value = 'Review for Redwood National Park';
    document.getElementById('comment').value = 'Enter your comments here...';
    document.getElementById('group-select').value = 'National Parks';

    // Populate the channel dropdown with the "Redwood" option
    const channelSelect = document.getElementById('channel-select');
    channelSelect.innerHTML = ''; // Clear existing options
    const redwoodOption = document.createElement('option');
    redwoodOption.value = 'Redwood';
    redwoodOption.text = 'Redwood';
    channelSelect.appendChild(redwoodOption);
    channelSelect.value = 'Redwood'; // Set default selection to Redwood

    // Set a default channel ID (example: 12 for Redwood)
    const channelID = 12;
    document.getElementById('postForm').setAttribute('data-channel-id', channelID);
  });

  document.getElementById('postForm').addEventListener('submit', async (e) => {
    e.preventDefault(); // Prevent default form submission behavior

    // Get form data
    const title = document.getElementById('title').value;
    const comment = document.getElementById('comment').value;
    const group = document.getElementById('group-select').value;
    const channel = document.getElementById('channel-select').value;
    const channelID = document.getElementById('postForm').getAttribute('data-channel-id');

    const postData = {
      title: title,
      comment: comment,
      channel_id: channelID,
    };

    try {
      // Log post data for debugging
      console.log('Submitting post data:', postData);

      const response = await fetch(`${pythonURI}/api/post`, {
        ...fetchOptions,
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(postData),
      });

      if (!response.ok) {
        console.error('Failed to submit post:', response.statusText);
        alert('Error: Could not submit your review. Please try again later.');
        return;
      }

      const result = await response.json();
      console.log('Post submitted successfully:', result);

      alert('Review submitted successfully!');
      document.getElementById('postForm').reset(); // Reset form after successful submission
    } catch (error) {
      console.error('Error during submission:', error);
      alert('Error: Unable to submit your review. Please check the console for more details.');
    }
  });
</script>

<style>
  .post-form-container {
    background-color: #13292b;
    border: 1px solid #ccc;
    padding: 20px;
    border-radius: 8px;
    margin-top: 20px;
  }

  .post-item {
    background-color: #13292b;
    padding: 10px;
    margin-bottom: 10px;
    border-radius: 5px;
  }
</style>
