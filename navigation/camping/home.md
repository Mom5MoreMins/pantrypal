---
layout: post
title: Camping Homepage
search_exclude: true
permalink: /camping/home
menu: nav/camping.html
---

<style>
    body {
        font-family: 'Poppins', sans-serif;
        background-color: #63c752;
        color: #e0e0e0;
        padding: 20px;
    }

    h1, h2, h3 {
        color: #00d4ff;
        margin-bottom: 15px;
        text-align: center;
    }

    p {
        margin-bottom: 15px;
        text-align: center;
    }

    .feature-overview {
        margin: 20px auto;
        max-width: 800px;
        text-align: center;
    }

    .slideshow-container {
        position: relative;
        margin: 20px auto;
        max-width: 800px;
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }

    .slides {
        display: none;
        width: 100%;
        height: 400px;
    }

    .slides img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        cursor: pointer;
    }

    .prev, .next {
        position: absolute;
        top: 50%;
        transform: translateY(-50%);
        background-color: rgba(0, 0, 0, 0.5);
        color: #fff;
        border: none;
        padding: 10px 20px;
        cursor: pointer;
        z-index: 10;
        border-radius: 5px;
    }

    .prev {
        left: 10px;
    }

    .next {
        right: 10px;
    }

    .dot-container {
        text-align: center;
        margin-top: 15px;
    }

    .dot {
        display: inline-block;
        width: 15px;
        height: 15px;
        margin: 5px;
        background-color: #ccc;
        border-radius: 50%;
        cursor: pointer;
    }

    .dot.active {
        background-color: #00d4ff;
    }

    .fullscreen {
        display: none;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.9);
        z-index: 100;
        justify-content: center;
        align-items: center;
    }

    .fullscreen img {
        max-width: 90%;
        max-height: 90%;
    }

    .close-btn {
        position: absolute;
        top: 20px;
        right: 20px;
        background-color: #fff;
        color: #000;
        border: none;
        padding: 10px;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1.2rem;
    }
</style>

<h1>Welcome to the Camping Homepage!</h1>

<div class="feature-overview">
    <h2>Discover Your Next Adventure</h2>
    <p>Explore the best camping destinations across stunning national parks.</p>
    <p>Learn tips and tricks for camping, connect with other adventurers, and share your experiences.</p>
</div>

<div class="slideshow-container">
    <div class="slides">
        <img src="https://media.cntraveler.com/photos/5f15ca3da107fd1a0223dde7/1:1/w_2634,h_2634,c_limit/DenaliNationalPark-Alaska-2020-GettyImages-628618916.jpg" alt="Denali National Park" onclick="openFullscreen(this)">
    </div>
    <div class="slides">
        <img src="https://encrypted-tbn3.gstatic.com/licensed-image?q=tbn:ANd9GcQe8po_i_zHqgTQ9LLpCFB9vArUZ1_BrBM60VTKFmk2yhghJadINiobzOE1BJJzndll2TsGbkk08QVlt1D5aVdQOGIkEjce5ThX0128RA" alt="Grand Canyon National Park" onclick="openFullscreen(this)">
    </div>
    <div class="slides">
        <img src="https://media.cntraveler.com/photos/641366bd693167e7802a8bf2/1:1/w_4000,h_4000,c_limit/Redwood%20National%20Park_GettyImages-1079164438.jpg" alt="Redwood National Park" onclick="openFullscreen(this)">
    </div>
    <div class="slides">
        <img src="https://www.nps.gov/articles/000/images/BUIS-corsaut-873x0425.jpg" alt="Buck Island Reef National Monument" onclick="openFullscreen(this)">
    </div>

    <button class="prev" onclick="plusSlides(-1)">&#10094;</button>
    <button class="next" onclick="plusSlides(1)">&#10095;</button>
</div>

<div class="dot-container">
    <span class="dot" onclick="currentSlide(1)"></span>
    <span class="dot" onclick="currentSlide(2)"></span>
    <span class="dot" onclick="currentSlide(3)"></span>
    <span class="dot" onclick="currentSlide(4)"></span>
</div>

<div class="fullscreen" id="fullscreen">
    <button class="close-btn" onclick="closeFullscreen()">&#10006;</button>
    <img id="fullscreenImage" src="" alt="Fullscreen Image">
</div>

<script>
    let slideIndex = 0;
    showSlides(slideIndex);

    function plusSlides(n) {
        showSlides(slideIndex += n);
    }

    function currentSlide(n) {
        showSlides(slideIndex = n - 1);
    }

    function showSlides(n) {
        const slides = document.querySelectorAll('.slides');
        const dots = document.querySelectorAll('.dot');
        if (n >= slides.length) slideIndex = 0;
        if (n < 0) slideIndex = slides.length - 1;
        slides.forEach(slide => slide.style.display = 'none');
        dots.forEach(dot => dot.classList.remove('active'));
        slides[slideIndex].style.display = 'block';
        dots[slideIndex].classList.add('active');
    }

    function openFullscreen(image) {
        const fullscreen = document.getElementById('fullscreen');
        const fullscreenImage = document.getElementById('fullscreenImage');
        fullscreenImage.src = image.src;
        fullscreen.style.display = 'flex';
    }

    function closeFullscreen() {
        const fullscreen = document.getElementById('fullscreen');
        fullscreen.style.display = 'none';
    }

    // Auto slide every 5 seconds
    setInterval(() => plusSlides(1), 5000);
</script>
