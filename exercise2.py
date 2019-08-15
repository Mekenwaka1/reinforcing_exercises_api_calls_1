import requests

elections_response = requests.get('https://represent.opennorth.ca/elections')
elections = elections_response.json()

print(elections, type(elections))
