---
layout: post
title: Deployment Blog
description: Team Frostbyte Deployment Blog
menu: nav/about.html
permalink: /about/deployment
author: Risha, Aranya, Abby, Ava, Elliot, Shriya
comments: true
---

## DEPLOYMENT BLOG

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Carousel</title>
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
</head>
<body>

<div class="carousel-container">
<img src="../../images/risha frontend.png" class="carousel-item" onclick="openFullscreen(this.src)">
<img src="../../images/risha code.png" class="carousel-item" onclick="openFullscreen(this.src)">
<div class="text-item">RISHA</div>
<img src="../../images/shriya frontend.png" class="carousel-item" onclick="openFullscreen(this.src)">
<img src="../../images/shriya code.png" class="carousel-item" onclick="openFullscreen(this.src)">
<div class="text-item">SHRIYA</div>
<img src="../../images/ava frontend.png" class="carousel-item" onclick="openFullscreen(this.src)">
<img src="../../images/ava code.png" class="carousel-item" onclick="openFullscreen(this.src)">
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



https://nighthawkcoders.github.io/portfolio_2025/csp/sprint5/objectives

link from slack he wants us to read https://nighthawkcoders.github.io/portfolio_2025/2024/12/03/aws-deployment_IPYNB_2_.html#pulling-changes-into-aws-ec2-deployment

 

 