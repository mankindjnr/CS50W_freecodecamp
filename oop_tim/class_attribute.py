class Person:
    number_of_people = 0 # class attribute- it does not have the self keyword - its not tied to any particular instance of the class
    # class attributes are shared by all instances of the class -  they are constant and do not from one instance to another
    # self attributes are unique to each instance of the class

    #defining a class attribute makes it a constant - hence you can define global constants in a class
    # this is a constant that will be shared by all instances of the class and it will not change for any instance
    GRAVITY = -9.8


    def __init__(self, name):
        self.name = name
        Person.number_of_people += 1 # this will keep track of the number of people that have been created
                                    # how many instances have been created - since each instance we call
                                    # the same attribute, it will be incremented by 1

p1 = Person("Tim")
p2 = Person("Jill")
p3 = Person("Bill")

print(p1.number_of_people) # accessing it from the instance of the class
print(Person.number_of_people) # accessing it from the class itself

Person.number_of_people = 8 # changing the value of the class attribute
print(p1.number_of_people) # accessing it from the instance of the class - the value has changed for all instances of the class