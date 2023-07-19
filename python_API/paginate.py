import requests

baseURL = "https://rickandmortyapi.com/api/"

endpoint = "character"

resp = requests.get(baseURL + endpoint)

print(resp.status_code)
#print(resp.json())

data = resp.json()

# acecessing different parts of the jsin data
# using key to print values associated with it
pages = data['info']['pages']
print(data)

# the name
name = data['results'][0]['name']
print(name)

episodes = data['results'][0]['episode']
print(len(episodes))