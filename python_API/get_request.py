DEMONSTRATION OF MAKING A GET REQUEST TO AN ENDPOINT

GET - is used to retrieve information from the given server using a given url.
The GET method sends the encoded user information appended to the page request.
    the page and the encoded information are separated by the "?" character.

            https://www.google.com/search?q=hello

MAKE GET REQUESTS THROUGH PYTHON REQUESTS
python requests module provides the get() for making get requests

    requests.get(url, params={key: value}, args)

    MAKING A REQUEST TO GITHUBS API

        import requests

        #making the GET request
        resp = requests.get('https://api.github.com/users/mankindjnr')

        #checking the status code for response received
        print(resp)

        #print content of request
        print(resp.content)

        #the above code has been run successfully in request_trial.py file

