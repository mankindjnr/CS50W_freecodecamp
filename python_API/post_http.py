import requests

"""
the post request is designed to request the web server to accept the data enclosed in the body of the
request message.
Used mostly when uploading a file or a completed form

the syntax is
     requests.post(url, params={"key": "value"}, args)
"""

# making the post request

response = requests.post("https://httpbin.org/post", data = {"name":"amos"})

# check the status code of the post request we just made
print(response.status_code)

#printing the content of the request
print(response.json())