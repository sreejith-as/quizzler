"""Fetches quiz question data from the Open Trivia Database API."""

import requests

# Define API parameters for quiz questions
parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 18,  # Science: Computers
}

# Make a GET request to the Open Trivia DB API
response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()

# Extract only the list of questions
question_data = data["results"]
