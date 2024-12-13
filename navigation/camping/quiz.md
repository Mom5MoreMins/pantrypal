<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>National Park Personality Quiz</title>
    <style>
        /* Basic page styling */
        body {
            font-family: Arial, sans-serif;
            background: #f4f4f9;
            padding: 20px;
            max-width: 800px;
            margin: auto;
        }
        h1 {
            text-align: center;
            color: #333;
        }
        .question {
            margin-bottom: 20px;
            padding: 15px;
            background: #fff;
            border: 1px solid #ccc;
            border-radius: 5px;
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
    </style>
</head>
<body>
    <h1>Which National Park Matches Your Personality?</h1>

    <!-- Quiz form with 7 questions -->
    <form id="quizForm">
        <!-- Question 1: Weather preference -->
        <div class="question">
            <label>1. What kind of weather do you prefer?</label><br>
            <input type="radio" name="q1" value="20"> Warm and sunny<br>
            <input type="radio" name="q1" value="30"> Cool and breezy<br>
            <input type="radio" name="q1" value="40"> Mild with occasional rain<br>
            <input type="radio" name="q1" value="10"> Cold and snowy<br>
        </div>

        <!-- Question 2: Terrain preference -->
        <div class="question">
            <label>2. What type of terrain are you most comfortable with?</label><br>
            <input type="radio" name="q2" value="20"> Flat plains or fields<br>
            <input type="radio" name="q2" value="30"> Rolling hills or forests<br>
            <input type="radio" name="q2" value="10"> Rocky and mountainous<br>
            <input type="radio" name="q2" value="40"> Sandy beaches<br>
        </div>

        <!-- Question 3: Water proximity preference -->
        <div class="question">
            <label>3. How close do you want to be to water?</label><br>
            <input type="radio" name="q3" value="20"> Very close – I love lakes or rivers<br>
            <input type="radio" name="q3" value="30"> Moderately close – Streams or small ponds are fine<br>
            <input type="radio" name="q3" value="10"> Not close – I’m fine without water nearby<br>
            <input type="radio" name="q3" value="40"> Oceanfront – Beaches and waves are ideal<br>
        </div>

        <!-- Question 4: Camping activities preference -->
        <div class="question">
            <label>4. What activities do you want to do while camping?</label><br>
            <input type="radio" name="q4" value="10"> Hiking and exploring<br>
            <input type="radio" name="q4" value="20"> Fishing or boating<br>
            <input type="radio" name="q4" value="30"> Relaxing and stargazing<br>
            <input type="radio" name="q4" value="40"> Swimming or surfing<br>
        </div>

        <!-- Question 5: Wildlife importance -->
        <div class="question">
            <label>5. How important is wildlife in your camping experience?</label><br>
            <input type="radio" name="q5" value="40"> Very important – I love spotting animals<br>
            <input type="radio" name="q5" value="30"> Somewhat important – It’s nice to see wildlife<br>
            <input type="radio" name="q5" value="20"> Not very important – I prefer the environment over animals<br>
            <input type="radio" name="q5" value="10"> Not important at all – I’m fine without seeing animals<br>
        </div>

        <!-- Question 6: Camping accommodation preference -->
        <div class="question">
            <label>6. What type of camping accommodations do you prefer?</label><br>
            <input type="radio" name="q6" value="10"> Tent camping – I like the full outdoor experience<br>
            <input type="radio" name="q6" value="20"> RV camping – I want some comforts of home<br>
            <input type="radio" name="q6" value="30"> Glamping – I love luxury and convenience<br>
            <input type="radio" name="q6" value="40"> Beach camping – Nothing beats camping by the waves<br>
        </div>

        <!-- Question 7: Preferred wildlife -->
        <div class="question">
            <label>7. What kind of wildlife are you most interested in seeing?</label><br>
            <input type="radio" name="q7" value="10"> Large mammals like bears or elk<br>
            <input type="radio" name="q7" value="40"> Aquatic animals like fish or coral<br>
            <input type="radio" name="q7" value="30"> Birds or smaller creatures<br>
            <input type="radio" name="q7" value="20"> Not interested – I’d rather focus on the landscapes<br>
        </div>

        <!-- Submit button -->
        <button type="button" onclick="submitQuiz()">Submit Quiz</button>
    </form>

    <p id="result"></p>

    <script>
        // Submit the quiz results to the backend
        async function submitQuiz() {
            const formData = new FormData(document.getElementById("quizForm"));
            let points = 0;

            for (let [key, value] of formData.entries()) {
                points += parseInt(value);
            }

            // Send points to the backend API
            const response = await fetch('http://localhost:5000/api/quiz', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ points })
            });

            const result = await response.json();
            document.getElementById("result").innerText = `You matched with: ${result.park}\nYou have access to: ${result.channels.join(', ')}`;
        }
    </script>
</body>
</html>
