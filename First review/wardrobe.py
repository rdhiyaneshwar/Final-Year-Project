import requests
import random

API_KEY = '1c3cd4d05f6949ac20ef50c13f8e91d9'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def get_weather(lat, lon):
    """Fetch weather data from OpenWeatherMap API."""
    params = {
        'lat': lat,
        'lon': lon,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Error fetching weather data")

def suggest_dress(weather_data):
    """Suggest a dress based on the current weather conditions."""
    weather_main = weather_data['weather'][0]['main'].lower()
    
    dresses = {
        'clear': [
            'A light summer dress with floral patterns.',
            'A casual tank top and shorts.'
        ],
        'clouds': [
            'A comfortable sweater with jeans.',
            'A light jacket over a casual shirt.'
        ],
        'rain': [
            'A waterproof raincoat and waterproof boots.',
            'An umbrella and a cozy hoodie.'
        ],
        'snow': [
            'A warm winter coat and snow boots.',
            'A thermal sweater with insulated pants.'
        ],
        'drizzle': [
            'A light rain jacket and comfortable shoes.',
            'An umbrella with a casual outfit.'
        ],
        'thunderstorm': [
            'A heavy raincoat and durable boots.',
            'Protective gear and a warm sweater.'
        ]
    }
    
    for condition, suggestions in dresses.items():
        if condition in weather_main:
            return random.choice(suggestions)
    
    return random.choice(sum(dresses.values(), []))

def main():
    lat = input("Enter latitude: ")
    lon = input("Enter longitude: ")
    
    try:
        weather_data = get_weather(lat, lon)
        dress_suggestion = suggest_dress(weather_data)
        print(f"Weather Description: {weather_data['weather'][0]['description']}")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Suggested Dress: {dress_suggestion}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
