---
layout: post
title: Camping Home
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
    }

    .slides img {
        width: 100%;
        border-radius: 10px;
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
</style>

<h1>Welcome to the World of National Parks!</h1>

<div class="feature-overview">
    <h2>Explore the Features</h2>
    <p>Take a personality quiz to find your ideal national park.</p>
    <p>Get camping tips, join discussions, and connect with other adventurers.</p>
    <p>Rate and review parks after your visit and share your experiences.</p>
</div>

<div class="slideshow-container">
    <div class="slides">
        <img src="https://media.cntraveler.com/photos/5f15ca3da107fd1a0223dde7/1:1/w_2634,h_2634,c_limit/DenaliNationalPark-Alaska-2020-GettyImages-628618916.jpg" alt="National Park 1">
    </div>
    <div class="slides">
        <img src="https://example.com/park2.jpg" alt="National Park 2">
    </div>
    <div class="slides">
        <img src="https://example.com/park3.jpg" alt="National Park 3">
    </div>

    <button class="prev" onclick="plusSlides(-1)">&#10094;</button>
    <button class="next" onclick="plusSlides(1)">&#10095;</button>
</div>

<div class="dot-container">
    <span class="dot" onclick="currentSlide(1)"></span>
    <span class="dot" onclick="currentSlide(2)"></span>
    <span class="dot" onclick="currentSlide(3)"></span>
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

    // Auto slide every 5 seconds
    setInterval(() => plusSlides(1), 5000);
</script>
