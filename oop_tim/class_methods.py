"""
class methods don't act for a specific instance, but for the class itself - they have no access to the instance
It is meant to be used as a factory method, which is a method that returns a class object/attributes
"""

class Person:
    number_of_people = 0
    GRAVITY = -9.8

    def __init__(self, name):
        self.name = name
        Person.add_person() # calling the class method to increment the number of people - the class attribute

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

p1 = Person("Tim")
p2 = Person("Jill")
print(Person.number_of_people())
