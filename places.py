import os
import re
import requests

GOOGLE_PLACES_API_KEY = os.getenv("GOOGLE_PLACES_API_KEY")

def extract_city(user_query: str) -> str:
    match = re.search(r'\bв\s+([А-Яа-яA-Za-z\s\-]+)', user_query)
    if match:
        return match.group(1).strip()
    return ""

def search_places(city: str, query: str = "attractions", limit: int = 5) -> list:
    location_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    location_params = {
        "query": city,
        "key": GOOGLE_PLACES_API_KEY
    }
    loc_response = requests.get(location_url, params=location_params).json()
    if not loc_response.get("results"):
        return []

    location = loc_response["results"][0]["geometry"]["location"]
    lat, lng = location["lat"], location["lng"]

    nearby_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    nearby_params = {
        "location": f"{lat},{lng}",
        "radius": 10000,
        "keyword": query,
        "key": GOOGLE_PLACES_API_KEY
    }
    places_response = requests.get(nearby_url, params=nearby_params).json()
    places = places_response.get("results", [])[:limit]

    return [place["name"] for place in places]

