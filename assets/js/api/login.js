import { pythonURI, fetchOptions } from './config.js';

console.log("login.js loaded");

document.addEventListener('DOMContentLoaded', function() {
    const baseurl = document.querySelector('.trigger').getAttribute('data-baseurl');
    console.log("Base URL:", baseurl); // Debugging line
    getCredentials(baseurl) // Call the function to get credentials
        .then(data => {
            console.log("Credentials data:", data); // Debugging line
            const loginArea = document.getElementById('loginArea');
            if (data) { // Update the login area based on the data
                // User is authenticated, replace "Login" with User's name
                loginArea.innerHTML = `
                    <div class="dropdown">
                        <button class="dropbtn">${data.name}</button>
                        <div class="dropdown-content">
                            <a href="${baseurl}/logout">Logout</a>
                            <a href="${baseurl}/profile">Profile</a>
                            <a href="${baseurl}/analytics">Analytics</a>
                        </div>
                    </div>
                `;
                localStorage.setItem('uid', data.uid);
            } else {
                // User is not authenticated, then "Login" link is shown
                loginArea.innerHTML = `<a href="${baseurl}/login">Login</a>`;
            }
        })
        .catch(err => { // General error handler
            console.error("Error fetching credentials: ", err);
            // Handle any errors that occurred during getCredentials
        });
});

function getCredentials(baseurl) {
    const URL = pythonURI + '/api/id';
    return fetch(URL, fetchOptions)
        .then(response => { // API response handler 
            if (response.status !== 200) {
                console.error("HTTP status code: " + response.status);
                return null; // prepares to stop the chain by returning null.
            }
            return response.json(); // plans to continue the chain with the data.
        })
        .then(data => { // Data handler from the previous promise  
            if (data === null) return null; // stops the chain, returns null.
            console.log(data); // logs data with should contain uid, name, etc.
            return data; // returns data to caller 
        })
        .catch(err => { // General error handler
            console.error("Fetch error: ", err);
            return null;
        });
}