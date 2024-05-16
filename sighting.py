"""
Student Name: SHARAD SHARMA, GAURI NEUPANE, SAKAR KHATIWADA
"""

from nominatim import gps_coordinate
from wildlife import get_species_list, get_surveys_by_species

def display_menu():
    """
     Displays the help menu for the wildlife application.
    """
    print("Help")
    print("====")
    print("Display help                             wildlife> help")
    print("Exit the application                     wildlife> exit")
    print("Display animal species in a city         wildlife> species city")
    print("Display animal sightings in a city       wildlife> sightings Cairns 1039")
    print("Display venomous species                wildlife> species Cairns venomous")

def search_species(city):
    """
        Searches for species data based on a city.
        :param city: Name of the city
        :return: Dictionary of species data based on city
        """
    coordinate = gps(city)  # Get GPS coordinates of the city
    species_data = get_species_list(coordinate)  # Get species data based on the GPS coordinates

    return species_data

def display_species(species_list, city_name):
    """
    Displays species data based on a city.
    :param species_list: Dictionary of species data based on city
    :param city_name: Name of the city
    :return: Dictionary of species data based on city.
    """
    print(f"Search found for {city_name}")
    print("=============")

    # Check the length of the species list
    if len(species_list) == 0:
        print(f"No Search found for {city_name}")  # If no species are found, print a message

    for species in species_list:
        try:
            # Extract species name and pest status
            name = species["Species"]["AcceptedCommonName"]
            status = species["Species"]["PestStatus"]

            # Print species name and pest status
            print(f" {name} (Pest Status: {status})")

        except Exception as e:
            # Handle other unforeseen errors that may occur
            print(f"Something went wrong! {e}")
def sort_by_date(sightings):
    """
    Sorts sightings by earliest date.
    :param sightings: Dictionary of sightings
    :return: Dictionary of sightings sorted by earliest date
    """
    sorted_sightings = sorted(sightings, key=lambda sighting: sighting["properties"]["StartDate"])
    return sorted_sightings

def display_sightings(sightings):
    """
    Displays sightings sorted by earliest date.
    :param sightings: Dictionary of sightings
    :return: Dictionary of sightings sorted by earliest date
    """
    print("Animal Sightings") 
    print("=============") 

    # Check if there are no sightings
    if len(sightings) == 0:
        print("No result founds")

    # Sort sightings by date
    sorted_sightings = sort_by_date(sightings)

    # Iterate over sorted sightings and display information
    for sighting in sorted_sightings:
        start_date = sighting["properties"]["StartDate"] 
        locality = sighting["properties"]["LocalityDetails"]
        site_code = sighting["properties"]["SiteCode"]

        print(f"Start Date:{start_date}, Locality: {locality}, Site Code: {site_code}")

def filter_venomous(species_list):
    """
    Filters species data based on a city.
    :param species_list: Dictionary of species data based on city
    :return: Dictionary of species data based on city
    """
    return [species for species in species_list if species["Species"]["PestStatus"] == "Venomous"]

def gps(city):
    """
    Returns gps coordinates for a city.
    :param city: Name of the city
    :return: GPS coordinates for a city
    """
    return gps_coordinate(city)

def main():
    """
    Main function of the application.
    """
    while True:
        user_input = input("wildlife> ")    # Prompt for user input

        # Check user input for various commands
        if user_input.lower() == "help":
            display_menu()  # Display help menu
        elif user_input.lower().startswith("species"):
            input_parts = user_input.lower().split(" ") # Process species command

            if len(input_parts) == 2:
                # Display species for a city
                city = input_parts[1]
                species_list = search_species(city)

                display_species(species_list, city)

            elif len(input_parts) == 3 and input_parts[2] == 'venomous':
                # Display venomous species for a city
                city = input_parts[1]
                species_list = search_species(city)
                venomous_species = filter_venomous(species_list)
                display_species(venomous_species, city + " (Venomous)")
            else:
                # Invalid command format
                print("Invalid command format: Please use 'species <city>'.")
        elif user_input.lower().startswith("sightings"):
            # Process sightings command
            input_parts = user_input.lower().split(" ")

            if len(input_parts) == 3:
                # Display sightings for a species in a city
                city = input_parts[1]
                taxonid = input_parts[2]

                coordinate = gps(city)
                sightings = get_surveys_by_species(coordinate, taxonid)
                display_sightings(sightings)
            else:
                # Invalid command format
                print("Invalid command format: Please use 'sightings <species> <city>'.")

        elif user_input.lower() == "exit":
            # Exit the application
            print("Exiting the application")
            break
        else:
            # Command not recognized
            print('Command not recognized')

if __name__ == "__main__":
    main()
