# etl/api_utils.py
import requests
import logging

def get_geolocation_data(region):
    """Fetch geolocation info using OpenStreetMap API (free)."""
    try:
        url = f"https://geocode.maps.co/search?q={region}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        if data:
            return {
                'latitude': data[0].get('lat'),
                'longitude': data[0].get('lon'),
                'display_name': data[0].get('display_name')
            }
        return {'latitude': None, 'longitude': None, 'display_name': None}
    
    except Exception as e:
        logging.warning(f"⚠️ Failed to fetch geolocation for region '{region}': {e}")
        return {'latitude': None, 'longitude': None, 'display_name': None}
