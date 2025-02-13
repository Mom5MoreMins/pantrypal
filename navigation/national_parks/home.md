---
layout: post 
title: National Parks
search_exclude: False
permalink: /national_parks/home
menu: nav/national_parks.html
---

Welcome to the National Parks showcase! Enjoy exploring the beauty of nature.

<style>
/* Styling for the National Parks page */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    text-align: center;
}

h1 {
    color: #2E8B57;
    font-size: 2.5em;
    margin-bottom: 10px;
}

h2 {
    color: #4682B4;
    font-size: 1.8em;
    margin-bottom: 20px;
}

.grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
    justify-items: center;
    margin: 20px 0;
}

.grid img {
    width: 100%;
    max-width: 300px;
    border-radius: 10px;
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
}

.bar {
    background-color: #4682B4;
    color: white;
    padding: 10px;
    border-radius: 5px;
    margin-bottom: 20px;
    font-size: 1.2em;
    font-weight: bold;
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
