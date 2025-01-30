---
layout: post
title: Deployment Blog
description: Team Frostbyte Deployment Blog
menu: nav/about.html
permalink: /about/deployment
author: Risha, Aranya, Abby, Ava, Elliot, Shriya
comments: true
---
<style>
        .carousel-container {
            display: flex;
            overflow-x: auto;
            gap: 20px;
            padding: 10px;
            white-space: nowrap;
            scroll-snap-type: x mandatory;
        }
        .carousel-item {
            width: 150px;
            height: 150px;
            object-fit: cover;
            cursor: pointer;
            border-radius: 10px;
            scroll-snap-align: center;
        }
        .text-item {
            font-size: 24px;
            font-weight: bold;
            display: flex;
            align-items: center;
            justify-content: center;
            width: 150px;
            height: 150px;
        }
        .fullscreen-container {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.8);
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 1000;
        }
        .fullscreen-container img {
            max-width: 90%;
            max-height: 90%;
            border-radius: 10px;
        }
</style>


<img src="{{ site.baseurl }}/images/deployment_page/Frostbyte_Deployment_Diagram.png" alt="Backend Diagram">

<div class="carousel-container">
<img src="images/risha frontend.png" class="carousel-item" onclick="openFullscreen(this.src)">
<img src="images/risha code.png" class="carousel-item" onclick="openFullscreen(this.src)">
<div class="text-item">RISHA</div>
<img src="images/shriya frontend.png" class="carousel-item" onclick="openFullscreen(this.src)">
<img src="images/shriya code.png" class="carousel-item" onclick="openFullscreen(this.src)">
<div class="text-item">SHRIYA</div>
<img src="images/ava frontend.png" class="carousel-item" onclick="openFullscreen(this.src)">
<img src="images/ava code.png" class="carousel-item" onclick="openFullscreen(this.src)">
<div class="text-item">AVA</div>

</div>

<!-- Fullscreen Image Container -->
<div id="fullscreen-view" class="fullscreen-container" style="display: none;" onclick="closeFullscreen()">
    <img id="fullscreen-img" src="" alt="">
</div>

<script>
    function openFullscreen(src) {
        document.getElementById("fullscreen-img").src = src;
        document.getElementById("fullscreen-view").style.display = "flex";
    }

    function closeFullscreen() {
        document.getElementById("fullscreen-view").style.display = "none";
    }
</script>

</body>
</html>

Our project is structured to provide a seamless integration between the frontend and backend. Below is an outline of the current repository setup, including subdomains, and frontend/backend port configuration.

**Backend:** Our backend repository is Flask based and runs on the port 8887 which is used for API requests and is the port we use to test it in postman. It is responsible for processing data, interactign with the database, and sending responses to frontend (JSON). The backend contains each of our APIs under the folder .py which all work through our main.py. Each of our APIs has a corresponding model under the model folder.

**Frontend:** Our frontend communicates the backend through RESTful APIs. The frontend runs on 4887 and sends HTTP requests to the backend. Our frontend is configured to fetch data from backend, process user data, then display it. The frontend 4887 sends API requests to the backend 8887. The backend processes the request, and interacts with the database. The frontend then updates the user interface based on the request.

**How our Features Interact with the Frontend and Backend**
- REVIEW FEATURE: The backend API handles CRUD operations for the Review model, allowing users to create, read, update, and delete reviews through routes like /api/review. The frontend interacts with these endpoints by sending HTTP requests, such as POST for creating reviews and GET for fetching them, often passing a JWT token for authentication. The backend processes these requests, interacting with the database via SQLAlchemy and returning relevant data to the frontend.

- GEMINI API: The Gemini API integrates with Google Generative AI to provide a chatbot that generates camping-related advice based on user inputs. When a user sends a message, the backend uses the AI model to generate a response, updates the conversation history, and stores both the user input and AI response in the database. The backend supports CRUD operations, allowing users to interact with the chatbot, update messages, and delete them via HTTP requests, while maintaining a persistent chat session.

- LOCATION API: The Location API allows the frontend to manage user-specific location data, including storing, retrieving, and deleting location information linked to users and channels. It provides endpoints for creating and updating locations, fetching a user's location by their ID and channel, and deleting specific location records by ID. The backend uses SQLAlchemy to interact with the Location model, which stores location data in the database and ensures that each user's location is properly tracked, while utilizing JWT token-based authentication.

- ANALYTICS API: The Analytics API allows the frontend to send and retrieve analytics data related to user reviews, such as star ratings for specific channels. Users can submit individual or bulk analytics entries, which are stored in the database, while the frontend can also request an overall summary of average ratings and review counts for each channel. The backend ensures proper validation and error handling for all requests, and provides CRUD operations for managing analytics data, which is stored in the Analytics model and can be queried for reporting purposes.

- POST API: The Post API allows the frontend to create, update, retrieve, and delete posts associated with specific channels and users. The backend handles these requests by interacting with the Post model, which is stored in a SQL database using SQLAlchemy, ensuring each post has a title, comment, content, and references to the user and channel. Through CRUD operations, the frontend can send requests to create posts, view individual or multiple posts, or delete posts, with responses being returned in JSON format for seamless integration with the frontend interface.

**Subdomain** To ensure that the frontend can communicate with the backend during development, we configure Cross-Origin Resource Sharing (CORS). Since the frontend and backend are running on different ports, we need to explicitly allow the frontend to make requests to the backend. CORS Configuration in Flask: The Flask backend is configured to allow requests from the frontend port (127.0.0.1:4887). This ensures that the browser doesn’t block the API requests due to cross-origin restrictions.



 