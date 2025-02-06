---
layout: post 
title: Denali
search_exclude: true
permalink: /national_parks/Denali
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
    <img src="{{ site.baseurl }}/images/NationalParkImages/Denali-summit.jpg" alt="Image 1">
    <img src="{{ site.baseurl }}/images/NationalParkImages/moose.jpg" alt="Image 2">
    <img src="{{ site.baseurl }}/images/NationalParkImages/wildlife.jpg" alt="Image 3">
    <img src="{{ site.baseurl }}/images/NationalParkImages/amazing.webp" alt="Image 4">
</div>

<div class="content">
    <h2>Welcome to Denali National Park</h2>
    <p>Denali National Park, located in Alaska, is renowned for its stunning landscapes, including North America's highest peak, Denali, and its diverse ecosystems that support a wide range of wildlife and outdoor adventures.</p>

{% include denalimaps.html %}

<div class="group-theme">
        <h3>Hiking Trails</h3>
        <p>Hiking in Denali offers an unparalleled adventure through Alaska's rugged wilderness, where expansive views of towering peaks, glaciers, and wildlife await. With trails ranging from accessible to challenging, hikers can immerse themselves in the raw beauty and serenity of North America's highest mountain, Denali.</p>
    </div>

<div class="group-theme">
        <h3>Wildlife and Nature</h3>
        <p>Denali National Park is home to diverse wildlife, including grizzly bears, moose, wolves, and caribou, surrounded by rugged mountains, pristine rivers, and expansive tundra, creating a breathtaking and untouched wilderness.</p>
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
    fetchData(10);



</script>

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Analytics Dashboard</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #121212;
            color: #fff;
        }
        .dashboard {
            max-width: 1200px;
            margin: 20px auto;
            padding: 20px;
            background: #1e1e1e;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 255, 0, 0.2);
        }
        h1, h2 {
            text-align: center;
            color: #0f0;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            background-color: #252525;
            color: #fff;
        }
        table th, table td {
            padding: 10px;
            text-align: left;
            border: 1px solid #333;
        }
        table th {
            background-color: #0f0;
            color: black;
        }
        .form-section {
            margin-bottom: 20px;
            padding: 15px;
            border-radius: 5px;
            background: #181818;
            box-shadow: 0px 0px 10px rgba(0, 255, 0, 0.2);
        }
        .form-section label {
            display: block;
            margin-bottom: 8px;
            font-weight: bold;
            color: #0f0;
        }
        .form-section input, .form-section button {
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #0f0;
            border-radius: 4px;
            background-color: #252525;
            color: #0f0;
        }
        .form-section input:focus {
            outline: none;
            box-shadow: 0 0 8px #0f0;
        }
        .form-section button {
            background-color: #0f0;
            color: black;
            font-weight: bold;
            cursor: pointer;
            transition: 0.3s;
        }
        .form-section button:hover {
            background-color: #00ff88;
            color: black;
            box-shadow: 0px 0px 10px #0f0;
        }
    </style>
</head>
<body>

<div class="dashboard">
    <h1>Analytics Dashboard</h1>

    <div class="form-section">
        <label for="channel_id">Channel ID</label>
        <input type="text" id="channel_id" placeholder="Enter Channel ID">
        <label for="user_id">User ID</label>
        <input type="text" id="user_id" placeholder="Enter User ID">
        <label for="stars">Stars</label>
        <input type="number" id="stars" placeholder="Enter Stars (1-5)" min="1" max="5">
        <button id="submitAnalytics">Submit Analytics</button>
    </div>

    <h2>Analytics Summary</h2>
    <table>
        <thead>
            <tr>
                <th>Channel ID</th>
                <th>Average Stars</th>
                <th>Total Reviews</th>
            </tr>
        </thead>
        <tbody id="analyticsSummary">
            <!-- Data will be dynamically inserted here -->
        </tbody>
    </table>
</div>

<script>
    // Placeholder for storing analytics data locally
    const analyticsData = [];

    document.getElementById('submitAnalytics').addEventListener('click', () => {
        const channelId = document.getElementById('channel_id').value;
        const userId = document.getElementById('user_id').value;
        const stars = parseInt(document.getElementById('stars').value, 10);

        if (!channelId || !userId || isNaN(stars) || stars < 1 || stars > 5) {
            alert('Please fill all fields correctly.');
            return;
        }

        // Add analytics data to the array
        analyticsData.push({ channel_id: channelId, user_id: userId, stars });
        alert('Analytics submitted successfully!');
        updateAnalyticsSummary();
    });

    function updateAnalyticsSummary() {
        const summaryTable = document.getElementById('analyticsSummary');
        summaryTable.innerHTML = '';

        // Calculate summary data grouped by channel_id
        const summary = {};
        analyticsData.forEach(entry => {
            if (!summary[entry.channel_id]) {
                summary[entry.channel_id] = { totalStars: 0, count: 0 };
            }
            summary[entry.channel_id].totalStars += entry.stars;
            summary[entry.channel_id].count += 1;
        });

        // Populate the table with summary data
        for (const channelId in summary) {
            const { totalStars, count } = summary[channelId];
            const avgStars = (totalStars / count).toFixed(1);

            const row = document.createElement('tr');
            row.innerHTML = 
                `<td>${channelId}</td>
                <td>${avgStars}</td>
                <td>${count}</td>`;

            summaryTable.appendChild(row);
        }
    }
</script>

</body>



<!-- Add this widget at the bottom of your HTML page -->
<div id="weather-widget" style="
    position: fixed;
    bottom: 0;
    width: 100%;
    background-color: #f4f4f4;
    padding: 10px;
    box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.2);
    font-family: Arial, sans-serif;
    color: #333;
">
    <h3 style="margin: 0; text-align: center;">Weather in Denali</h3>
    <div id="weather-info" style="text-align: center; font-size: 14px;">
        Loading weather information...
    </div>
</div>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Weather Widget</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #1e1e1e;
            color: #fff;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }

        #weather-widget {
            background-color: #2e2e2e;
            border: 4px solid #39ff14; /* Neon green border */
            border-radius: 10px;
            padding: 20px;
            width: 90%;
            max-width: 400px;
            text-align: center;
            box-shadow: 0px 4px 8px rgba(0, 255, 0, 0.3);
        }

        #weather-title {
            font-size: 24px;
            margin-bottom: 15px;
            color: #39ff14;
        }

        .forecast {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: #3a3a3a;
            border-radius: 5px;
            padding: 10px;
            margin: 10px 0;
            color: #fff;
        }

        .forecast-day {
            font-weight: bold;
        }

        .forecast-temp {
            font-size: 14px;
        }

        .forecast-condition {
            font-size: 12px;
            color: #bbb;
        }

        .forecast-wind {
            font-size: 12px;
        }
    </style>
</head>
<body>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>7-Day Weather Forecast: San Diego</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #1a1a1a;
            color: #fff;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            min-height: 100vh;
            margin: 0;
        }

        .weather-widget {
            background-color: #333;
            border: 2px solid #39ff14;
            border-radius: 10px;
            padding: 20px;
            width: 300px;
            text-align: center;
        }

        .weather-widget h2 {
            color: #39ff14;
            margin-bottom: 20px;
        }

        .weather-day {
            margin: 10px 0;
            padding: 10px;
            background-color: #444;
            border-radius: 5px;
        }
    </style>
</head>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Weather Info</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #1e1e1e;
            color: #fff;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .weather-container {
            background-color: #333;
            border: 2px solid #39ff14; /* Neon green */
            border-radius: 10px;
            padding: 20px;
            text-align: center;
            width: 300px;
            box-shadow: 0 0 10px #39ff14;
        }
        .weather-container h1 {
            font-size: 1.5rem;
            margin-bottom: 10px;
        }
        .weather-container p {
            font-size: 1rem;
            margin: 5px 0;
        }
    </style>

<body>
    <div class="weather-container">
        <h1>Weather in Denali</h1>
        <p id="temperature">Temperature: Loading...</p>
        <p id="wind">Wind Speed: Loading...</p>
        <p id="direction">Wind Direction: Loading...</p>
        <p id="time">Time: Loading...</p>
        <p id="day-status">Day/Night: Loading...</p>
        <p id="weathercode">Weather Code: Loading...</p>
    </div>

    <script>
        async function fetchWeather() {
            try {
                const response = await fetch('http://127.0.0.1:8887/api/weather?location=San%20Diego&type=current');
                const data = await response.json();

                if (response.ok) {
                    const currentWeather = data.current_weather;

                    // Update the DOM with weather data
                    document.getElementById('temperature').textContent = `Temperature: ${currentWeather.temperature}°C`;
                    document.getElementById('wind').textContent = `Wind Speed: ${currentWeather.windspeed} km/h`;
                    document.getElementById('direction').textContent = `Wind Direction: ${currentWeather.winddirection}°`;
                    document.getElementById('time').textContent = `Time: ${currentWeather.time}`;
                    document.getElementById('day-status').textContent = `Day/Night: ${currentWeather.is_day ? 'Day' : 'Night'}`;
                    document.getElementById('weathercode').textContent = `Weather Code: ${currentWeather.weathercode}`;
                } else {
                    alert('Failed to fetch weather data: ' + data.error);
                }
            } catch (error) {
                console.error('Error fetching weather data:', error);
                alert('Error fetching weather data.');
            }
        }

        // Fetch weather data on page load
        fetchWeather();
    </script>
</body>
</html>
