import requests

#making the GET request
resp = requests.get('https://api.github.com/users/mankindjnr')

#checking the status code for response received (the whole string)
print(resp)

#print content of request
#print(resp.content)

# print the request object - (the url we queried)
print(resp.url)

# print the status code.(the code only)
print(resp.status_code)