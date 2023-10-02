"""
This is a module that contains the class Dog, we are creating a template of what do can do, the template
will be built using methods, and the methods will be built using functions.
The methods are the actions that the object can do.
This methods have an argumnet called self, which is a reference to the object itself.
"""

class Dog:
    """a special method called __init__ that is used to initialize the object right after it has been created.
    it is called immediately after the object is created, before we have a chance to assign values to the object's
    attributes.
    i.e when Bosco = Dog() is called, the __init__ method is called.
    Whenever you create an instance of the class, it is called(__init__ method)

    if there are any arguments that need to be passed to the object during creation, the __init__ method
    can receive them and pass them on to the object's internal variables. This is done by adding parameters when
    you create an instance of the class.

    if the Dog class is not accepting any arguments, then the __init__ method would be defined as follows:
    def __init__(self):
        pass

    if Dog class is to accept a name when its created, then the __init__ method would be defined as follows:
    def __init__(self, name):
        self.name = name

        # self.name is now an attribute of the object, and it will be assigned the value of the name argument

    when creating its instance, you would pass the name as an argument to the class constructor:
    Bosco = Dog("Bosco")
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    # methods that can modify or create new attributes of the object
    def set_age(self, age):
        self.age = age

    def add_one(self, x):
        return x + 1
    def bark(self):
        return "Woof!"


# instance of class Dog stored in a variable
# if the Dog class is not accepting any arguments, then the __init__ method would be defined as follows:
    #Bosco = Dog()
# if Dog class is to accept a name when its created, then the __init__ method would be defined as follows:
Bosco = Dog("Bosco", 94)
print("passed age: ", Bosco.get_age())
# above we have passed 94 as the age, we will now set a new age
Bosco.set_age(940)


# calling the methods of the object Bosco
print(Bosco.get_name())
print("set age: ", Bosco.get_age())

# calling the method bark and add_one of the object Bosco
Bosco.bark()
Bosco.add_one(5)
