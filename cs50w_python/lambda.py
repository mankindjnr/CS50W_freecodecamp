people = [
    {"name": "kikie"},
    {"name": "michell"},
    {"name": "mankindjnr"}
]

def f(person):
    return person["name"]

#since sort func can't sort dicts we now passing a value, name of in the dicts to sort by
people.sort(key=f)
#lambda equivalent
people.sort(key=lambda person: person["name"])

print(people)