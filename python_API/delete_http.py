import requests

"""
it deletes the specified resource
you need to specifiy a resource
"""

#the delete request
response = requests.delete("https://httpbin.org/delete", data = {"name":"kair"})

# the status code
print(response.status_code)

#print the content of request
print(response.json())