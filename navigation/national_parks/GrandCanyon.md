---
layout: post 
title: Grand Canyon
search_exclude: true
permalink: /national_parks/GrandCanyon
menu: nav/national_parks.html
---

<h1>Grand Canyon National Park 🏜️🌄</h1>

<style>
    body {
        font-family: 'Poppins', sans-serif;
        background-color: #000;
        color: #e0e0e0;
        padding: 20px;
    }

    h2, h3 {
        color: #00d4ff;
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
        margin-top: 10px;
        padding: 10px 20px;
        background-color: #00d4ff;
        border: none;
        color: #fff;
        border-radius: 5px;
        cursor: pointer;
        font-family: 'Poppins', sans-serif;
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
        font-size: 2rem;
        color: #bbb;
        cursor: pointer;
        margin: 0 5px;
        transition: color 0.3s;
    }

    .star:hover,
    .star:hover ~ .star {
        color: #ff0;
    }
</style>

<div class="image-scroller">
    <img src="{{ site.baseurl }}/images/NationalParkImages/image.png" alt="Image 1">
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
        <p>Discover the best trails for breathtaking views and incredible experiences. The Grand Canyon has something for every level of hiker!</p>
    </div>

<div class="group-theme">
        <h3>Wildlife and Nature</h3>
        <p>Learn about the unique wildlife and ecosystems of the Grand Canyon National Park.</p>
    </div>
</div>

<div class="review-section">
    <h3>Leave a review</h3>
    <textarea class="review-input" placeholder="Write your review here..."></textarea>
    <button class="submit-btn">Submit Review</button>

    <div class="star-rating">
        <span class="star" onclick="setRating(1)">&#9733;</span>
        <span class="star" onclick="setRating(2)">&#9733;</span>
        <span class="star" onclick="setRating(3)">&#9733;</span>
        <span class="star" onclick="setRating(4)">&#9733;</span>
        <span class="star" onclick="setRating(5)">&#9733;</span>
    </div>
</div>

<script>
    let rating = 0;

    // Function to set the rating
    function setRating(stars) {
        rating = stars;
        document.querySelectorAll('.star').forEach((star, index) => {
            star.style.color = (index < stars) ? '#ff0' : '#bbb';
        });
    }

    // Handle review submission
    document.querySelector('.submit-btn').addEventListener('click', function() {
        const title = 'Grand Canyon Review';  // You can dynamically set this from the page title
        const comment = document.querySelector('.review-input').value;
        const content = { rating: rating };  // Add any extra data if necessary
        const channel_id = 1;  // Static for now or dynamically set it based on the context

        // Validate that the review has a comment
        if (!comment.trim()) {
            alert('Please write a review.');
            return;
        }

        // Create the review object
        const review = {
            title: title,
            comment: comment,
            content: content,
            channel_id: channel_id
        };

        // Send the review data to the backend
        fetch('/api/review', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + localStorage.getItem('jwt_token') // Make sure the token is available
            },
            body: JSON.stringify(review)
        })
        .then(response => response.json())
    .then(data => {
    if (data.message) {
        alert(data.message); // Handle error from backend
    } else {
        alert('Review submitted successfully!');
    }
})
        .catch(error => {
            console.error('Error:', error);
            alert('Failed to submit review.');
        });
    });

</script>