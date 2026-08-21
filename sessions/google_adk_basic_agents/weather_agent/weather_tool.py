import requests

ACCESS_KEY = "8ce89013be4bf72c73a81bb457e9eb3d"


def get_current_weather(location: str) -> dict:
    """Fetches the current weather information for a given location using the Weatherstack API.
    
    Args:
        location: The name of the city or location to retrieve weather data for (e.g., 'London', 'New York').

    Returns:
        A dictionary containing the current weather information for the specified location.
    """
    url = f'https://api.weatherstack.com/current?access_key={ACCESS_KEY}&query={location}'
    headers = {
        'Accept': 'application/json'
    }
    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return {}
