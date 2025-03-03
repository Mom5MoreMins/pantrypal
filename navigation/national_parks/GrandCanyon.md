---
layout: post 
title: Grand Canyon
search_exclude: true
permalink: /national_parks/GrandCanyon
menu: nav/national_parks.html
---

<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
    body {
        font-family: 'Arial', sans-serif;
        background-color: #000;
        color: #e0e0e0;
        padding: 20px;
    }

    h2, h3 {
        font-family: 'Poppins', sans-serif;
        color: #00d4ff;
        margin-bottom: 10px;
    }

    h1 {
        font-family: "Poppins", sans-serif;
        color: #2E8B57;
        font-size: 2.5em;
        margin-bottom: 10px;
    }

    p {
        margin-bottom: 15px;
    }

    .group-theme {
        background: #000;
        color: #e0e0e0;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0 4px 8px 0 rgba(0, 212, 255, 0.2), 0 6px 20px 0 rgba(0, 212, 255, 0.19);
        border: 1px solid #bbf14f;
    }

    .group-theme h3 {
        margin-top: 0;
    }

    .image-scroller {
        width: 100%;
        overflow-x: scroll;
        overflow-y: hidden;
        white-space: nowrap;
        background-color: #111;
        border: 1px solid #bbf14f;
        border-radius: 10px;
        box-shadow: 0 4px 8px 0 rgba(0, 212, 255, 0.2), 0 6px 20px 0 rgba(0, 212, 255, 0.19);
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

    .content {
        text-align: center;
    }

    .review-section {
        margin-top: 30px;
        padding: 20px;
        background-color: #111;
        border-radius: 10px;
        border: 1px solid #bbf14f;
        box-shadow: 0 4px 8px 0 rgba(0, 212, 255, 0.2), 0 6px 20px 0 rgba(0, 212, 255, 0.19);
        text-align: left;
        color: #e0e0e0;
    }

    .review-section h3 {
        color: #00d4ff;
    }

    .review-input {
        width: 100%;
        margin-top: 10px;
        padding: 10px;
        font-family: 'Poppins', sans-serif;
        border-radius: 5px;
        border: 1px solid #bbf14f;
        background-color: #222;
        color: #e0e0e0;
    }

    .submit-btn {
        margin-top: 20px;
        padding: 12px 25px;
        background-color: #00d4ff;
        border: none;
        color: white;
        border-radius: 6px;
        cursor: pointer;
        font-size: 1rem;
    }

    .submit-btn:hover {
        background-color: #007a99;
    }

    .star-rating {
        margin-top: 20px;
        display: flex;
        justify-content: center;
    }

    .star {
        font-size: 2.5rem;
        color: #bbb;
        cursor: pointer;
        margin: 0 8px;
        transition: color 0.3s, transform 0.2s;
    }


    .star:hover,
    .star:hover ~ .star {
        color: #ff0;
        transform: scale(1.1);
    }

    .post-item {
        background-color: #111;
        border: 1px solid #95becf;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 20px;
    }

    .post-item h3 {
        margin-top: 0;
    }

    .post-item p {
        margin-bottom: 10px;
    }

    .post-item .star-rating {
        font-size: 1.5rem;
        color: gold;
    }

    .post-item .user-name {
        font-size: 0.9rem;
        color: #aaa;
        margin-bottom: 10px;
    }
    .starring-section {
        margin-top: 30px;
        padding: 20px;
        background-color: #111;
        border-radius: 10px;
        border: 1px rgb(206, 185, 255);
        box-shadow: 0 4px 8px 0 rgba(0, 212, 255, 0.2), 0 6px 20px 0 rgba(0, 212, 255, 0.19);
        text-align: left;
        color: #e0e0e0;
    }

</style>


<div class="image-scroller">
    <img src="{{ site.baseurl }}/images/NationalParkImages/image.png" alt="Image 1">
     <img src="{{ site.baseurl }}/images/NationalParkImages/GrandCanyonText1.png" alt="Hiking Trails" style="margin-left: 10px;">
    <img src="{{ site.baseurl }}/images/NationalParkImages/Pic1.jpg" alt="Image 2">
    <img src="{{ site.baseurl }}/images/NationalParkImages/Pic2.jpg" alt="Image 3">
    <img src="{{ site.baseurl }}/images/NationalParkImages/Pic4.png" alt="Image 4">
    <img src="{{ site.baseurl }}/images/NationalParkImages/GrandCanyon5.jpg" alt="Image 5">
</div>

<div class="content">
    <h2>Welcome to Grand Canyon National Park</h2>
    <p>Explore the breathtaking landscapes, unique wildlife, and rich history of one of the most iconic natural wonders of the world. Whether you're planning a visit or just learning more, you're in the right place!</p>

{% include google_maps.html %}

<div class="group-theme">
        <h3>Hiking Trails</h3>
        <p>The Grand Canyon is home to diverse wildlife, including species such as bighorn sheep, mule deer, and a variety of birds like the California condor. Its unique ecosystems, from the desert floor to the forested rim, support a rich array of plants and animals adapted to the extreme conditions of this iconic landscape.</p>
    </div>

<div class="group-theme">
        <h3>Wildlife and Nature</h3>
        <p>Learn about the unique wildlife and ecosystems of the Grand Canyon National Park.</p>
    </div>
</div>


<div class="starring-section">
    <h3> Overall Rating </h3>
    <button id="deleteRatingBtn" style="background: none; border: none; float: right; font-size: 1.5rem; cursor: pointer;">
            🗑️
        </button>
    <p> Based on your experiences and the reviews below, submit your overall rating of the Grand Canyon National Park here! </p>
    <div class="star-rating">
        <span class="star" data-stars-overall="1" data-rating-type="overall">&#9733;</span>
        <span class="star" data-stars-overall="2" data-rating-type="overall">&#9733;</span>
        <span class="star" data-stars-overall="3" data-rating-type="overall">&#9733;</span>
        <span class="star" data-stars-overall="4" data-rating-type="overall">&#9733;</span>
        <span class="star" data-stars-overall="5" data-rating-type="overall">&#9733;</span>
    </div>
    <button class="submit-btn" type="overall">Submit Overall Star Rating</button>
</div>

<div class="review-section">
<form id="postForm">
    <label for="title">Title:</label>
    <input type="text" id="title" name="title" required>
    <textarea class="review-input" id="comment" name="comment" placeholder="Write your review here..."></textarea>
    <input type="hidden" id="group_id" name="group_id" value="national parks">
    <input type="hidden" id="channel_id" name="channel_id" value="13">
    <div class="star-rating">
        <span class="star" data-stars-review="1" data-rating-type="review">&#9733;</span>
        <span class="star" data-stars-review="2" data-rating-type="review">&#9733;</span>
        <span class="star" data-stars-review="3" data-rating-type="review">&#9733;</span>
        <span class="star" data-stars-review="4" data-rating-type="review">&#9733;</span>
        <span class="star" data-stars-review="5" data-rating-type="review">&#9733;</span>
    </div>
    <button class="submit-btn">Submit Review</button>
</form>
</div>

<div>
    <p id="count"></p>
    <div class="details" id="details"></div>
</div>

<script>

// Declare the rating variable and initialize it for overall and review separately
let overall_rating = 0;
let review_rating = 0;

// Set up the star click functionality for overall rating
document.querySelectorAll('.star[data-rating-type="overall"]').forEach(star => {
    star.addEventListener('click', function () {
        const overall_stars = parseInt(this.getAttribute('data-stars-overall'), 10);
        setRating(overall_stars, 'overall');
    });
});

// Set up the star click functionality for review rating
document.querySelectorAll('.star[data-rating-type="review"]').forEach(star => {
    star.addEventListener('click', function () {
        const review_stars = this.getAttribute('data-stars-review');
        console.log(`Review star clicked with value: ${review_stars}`);  // Log value
        const review_stars_int = parseInt(review_stars, 10);
        if (!isNaN(review_stars_int)) {
            setRating(review_stars_int, 'review');
        } else {
            console.error("Invalid rating value", review_stars);  // Log invalid value
        }
    });
});

// Function to update the rating and highlight the stars for different rating types
function setRating(stars, type) {
    if (type === 'overall') {
        overall_rating = stars;
        document.querySelectorAll('.star[data-rating-type="overall"]').forEach((star, index) => {
            star.style.color = (index < stars) ? '#ff0' : '#bbb';
        });
        console.log(`Overall Rating set to: ${stars}`);
    } else if (type === 'review') {
        review_rating = stars;
        document.querySelectorAll('.star[data-rating-type="review"]').forEach((star, index) => {
            star.style.color = (index < stars) ? '#ff0' : '#bbb';
        });
        console.log(`Review Rating set to: ${stars}`);
    }
}
</script>

<script type="module">
    import { pythonURI, fetchOptions } from '{{ site.baseurl }}/assets/js/api/config.js';

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
            content: review_rating,
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
    
    document.querySelector('.submit-btn').addEventListener('click', async function(event) {
        event.preventDefault();
        const channelId = document.getElementById('channel_id').value;  // Assuming channel_id is still available
        const userId = localStorage.getItem('uid');
        console.log(userId);  

        if (overall_rating > 0) {
            try {
                const ratingData = {
                    stars: overall_rating,
                    user_id: userId,
                    channel_id: channelId
                };

                const ratingResponse = await fetch(`${pythonURI}/api/rating`, {  // Use backticks for string interpolation
                    ...fetchOptions,
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(ratingData)
                });

                if (!ratingResponse.ok) {
                    throw new Error('Failed to submit rating: ' + ratingResponse.statusText);
                }
                alert('Rating submitted successfully!');
                console.log('Rating submitted successfully!');
            } catch (error) {
                console.error('Error submitting rating:', error);
            }
        } else {
            alert('Please select an overall rating before submitting.');
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
        document.getElementById('count').innerHTML = `<h4>Total Reviews: ${postData.length || 0}</h4>`;
        const detailsDiv = document.getElementById('details');
        detailsDiv.innerHTML = '';

        postData.forEach(post => {
            const stars = '★'.repeat(post.content) + '☆'.repeat(5 - post.content); // Generate star rating
            const postElement = document.createElement('div');
            postElement.className = 'post-item';
            postElement.style.marginBottom = "20px"; // Add spacing between reviews
            postElement.innerHTML = 
                `<h3>${post.title}</h3>
                <p style="font-size: 1.5rem; color: gold;">${stars}</p>
                <p style="font-size: 0.9rem; color: #aaa;"><em>${post.user_name}</em></p>
                <p>${post.comment}</p>`;
            detailsDiv.appendChild(postElement);
        });
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

/**
 * Fetch and fill the existing overall stars
 */

const userId = localStorage.getItem('uid');
const channelId = document.getElementById('channel_id').value;  // Assuming channel_id is still available

async function fetchAndFillOverallStars(channelId) {
    try {
        // Fetch overall rating from the endpoint
        const fetchingRatingData = {
                    user_id: userId,
                    channel_id: channelId
                };

        const response = await fetch(`${pythonURI}/api/rating`, {
            ...fetchOptions,
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(fetchingRatingData)
        });

        if (!response.ok) {
            throw new Error('Failed to fetch overall rating: ' + response.statusText);
        }

        // Parse the response to get the star rating
        const { stars } = await response.json();

        // Find the existing stars for overall rating and fill them
        document.querySelectorAll('.star[data-rating-type="overall"]').forEach((star, index) => {
            star.style.color = (index < stars) ? '#ff0' : '#bbb'; // Fill stars with yellow for selected, grey for the rest
        });

    } catch (error) {
        console.error('Error fetching overall stars:', error);
    }
}

document.getElementById('deleteRatingBtn').addEventListener('click', async function () {
    const userId = localStorage.getItem('uid'); // Assume user ID is stored in local storage
    const confirmed = confirm("Are you sure you want to delete your ratings?");

    if (confirmed) {
        try {
            // Send DELETE request to backend
            const response = await fetch(`${pythonURI}/api/rating`, {
                ...fetchOptions,
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ user_id: userId })
            });

            if (!response.ok) {
                throw new Error('Failed to delete ratings: ' + response.statusText);
            }

            alert('Your ratings have been deleted.');

            // Reset the stars to be blank
            document.querySelectorAll('.star[data-rating-type="overall"]').forEach(star => {
                star.style.color = '#bbb'; // Set stars to default color
            });
        } catch (error) {
            console.error('Error deleting ratings:', error);
            alert('Error deleting your ratings: ' + error.message);
        }
    }
});


// Call the function on page load
document.addEventListener('DOMContentLoaded', () => fetchAndFillOverallStars(13)); // Replace 13 with your desired channel ID

    // Fetch posts on page load
    fetchData(13);

</script>

<script>

// Declare checklist array
let checklist = [];

// Function to fetch the checklist from the backend
async function fetchChecklist() {
    const token = localStorage.getItem("token");
    try {
        const response = await fetch("/api/checklist", {
            headers: { "Authorization": `Bearer ${token}` }
        });
        if (!response.ok) throw new Error("Failed to fetch checklist");
        checklist = await response.json();
        renderChecklist();
    } catch (error) {
        console.error("Error fetching checklist:", error);
    }
}

// Function to add an item to the checklist
async function addItem() {
    const newItem = document.getElementById("newItem").value;
    if (!newItem) return;

    const token = localStorage.getItem("token");
    try {
        const response = await fetch("/api/checklist", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${token}`
            },
            body: JSON.stringify({ item_name: newItem })
        });

        if (!response.ok) throw new Error("Failed to add item");

        const data = await response.json();
        checklist.push(data);
        document.getElementById("newItem").value = "";
        renderChecklist();
    } catch (error) {
        console.error("Error adding item:", error);
    }
}

// Function to remove an item from the checklist
async function removeItem(id) {
    const token = localStorage.getItem("token");
    try {
        const response = await fetch("/api/checklist", {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${token}`
            },
            body: JSON.stringify({ id })
        });

        if (!response.ok) throw new Error("Failed to delete item");

        checklist = checklist.filter(item => item.id !== id);
        renderChecklist();
    } catch (error) {
        console.error("Error deleting item:", error);
    }
}

// Function to render checklist items
function renderChecklist() {
    const listElement = document.getElementById("checklistItems");
    listElement.innerHTML = "";
    checklist.forEach(item => {
        const listItem = document.createElement("li");
        listItem.innerHTML = `${item.item_name} <button onclick="removeItem(${item.id})">Remove</button>`;
        listElement.appendChild(listItem);
    });
}

// Fetch checklist on page load
document.addEventListener("DOMContentLoaded", fetchChecklist);

</script>

### 🏕️ Camping Checklist

<div>
    <input type="text" id="newItem" placeholder="Add an item..." />
    <button onclick="addItem()">Add</button>

<ul id="checklistItems"></ul>
</div>
