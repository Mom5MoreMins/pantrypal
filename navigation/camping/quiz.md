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
        body {
            font-family: Arial, sans-serif;
            background: #f4f4f9;
            padding: 20px;
            max-width: 800px;
            margin: auto;
            color: #000; /* Text color set to black */
        }
        h1 {
            text-align: center;
            color: #000; /* Text color set to black */
        }
        .question {
            margin-bottom: 20px;
            padding: 15px;
            background: #fff; /* White background for questions */
            border: 1px solid #ccc;
            border-radius: 5px;
            color: #000; /* Text color set to black */
        }
        label {
            color: #000; /* Text color set to black */
            font-size: 16px;
            line-height: 1.5;
        }

        input[type="radio"] {
            margin-right: 10px;
        }

        button {
            background: #5cb85c;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background: #4cae4c;
        }
        #result {
            font-size: 18px;
            color: #000; /* Text color set to black */
            font-weight: bold;
            margin-top: 20px;
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

        <button type="button" onclick="submitQuiz()">Submit Quiz</button>
    </form>

    <p id="result"></p>

    <script>
        async function submitQuiz() {
            const formData = new FormData(document.getElementById("quizForm"));
            let points = 0;

            for (let [key, value] of formData.entries()) {
                points += parseInt(value);
            }

            document.getElementById("result").innerText = `You scored ${points} points.`;
        }
    </script>
</body>
</html>
