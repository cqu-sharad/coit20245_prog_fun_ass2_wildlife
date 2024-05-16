"""
Student Name: SHARAD SHARMA, GAURI NEUPANE, SAKAR KHATIWADA
"""
import requests

def  get_species_list(coordinate, radius=600000):
    """
    Retrieves a list of species based on a specified coordinate within a given radius.

    :param coordinate: 'latitude' and 'longitude' keys representing the coordinate.
    :param radius: Default is 600,000 meters
    :return: A list of species names.
    """
    # Extract latitude and longitude from the coordinate dictionary
    latitude, longitude = coordinate['latitude'], coordinate['longitude']

    # Construct the base URL for the API request
    base_url = f"https://apps.des.qld.gov.au/species/?op=getspecieslist&kingdom=animals&circle={latitude},{longitude},{radius}"

    try:
        response = requests.get(base_url)   # Send a GET request to the API endpoint
        data = response.json()  # Parse the JSON response

        # Extract the list of species sighting summaries from the response data
        results = data["SpeciesSightingSummariesContainer"]["SpeciesSightingSummary"]

        # Return the list of species sightings
        return results

    except requests.RequestException as e:
        # Handle any request exceptions and print an error message
        print(f"Something went wrong! {e}")

        # Return None to indicate an error occurred
        return None

def get_surveys_by_species(coordinate, taxonid, radius=100000):
    """
    Retrieves a list of species based on a specified coordinate within a given radius.
    :param coordinate: 'latitude' and 'longitude' keys representing the coordinate.
    :param taxonid: The taxon ID of the species.
    :param radius: Default is 100000 meters
    :return: A list of species names.
    """
    # Extract latitude and longitude from the coordinate dictionary
    latitude, longitude = coordinate['latitude'], coordinate['longitude']

    # Construct the base URL for the API request
    base_url = f"https://apps.des.qld.gov.au/species/?op=getsurveysbyspecies&taxonid={taxonid}&&circle={latitude},{longitude},{radius}"
    
    try:
        response = requests.get(base_url)   # Send a GET request to the API endpoint
        data = response.json()  # Parse the JSON response

        results = data["features"]

        if results is not None:
            # Filter surveys based on SiteCode 'INCIDENTAL'
            surveys = [survey for survey in data["features"] if survey["properties"]["SiteCode"] == "INCIDENTAL"]
            return surveys
        else:
            return None

    except requests.RequestException as e:
        # Handle any request exceptions and print an error message
        print(f"Something wen wrong! {e}")

        # Return None to indicate an error occurred
        return None
