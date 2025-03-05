---
layout: post 
title: Buck Reef National Park
search_exclude: true
permalink: /national_parks/buck_reef
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
    <img src="{{ site.baseurl }}/images/NationalParkImages/ocean.jpg" alt="Image 1">
    <img src="{{ site.baseurl }}/images/NationalParkImages/BUCKREEFPIC.jpg" alt="Image 2">
    <img src="{{ site.baseurl }}/images/NationalParkImages/reeef.jpg" alt="Image 3">
</div>

<div class="content">
    <h2>Welcome to Buck Reef National Park</h2>
    <p>Explore the stunning underwater landscapes, vibrant marine life, and rich history of one of the most captivating reefs in the world. Whether you're planning a dive or simply looking to learn more, you're in the perfect place!</p>

    {% include buckreefmap.html %}

<div class="group-theme">
        <h3>Explore the gorgeous waters</h3>
        <p>Discover the best dive spots for breathtaking underwater views and unforgettable marine encounters. Buck Reef offers something for every level of diver!</p>
    </div>

<div class="group-theme">
        <h3>Wildlife and Nature</h3>
        <p>Buck Reef National Park in the Turks and Caicos Islands is home to vibrant coral reefs, tropical fish, and sea turtles, making it a haven for marine life. Its clear waters support diverse underwater ecosystems.</p>
    </div>
</div>


<div class="starring-section">
    <h3> Overall Rating </h3>
    <button id="deleteRatingBtn" style="background: none; border: none; float: right; font-size: 1.5rem; cursor: pointer;">
            🗑️
        </button>
    <p> Based on your experiences and the reviews below, submit your overall rating of the Buck Reef National Park here! </p>
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
    <input type="hidden" id="channel_id" name="channel_id" value="11">
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
            content: rating,
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
        document.getElementById('count').innerHTML = `<h4>Total Reviews: ${postData.length || 0}</h4>`;
        const detailsDiv = document.getElementById('details');
        detailsDiv.innerHTML = '';

        postData.forEach(post => {
            const stars = '★'.repeat(post.content) + '☆'.repeat(5 - post.content); // Generate star rating
            const postElement = document.createElement('div');
            postElement.className = 'post-item';
            postElement.style.marginBottom = "20px"; // Add spacing between reviews
            postElement.innerHTML = `
                <h3>${post.title}</h3>
                <p style="font-size: 1.5rem; color: gold;">${stars}</p>
                <p style="font-size: 0.9rem; color: #aaa;"><em>${post.user_name}</em></p>
                <p>${post.comment}</p>
            `; 
            detailsDiv.appendChild(postElement);
        });
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

    // Fetch posts on page load
    fetchData(11);



<<<<<<< HEAD


</script>


<h2 class="checklist-title">Checklist</h2>

<div class="checklist-section">
    <form id="checklistForm" class="checklist-form">
        <label for="item_name" class="checklist-label">Item Name:</label>
        <input type="text" id="item_name" name="item_name" required class="checklist-input">
        <button class="submit-btn checklist-btn">Add Item</button>
    </form>
</div>

<div class="checklist-container">
    <p id="count" class="checklist-count"></p>
    <div class="checklist-items" id="checklist-items"></div>
</div>

<style>
    body {
        font-family: Arial, sans-serif;
        background-color: #121212;
        color: #fff;
    }
    .checklist-title {
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        margin-top: 20px;
        color: #00ff00;
        text-shadow: 0 0 10px #00ff00;
    }
    .checklist-section, .checklist-container {
        text-align: center;
        margin: 20px auto;
        padding: 20px;
        background: #1e1e1e;
        border-radius: 10px;
        max-width: 400px;
        border: 2px solid #00ff00;
        box-shadow: 0 0 10px #00ff00;
    }
    .checklist-label {
        font-weight: bold;
    }
    .checklist-input {
        padding: 8px;
        border-radius: 5px;
        border: none;
        outline: none;
        margin-right: 10px;
    }
    .checklist-btn {
        background-color: #ff9800;
        border: none;
        padding: 8px 15px;
        border-radius: 5px;
        color: #fff;
        cursor: pointer;
        font-weight: bold;
    }
    .checklist-btn:hover {
        background-color: #e68900;
    }
    .checklist-item {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 10px;
        border-bottom: 1px solid #333;
    }
    .check-item {
        cursor: pointer;
    }
    .delete-btn {
        background-color: #ff4d4d;
        border: none;
        padding: 5px 10px;
        border-radius: 5px;
        color: #fff;
        cursor: pointer;
        font-weight: bold;
    }
    .delete-btn:hover {
        background-color: #e60000;
    }
</style>

<script type="module">
    import { pythonURI, fetchOptions } from '{{ site.baseurl }}/assets/js/api/config.js';

    document.getElementById("checklistForm").addEventListener("submit", async function(event) {
        event.preventDefault();

        const itemName = document.getElementById("item_name").value;
        const userId = localStorage.getItem("uid");
        if (!itemName.trim()) return;

        const postData = {
            user_id: userId,
            item_name: itemName,
            is_checked: false
        };

        try {
            const response = await fetch(`${pythonURI}/api/checklist`, {
                ...fetchOptions,
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(postData)
            });

            if (!response.ok) {
                throw new Error("Failed to add item: " + response.statusText);
            }

            alert("Item added successfully!");
            document.getElementById("checklistForm").reset();
            fetchChecklistItems();
        } catch (error) {
            console.error("Error adding item:", error);
            alert("Error adding item: " + error.message);
        }
    });

    async function fetchChecklistItems() {
        const userId = localStorage.getItem("uid");

        try {
            const response = await fetch(`${pythonURI}/api/checklist?user_id=${userId}`, {
                ...fetchOptions,
                method: "GET"
            });

            if (!response.ok) {
                throw new Error("Failed to fetch items: " + response.statusText);
            }

            const items = await response.json();
            document.getElementById("count").innerHTML = `<h4>Total Items: ${items.length || 0}</h4>`;
            const checklistDiv = document.getElementById("checklist-items");
            checklistDiv.innerHTML = "";

            items.forEach(item => {
                const itemElement = document.createElement("div");
                itemElement.className = "checklist-item";
                itemElement.innerHTML = `
                    <input type="checkbox" class="check-item" data-id="${item.id}" ${item.is_checked ? "checked" : ""}>
                    <span>${item.item_name}</span>
                    <button class="delete-btn" data-id="${item.id}">Delete</button>
                `;
                checklistDiv.appendChild(itemElement);
            });

            document.querySelectorAll(".delete-btn").forEach(button => {
                button.addEventListener("click", function() {
                    deleteItem(this.getAttribute("data-id"));
                });
            });

            document.querySelectorAll(".check-item").forEach(checkbox => {
                checkbox.addEventListener("change", function() {
                    updateItemStatus(this.getAttribute("data-id"), this.checked);
                });
            });
        } catch (error) {
            console.error("Error fetching items:", error);
        }
    }

    async function deleteItem(id) {
        try {
            await fetch(`${pythonURI}/api/checklist`, {
                ...fetchOptions,
                method: "DELETE",
                body: JSON.stringify({ id })
            });
            fetchChecklistItems();
        } catch (error) {
            console.error("Error deleting item:", error);
        }
    }

    async function updateItemStatus(id, isChecked) {
        try {
            await fetch(`${pythonURI}/api/checklist`, {
                ...fetchOptions,
                method: "PUT",
                body: JSON.stringify({ id, is_checked: isChecked })
            });
        } catch (error) {
            console.error("Error updating item status:", error);
        }
    }

    document.addEventListener("DOMContentLoaded", fetchChecklistItems);
</script>

>>>>>>> 189da01 (CHECKLIST FINISHED)
