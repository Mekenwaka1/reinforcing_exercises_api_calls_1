import requests

ottawa_wards_response = requests.get('https://represent.opennorth.ca/boundaries/?sets=ottawa-wards')
boundaries_dictionary = ottawa_wards_response.json()

for ward in boundaries_dictionary['objects']:
    print(ward['name'])
