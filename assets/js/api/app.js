// Function to get weather details when the user clicks the button
function getWeather() {
    const city = document.getElementById('city').value.trim();

    // Check if the city input is empty
    if (!city) {
        alert("Please enter a city.");
        return;
    }

    // Make a request to the backend weather API using fetch
    fetch(`http://localhost:8102/api/weather/${city}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            // Add authorization if needed, like the token:
            // 'Authorization': `Bearer <your_token_here>`
        }
    })
    .then(response => response.json())
    .then(data => {
        // If there's an error in the response, display an alert
        if (data.error) {
            alert(data.error);
            return;
        }

        // Otherwise, display the weather data in the UI
        document.getElementById('temperature').textContent = `Temperature: ${data.temperature}°C`;
        document.getElementById('description').textContent = `Description: ${data.description}`;
        document.getElementById('humidity').textContent = `Humidity: ${data.humidity}%`;
        document.getElementById('wind').textContent = `Wind Speed: ${data.wind_speed || 'N/A'} km/h`;
    })
    .catch(error => {
        console.error("Error fetching weather data:", error);
        alert("There was an issue fetching the weather data.");
    });
}
