import json
"""
PYTHON PARSE A JSON FILE

to work with json, python has an inbuilt json packahe (json)

PARSE JSON - convert from json to python
    json.loads() method can parsse a json string and the result will be a python dictionary

    json.loads(json_string)

"""

# CONVERT JSON TO PYTHON
# the json string
employee = '{"id":"09", "name":"amos", "department":"tech"}'

#convert string to python dict
employee_dict = json.loads(employee)
print(employee_dict)

# exptracting a value using its key from the python dictionary formed from parsing  a json string
print(employee_dict['name'])


"""
PYTHON READ A JSON FILE

json.load() can read a file which contains a json object i.e employee.json containing
    a json object

    json.load(file_object)
"""
"""
# reading a json file

# opening json file
f = open("data.json")

# return a json object as a python dictionary
data = json.load(f)

# iterating through the json list
for i in data['emp_details']:
    print(i)

# closing the file
f.close()
"""

"""
CONVERT FROM PYTHON to JSON

json.dumps() is a method that converts python object into a json string

it takes two parameters, a dictionaru which is to be converted into a json object
    and an indent - the number of units for identation
"""

# convert python to json

# data to e written
dictionary = {
    "id": "08",
    "name":"mankind_jnr",
    "department":"tech"
}

# serializing json
json_object = json.dumps(dictionary, indent = 8)
print(json_object)