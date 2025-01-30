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

**Subdomain** To ensure that the frontend can communicate with the backend during development, we configure Cross-Origin Resource Sharing (CORS). Since the frontend and backend are running on different ports, we need to explicitly allow the frontend to make requests to the backend. CORS Configuration in Flask: The Flask backend is configured to allow requests from the frontend port (127.0.0.1:4887). This ensures that the browser doesn’t block the API requests due to cross-origin restrictions.



 