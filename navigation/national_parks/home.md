---
layout: post 
title: National Parks
search_exclude: False
permalink: /national_parks/home
menu: nav/national_parks.html
---

Welcome to the National Parks showcase! Enjoy exploring the beauty of nature.

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
/* Styling for the National Parks page */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    text-align: center;
}

h1 {
    font-family: "Poppins", sans-serif;
    color: #2E8B57;
    font-size: 2.5em;
    margin-bottom: 10px;
}

h2 {
    font-family: "Poppins", sans-serif;
    color: #4682B4;
    font-size: 1.8em;
    margin-bottom: 20px;
}

/* Assigned Park Bar */
.bar {
    background: linear-gradient(to right, #4682B4, #2E8B57);
    color: white;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 20px;
    font-size: 1.3em;
    font-weight: bold;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    max-width: 600px;
    margin: auto;
}

/* Responsive Grid Layout */
.grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(250px, 1fr));
    gap: 20px;
    justify-items: center;
    margin: 20px auto;
    max-width: 900px;
}

/* Image Styling */
.grid img {
    width: 100%;
    max-width: 350px;
    border-radius: 12px;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.15);
    transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
}

/* Hover Effect on Images */
.grid img:hover {
    transform: scale(1.05);
    box-shadow: 0px 6px 14px rgba(0, 0, 0, 0.25);
    cursor: pointer;
}
</style>

<!-- Assigned Park Message -->
<div class="bar" id="assignedPark">Your assigned national park is: Loading...</div>

<!-- National Park Images -->
<div class="grid">
    <img src="{{ site.baseurl }}/images/NationalParkImages/reeef.jpg" alt="Park 1">
    <img src="{{ site.baseurl }}/images/NationalParkImages/Pic1.jpg" alt="Park 2">
    <img src="{{ site.baseurl }}/images/NationalParkImages/redwood.webp" alt="Park 3">
    <img src="{{ site.baseurl }}/images/NationalParkImages/amazing.webp" alt="Park 4">
</div>

<!-- Fetch Quiz Results and Display Assigned Park -->
<script type="module">
    import { pythonURI, fetchOptions } from '{{ site.baseurl }}/assets/js/api/config.js';

    async function fetchAssignedPark() {
        try {
            console.log("Fetching assigned park...");

            const response = await fetch(`${pythonURI}/api/quiz/`, {
                ...fetchOptions,
                method: "GET"
            });

            if (!response.ok) {
                if (response.status === 404) {
                    console.warn("No quiz results found.");
                    document.getElementById("assignedPark").innerText = 
                        "Your assigned national park is: Take Quiz";
                    return;
                }
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const data = await response.json();
            console.log("Quiz API Response:", data); // Debugging API response

            // Get assigned park or fallback to "Take Quiz"
            const assignedPark = data.assigned_park || "Take Quiz";

            // Update the UI (Modify Bar)
            const assignedParkElement = document.getElementById("assignedPark");
            assignedParkElement.innerText = `Your assigned national park is: ${assignedPark}`;

        } catch (error) {
            console.error("Error fetching quiz results:", error);
            document.getElementById("assignedPark").innerText = 
                "Your assigned national park is: Take Quiz";
        }
    }

    // Run function when the page loads
    document.addEventListener("DOMContentLoaded", fetchAssignedPark);
</script>
