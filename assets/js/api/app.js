// Function to get weather data from your Flask backend
async function getWeather() {
    const city = document.getElementById('city').value.trim().toLowerCase();
    
    // Make sure the city input is not empty
    if (!city) {
        alert("Please enter a city.");
        return;
    }

    // Send the request to the Flask backend API
    const url = `/api/weather/${city}`; // Assuming the backend is running on the same domain/port
    try {
        const response = await fetch(url);
        
        if (!response.ok) {
            throw new Error('Location not found or API error');
        }

        const data = await response.json();
        
        if (data.error) {
            alert(data.error);
            return;
        }

        // Update the UI with the weather data
        document.getElementById('temperature').innerText = `Temperature: ${data.temperature}°C`;
        document.getElementById('description').innerText = `Description: ${data.description}`;
        document.getElementById('humidity').innerText = `Humidity: ${data.humidity}%`;
        document.getElementById('wind').innerText = `Pressure: ${data.pressure} mb`;

    } catch (error) {
        console.error("Error fetching the weather data:", error);
        alert("An error occurred while fetching weather data.");
    }
}
