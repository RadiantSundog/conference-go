from .keys import PEXELS_API_KEY, OPEN_WEATHER_API_KEY
import requests


def get_photo(city, state):
    url = "https://api.pexels.com/v1/search"
    query = {"query": f"{city}, {state}"}
    headers = {"Authorization": PEXELS_API_KEY}
    response = requests.get(url, params=query, headers=headers)
    content = response.json()
    try:
        picture_url = content["photos"][0]["src"]["original"]
        return {"picture_url": picture_url}
    except (KeyError, IndexError):
        return {"picture_url": None}
    # Create a dictionary for the headers to use in the request
    # Create the URL for the request with the city and state
    # Make the request
    # Parse the JSON response
    # Return a dictionary that contains a `picture_url` key and
    #   one of the URLs for one of the pictures in the response


def get_weather_data(city, state):
    url = "http://api.openweathermap.org/geo/1.0/direct"
    params = {"q": f"{city}, {state}", "appid": OPEN_WEATHER_API_KEY}
    response = requests.get(url, params=params)
    content = response.json()
    lat = content[0]["lat"]
    lon = content[0]["lon"]

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"lat": lat, "lon": lon, "appid": OPEN_WEATHER_API_KEY}
    response = requests.get(url, params=params)
    content = response.json()
    description = content["weather"][0]["description"]
    temp = content["main"]["temp"]
    return {"description": description, "temp": temp}


# Create the URL for the geocoding API with the city and state
# Make the request
# Parse the JSON response
# Get the latitude and longitude from the response
# Create the URL for the current weather API with the latitude
#   and longitude
# Make the request
# Parse the JSON response
# Get the main temperature and the weather's description and put
# them in a dictionary
# Return the dictionary
