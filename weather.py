import os
import sys
import requests

API_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city: str, api_key: str):
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
        "lang": "zh_cn"
    }
    response = requests.get(API_URL, params=params, timeout=10)
    response.raise_for_status()
    return response.json()

def main():
    if len(sys.argv) < 2:
        print("Usage: python weather.py CITY_NAME")
        sys.exit(1)
    city = sys.argv[1]
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        print("Error: OPENWEATHER_API_KEY environment variable not set")
        sys.exit(1)
    try:
        data = get_weather(city, api_key)
        weather_desc = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        print(f"{city}: {weather_desc}, {temp}°C")
    except requests.HTTPError as e:
        print(f"HTTP error: {e}")
    except requests.RequestException as e:
        print(f"Request error: {e}")

if __name__ == "__main__":
    main()
