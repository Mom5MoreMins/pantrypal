---
layout: post 
title: Redwood National Park
search_exclude: true
permalink: /national_parks/redwood
menu: nav/national_parks.html
---

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
</style>

<div class="image-scroller">
    <img src="{{ site.baseurl }}/images/NationalParkImages/redwood.webp" alt="Image 1">
    <img src="{{ site.baseurl }}/images/NationalParkImages/redwood2.jpg" alt="Image 2">
    <img src="{{ site.baseurl }}/images/NationalParkImages/redwood3.jpg" alt="Image 3">
    <img src="{{ site.baseurl }}/images/NationalParkImages/redwood4.jpg" alt="Image 4">
    <img src="{{ site.baseurl }}/images/NationalParkImages/redwood5.jpeg" alt="Image 5">
</div>

<div class="content">
    <h2>Welcome to Redwood National Park</h2>
    <p>Explore the stunning landscapes, towering trees, diverse wildlife, and rich history of Redwood National Park, home to some of the tallest trees on Earth. These ancient giants, some over 2,000 years old, create a breathtaking forest canopy that must be seen to be believed. Whether you're planning a visit to stand beneath the awe-inspiring redwoods or simply curious to learn more about this remarkable ecosystem, you've come to the perfect place!</p>

{% include redwoodmaps.html %}

<div class="group-theme">
        <h3>Hiking Trails</h3>
        <p>Discover the best trails for breathtaking views and unforgettable experiences in Redwood National Park, where you can hike among towering ancient trees, from easy walks through serene groves to more challenging treks up scenic ridges, offering something for every level of hiker!</p>
    </div>

<div class="group-theme">
        <h3>Wildlife and Nature</h3>
        <p>Redwood National Park is a haven for diverse wildlife and lush nature, home to majestic redwoods, elk, black bears, and countless bird species, all thriving in its rich, vibrant ecosystems.</p>
    </div>
</div>


<div class="review-section">
<form id="postForm">
    <label for="title">Title:</label>
    <input type="text" id="title" name="title" required>
    <textarea class="review-input" id="comment" name="comment" placeholder="Write your review here..."></textarea>
    <input type="hidden" id="group_id" name="group_id" value="national parks">
    <input type="hidden" id="channel_id" name="channel_id" value="12">
    <div class="star-rating">
        <span class="star" data-stars="1">&#9733;</span>
        <span class="star" data-stars="2">&#9733;</span>
        <span class="star" data-stars="3">&#9733;</span>
        <span class="star" data-stars="4">&#9733;</span>
        <span class="star" data-stars="5">&#9733;</span>
    </div>
    <button class="submit-btn">Submit Review</button>
</form>
</div>

<div>
    <p id="count"></p>
    <div class="details" id="details"></div>
</div>
<script>
    let rating = 0; // Declare the rating variable and initialize it
    document.querySelectorAll('.star').forEach(star => {
        star.addEventListener('click', function () {
            const stars = parseInt(this.getAttribute('data-stars'), 10);
            setRating(stars);
        });
    });
    function setRating(stars) {
        rating = stars; // Update the global rating variable
        document.querySelectorAll('.star').forEach((star, index) => {
            star.style.color = (index < stars) ? '#ff0' : '#bbb';
        });
        console.log(`Rating set to: ${stars}`);
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
    fetchData(12);



</script>



<div id="analyticsSummary" class="group-theme">
    <h3>Analytics Summary</h3>
</div>

<script>
    /**
     * Fetch and display analytics summary for all parks.
     */
    async function fetchAnalytics() {
        try {
            const response = await fetch('/api/analytics/summary', {
                method: 'GET',
                headers: {
                    'Authorization': `___`, // Replace with your actual token logic
                    'Content-Type': 'application/json'
                }
            });

            if (!response.ok) {
                throw new Error('Failed to fetch analytics summary: ' + response.statusText);
            }

  
            const analyticsData = await response.json();

     
            const analyticsDiv = document.getElementById('analyticsSummary');
            analyticsDiv.innerHTML = ''; 

     
            analyticsData.forEach(entry => {
                const summaryElement = document.createElement('div');
                summaryElement.className = 'analytics-item';
                summaryElement.innerHTML = `
                    <h3>Park: ${entry.park_id}</h3>
                    <p>Average Rating: ${entry.stars.toFixed(1)}</p>
                    <p>Total Reviews: ${entry.total_reviews}</p>
                `;
                analyticsDiv.appendChild(summaryElement);
            });
        } catch (error) {
            console.error('Error fetching analytics:', error);
        }
    }

   
    document.addEventListener('DOMContentLoaded', fetchAnalytics);
    
</script>