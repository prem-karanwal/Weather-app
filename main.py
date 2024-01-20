import requests

def get_weather(api_key, city, country):
    endpoint = "http://api.openweathermap.org/data/2.5/weather"
    location = f"{city},{country}"
    params = {
        'q': location,
        'APPID': api_key,
        'units': 'metric'
    }

    try:
        response = requests.get(endpoint, params=params)
        data = response.json()
        # print(data)
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        print(f"Response content: {response.content.decode('utf-8')}")
        return None

def display_weather(weather_data):
    if weather_data and 'name' in weather_data:
        print("\nCurrent Weather Conditions:")
        print(f"City: {weather_data['name']}")
        print(f"Country: {weather_data['sys']['country']} ")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Description: {weather_data['weather'][0]['description']}")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
    else:
        print("Unable to retrieve weather information.")

if __name__ == "__main__":
    api_key = "a1eccef0136bf55b958717d9353ae085"  
    city = input("Enter the city name: ")
    country = input("Enter the country code: ")
    weather_data = get_weather(api_key, city, country)
    display_weather(weather_data)
