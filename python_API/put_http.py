import requests

"""
it requests that the enclosed entity be stored under the supplied url
if the url refers to an already existing resource, it is modified
if the resource doesn't exist, one is created with that url
"""

# the put request
response = requests.put("https://httpbin.org/put", data = {"name":"mankind_jnr"})

# the status code
print(response.status_code)
# print content of request
print(response.content)
