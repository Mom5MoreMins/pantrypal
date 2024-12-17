---
layout: post 
title: Buck Reef National Park
search_exclude: true
permalink: /national_parks/buck_reef
menu: nav/national_parks.html
---
# All About Buck Reef National Park! 🌊🪸


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