"""
Student Name: <SHARAD SHARMA>, <GAURI NEUPANE>, <SAKAR KHATIWADA>
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