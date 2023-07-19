import requests
from requests.auth import HTTPBasicAuth

response = requests.get('https://api.github.com/mankindjnr, ', 
                        auth = HTTPBasicAuth('mankindjnr', '@1999FutureAlpha94!'))

print(response)