"""
Student Name: SHARAD SHARMA, GAURI NEUPANE, SAKAR KHATIWADA
"""
def display_menu():
    print("Help")
    print("====")
    print("Display help                             wildlife> help")
    print("Exit the application                     wildlife> exit")
    print("Display animal species in a city         wildlife> species city")
    print("Display animal sightings in a city       wildlife> sightings Cairns 1039")
    print("Display venonmous species                wildlife> species Cairns venomous")

def search_species(city):
    species_data = {
        "cairns": [
            {"Species": {"TaxonID": 1001, "AcceptedCommonName": "parrot", "PestStatus": "Safe"}},
            {"Species": {"TaxonID": 1002, "AcceptedCommonName": "lizard", "PestStatus": "Safe"}},
            {"Species": {"TaxonID": 1003, "AcceptedCommonName": "spider", "PestStatus": "Venomous"}}
        ],
        "brisbane": [
            {"Species": {"TaxonID": 2001, "AcceptedCommonName": "koala", "PestStatus": "Protected"}},
            {"Species": {"TaxonID": 2002, "AcceptedCommonName": "kangaroo", "PestStatus": "Safe"}},
            {"Species": {"TaxonID": 2003, "AcceptedCommonName": "bat", "PestStatus": "Nuisance"}}
        ],
        "sydney": [
            {"Species": {"TaxonID": 3001, "AcceptedCommonName": "snake", "PestStatus": "Venomous"}},
            {"Species": {"TaxonID": 3002, "AcceptedCommonName": "spider", "PestStatus": "Venomous"}},
            {"Species": {"TaxonID": 3003, "AcceptedCommonName": "seagull", "PestStatus": "Nuisance"}},
            {"Species": {"TaxonID": 3004, "AcceptedCommonName": "octopus", "PestStatus": "Venomous"}}
        ]
    }

    cites = species_data[city]

    return cites

def display_species(species_list, city_name):
     print(f"Search found for {city_name}") 
     print("=============") 

     if len(species_list) == 0: 
        print(f"No Search found for {city_name}") 

     for species in species_list: 
        name = species["Species"]["AcceptedCommonName"]
        status = species["Species"]["PestStatus"] 

        print(f" {name} (Pest Status: {status})") 
        
def search_sightings(taxonid, city): 
    return [{"properties":{"TaxonID": taxonid, "StartDate": "1999-11-15", "LocalityDetails": city, "SiteCode": "INCIDENTAL"}}]

def display_sightings(sightings): 
    print("Animal Sightings") 
    print("=============") 

    if len(sightings) == 0:
        print("No result founds") 

    for sighting in sightings:
        start_date = sighting["properties"]["StartDate"] 
        locality = sighting["properties"]["LocalityDetails"] 

        print(f"Start Date:{start_date}, Locality: {locality}")

def filter_venomous(species_list):
    return [species for species in species_list if species["Species"]["PestStatus"] == "Venomous"]

def main():
    while True:
        user_input = input("wildlife> ")

        if user_input.lower() == "help":
            display_menu()
        elif user_input.lower().startswith("species"):
            input_parts = user_input.lower().split(" ")

            if len(input_parts) == 2:
                city = input_parts[1]
                species_list = search_species(city)

                display_species(species_list, city)

            elif len(input_parts) == 3 and input_parts[2] == 'venomous':
                city = input_parts[1]
                species_list = search_species(city)
                venomous_species = filter_venomous(species_list)
                display_species(venomous_species, city + " (Venomous)")
            else:
                print("Invalid command format: Please use 'species <city>'.")
        elif user_input.lower().startswith("sightings"):
            input_parts = user_input.lower().split(" ")

            if len(input_parts) == 3:
                city = input_parts[1]
                taxonid = input_parts[2]

                sightings = search_sightings(taxonid, city)
                display_sightings(sightings)
            else:
                print("Invalid command format: Please use 'sightings <species> <city>'.")

        elif user_input.lower() == "exit":
            print("Exiting the application")
            break
        else:
            print('Command not recognized')

if __name__ == "__main__":
    main()