---
layout: post 
title: About Our Team
search_exclude: true
menu: nav/about.html
permalink: /about/home
---
<style>
    body {
        font-family: Arial, sans-serif;
        margin: 20px;
        background-color: #f9f9f9;
    }
    h1 {
        text-align: center;
        color: #333;
    }
    .table-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 20px;
    }
    .table-wrapper {
        background: #fff;
        border: 1px solid #ddd;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        border-radius: 8px;
        overflow: hidden;
        width: 300px;
        display: flex;
        flex-direction: column;
        justify-content: flex-start; /* Align content to the top */
    }
    table {
        width: 100%;
        border-collapse: collapse;
    }
    th, td {
        text-align: left;
        padding: 8px 12px;
        border-bottom: 1px solid #ddd;
        word-wrap: break-word; /* Ensure long text breaks into new lines */
    }
    th {
        background-color: #f4f4f4;
        font-weight: bold;
    }
    td {
        background-color: #fff;
    }
    /* Ensures consistent height across all .table-wrapper */
    .table-container {
        align-items: stretch; /* Ensures all items match the tallest one */
    }
</style>

<div class="table-container" id="tableContainer">
    <!-- Tables will be dynamically injected here -->
</div>

<script>
    // Fetch data from Flask API
    const apiUrl = 'http://127.0.0.1:8887/api/data';

    fetch(apiUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            // Get the table container
            const container = document.getElementById('tableContainer');

            // Loop through each user's data to create tables
            data.forEach((user, index) => {
                // Create a wrapper div for each table
                const tableWrapper = document.createElement('div');
                tableWrapper.className = 'table-wrapper';

                // Create a table element
                const table = document.createElement('table');
                table.innerHTML = `
                    <thead>
                        <tr>
                            <th colspan="2">User ${index + 1}: ${user.FirstName} ${user.LastName}</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Favorite Color</td>
                            <td>${user.FavoriteColor || user.Favorite_Color || 'N/A'}</td>
                        </tr>
                        <tr>
                            <td>Favorite Fruit</td>
                            <td>${user.FavoriteFruit || user.Favorite_Fruit || 'N/A'}</td>
                        </tr>
                        <tr>
                            <td>Favorite Sport</td>
                            <td>${user.FavoriteSport || 'N/A'}</td>
                        </tr>
                        <tr>
                            <td>Hobbies</td>
                            <td>${(user.Hobbies || []).join(', ')}</td>
                        </tr>
                    </tbody>
                `;

                // Append the table to the wrapper
                tableWrapper.appendChild(table);

                // Append the wrapper to the container
                container.appendChild(tableWrapper);
            });
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
</script>


<h3> Planning and Personal Contribution Video </h3>

<iframe width="560" height="315" src="{{site.baseurl}}/images/videos/frostbyte_vid.mp4" 
title="Frostbyte video player" frameborder="0" allow="accelerometer; autoplay; 
clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Team Challenges</title>
</head>
<body>
    <h2>Team Challenges</h2>
    <p>In the process of creating our social media site, we faced many challenges.</p>
    <h3>1. Lack of Communication</h3>
    <ul>
        <li>To overcome this challenge, we held several meetings and discussed issues in our code during class.</li>
        <li>We frequently used Slack to communicate and inform each other when to pull, preventing merge errors.</li>
        <li>The Live Share feature on VSCode allowed us to collaborate effectively, even with overlapping work.</li>
    </ul>
    <h3>2. Organization Difficulties</h3>
    <ul>
        <li>With six people working together, organization was not easy.</li>
        <li>A Kanban board helped us track progress and view pending tasks.</li>
        <li>Personal burndown lists allowed us to check the next steps for our individual features.</li>
    </ul>
    <h3>3. Code Issues and Errors</h3>
    <ul>
        <li>We collaborated to ensure correct formatting and sought help from the coding tutoring club.</li>
        <li>We formed groups with members working on similar features to troubleshoot problems together.</li>
        <li>We tested our functions on different computers to improve the overall user experience.</li>
    </ul>
</body>
</html>
