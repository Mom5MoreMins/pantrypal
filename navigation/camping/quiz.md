---
layout: post
title: Camping Quiz
search_exclude: true
permalink: /camping/quiz
menu: nav/camping.html
---
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>National Park Personality Quiz</title>
    <style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

/* Fix for the Main Navigation Bar */
#main-nav {
    position: relative !important; /* Prevents it from staying fixed */
    width: 100%;
    top: 0;
    background: #3e7b52; /* Rich green */
    z-index: 1000; /* Keeps it above other elements */
    padding: 15px 0;
}

#secondary-nav {
    position: relative; /* Ensures it behaves normally */
    width: 100%;
    background: #a5a35f; /* Lighter green */
    padding: 10px 0;
}

/* General Page Styles */
body {
    font-family: 'Poppins', sans-serif;
    background: linear-gradient(to bottom, #3f622e, #a5a35f); /* Green gradient */
    color: #2e2e2e;
    margin: 0;
    padding: 20px;
}

h1 {
    text-align: center;
    font-size: 2.5rem;
    color: #2e4d28; /* Dark green */
}

/* Quiz Question Styling */
.question {
    background-color: #5a483c; /* Darker earthy brown */
    border: 3px solid #7d6b5f; /* Muted brown */
    border-radius: 12px;
    max-width: 800px;
    padding: 25px;
    margin: 20px auto;
    font-size: 1.2rem;
}

.question label {
    color: #f8f4e3; /* Light beige for contrast */
    font-weight: 600;
}

/* Radio Button Styling */
input[type="radio"] {
    margin-right: 12px;
    transform: scale(1.2); /* Make radio buttons larger */
}

/* Button Styling */
button {
    background: #3e7b52; /* Rich green */
    color: #fff;
    padding: 12px 24px;
    border: none;
    border-radius: 8px;
    font-size: 1.2rem;
    cursor: pointer;
    transition: background 0.3s ease, transform 0.2s ease;
    display: block;
    margin: 30px auto;
    font-weight: 600;
}

button:hover {
    background: #285437; /* Darker green */
    transform: scale(1.05);
}

/* Quiz Result Styling */
#result {
    font-size: 1.5rem;
    color: #3e7b52;
    font-weight: bold;
    text-align: center;
    margin-top: 25px;
}

    </style>
</head>
<body>
    <h1>Which National Park Matches Your Personality?</h1>
    <form id="quizForm">
        <div class="question">
            <label>1. What kind of weather do you prefer?</label><br>
            <input type="radio" name="q1" value="20"> Warm and sunny (20 points)<br>
            <input type="radio" name="q1" value="30"> Cool and breezy (30 points)<br>
            <input type="radio" name="q1" value="40"> Mild with occasional rain (40 points)<br>
            <input type="radio" name="q1" value="10"> Cold and snowy (10 points)<br>
        </div>
        <div class="question">
            <label>2. What type of terrain are you most comfortable with?</label><br>
            <input type="radio" name="q2" value="20"> Flat plains or fields (20 points)<br>
            <input type="radio" name="q2" value="30"> Rolling hills or forests (30 points)<br>
            <input type="radio" name="q2" value="10"> Rocky and mountainous (10 points)<br>
            <input type="radio" name="q2" value="40"> Sandy beaches (40 points)<br>
        </div>
        <div class="question">
            <label>3. How close do you want to be to water?</label><br>
            <input type="radio" name="q3" value="20"> Very close – I love lakes or rivers (20 points)<br>
            <input type="radio" name="q3" value="30"> Moderately close – Streams or small ponds are fine (30 points)<br>
            <input type="radio" name="q3" value="10"> Not close – I’m fine without water nearby (10 points)<br>
            <input type="radio" name="q3" value="40"> Oceanfront – Beaches and waves are ideal (40 points)<br>
        </div>
        <div class="question">
            <label>4. What activities do you want to do while camping?</label><br>
            <input type="radio" name="q4" value="10"> Hiking and exploring (10 points)<br>
            <input type="radio" name="q4" value="20"> Fishing or boating (20 points)<br>
            <input type="radio" name="q4" value="30"> Relaxing and stargazing (30 points)<br>
            <input type="radio" name="q4" value="40"> Swimming or surfing (40 points)<br>
        </div>
        <div class="question">
            <label>5. How important is wildlife in your camping experience?</label><br>
            <input type="radio" name="q5" value="40"> Very important – I love spotting animals (40 points)<br>
            <input type="radio" name="q5" value="30"> Somewhat important – It’s nice to see wildlife (30 points)<br>
            <input type="radio" name="q5" value="20"> Not very important – I prefer the environment over animals (20 points)<br>
            <input type="radio" name="q5" value="10"> Not important at all – I’m fine without seeing animals (10 points)<br>
        </div>
        <div class="question">
            <label>6. What type of camping accommodations do you prefer?</label><br>
            <input type="radio" name="q6" value="10"> Tent camping – I like the full outdoor experience (10 points)<br>
            <input type="radio" name="q6" value="20"> RV camping – I want some comforts of home (20 points)<br>
            <input type="radio" name="q6" value="30"> Glamping – I love luxury and convenience (30 points)<br>
            <input type="radio" name="q6" value="40"> Beach camping – Nothing beats camping by the waves (40 points)<br>
        </div>
        <div class="question">
            <label>7. What kind of wildlife are you most interested in seeing?</label><br>
            <input type="radio" name="q7" value="10"> Large mammals like bears or elk (10 points)<br>
            <input type="radio" name="q7" value="40"> Aquatic animals like fish or coral (40 points)<br>
            <input type="radio" name="q7" value="30"> Birds or smaller creatures (30 points)<br>
            <input type="radio" name="q7" value="20"> Not interested – I’d rather focus on the landscapes (20 points)<br>
        </div>
 <button type="button" id="submitQuizBtn">Submit Quiz</button>
 <button id="deleteQuizBtn">Delete Quiz Result</button>
</form>
<p id="result"></p>
</body>

<script type="module">
    import { pythonURI, fetchOptions } from '{{ site.baseurl }}/assets/js/api/config.js';

    function calculateTotalPoints() {
        let total_points = 0;
        const questions = document.querySelectorAll("form .question");

        questions.forEach(question => {
            const selectedOption = question.querySelector("input[type='radio']:checked");
            if (selectedOption) {
                total_points += parseInt(selectedOption.value, 10);
            }
        });

        return total_points;
    }

    function submitQuiz() {
        const total_points = calculateTotalPoints(); // Call the function to get total points

        fetch(`${pythonURI}/api/quiz/`, {
            ...fetchOptions,  // Use predefined fetch options
            method: "POST",
            body: JSON.stringify({ total_points: total_points })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            document.getElementById("result").innerText = 
                `✅ Quiz Submitted Successfully!\nTotal Points: ${total_points}\nAssigned Park: ${data.assigned_park || "Unknown"}`;
        })
        .catch(error => {
            document.getElementById("result").innerText = 
                `❌ Error submitting quiz: ${error.message}`;
            console.error("Request failed:", error);
        });
    }

    // Attach the submit function to the button
    document.getElementById("submitQuizBtn").addEventListener("click", submitQuiz);
</script>

<script type="module">
    import { pythonURI, fetchOptions } from '{{ site.baseurl }}/assets/js/api/config.js';

    async function deleteLatestQuizResult() {
        try {
            const response = await fetch(`${pythonURI}/api/quiz/`, {
                ...fetchOptions,
                method: "DELETE"
            });

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const data = await response.json();
            document.getElementById("result").innerText = 
                `🗑️ ${data.message}`;
            console.log("Quiz result deleted:", data);

        } catch (error) {
            document.getElementById("result").innerText = 
                `❌ Error deleting quiz result: ${error.message}`;
            console.error("Request failed:", error);
        }
    }

    // Attach event listener to the delete button
    document.getElementById("deleteQuizBtn").addEventListener("click", deleteLatestQuizResult);
</script>
