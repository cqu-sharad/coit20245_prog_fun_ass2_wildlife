"""
Student Name: SHARAD SHARMA, GAURI NEUPANE, SAKAR KHATIWADA
"""

import requests

def gps_coordinate(city):
    """
    Returns the GPS coordinates of a city
    :param city: Name of the city
    :return: GPS coordinates
    """

    # Construct the base URL for the API request
    base_url = f"https://nominatim.openstreetmap.org/search?q={city}&format=json"

    try:
        # Send a GET request to the Nominatim API endpoint
        response = requests.get(
        base_url,
        headers={
            'User-Agent': 'CQUniversity (sharad.sharma@cqumail.com)'
        })
        data = response.json()  # Parse the JSON response

        # Check if data is not empty
        if data:
            results = data[0]   # Extract the first result

            # Extract latitude and longitude and convert them to float
            return {
                "latitude": float(results['lat']),
                "longitude": float(results['lon'])  
            }
    
    except requests.RequestException as e:
        # Handle any request exceptions and print an error message
        print(f"Something went wrong! {e}")

        # Return None to indicate an error occurred
        return None

        