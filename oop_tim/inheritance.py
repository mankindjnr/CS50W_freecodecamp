"""
the idea is, we have two classes Cat and Dog, both of them have the same method speak() but they do almost
similar things. Like the classes below, where the only difference is the print statement in the speak() method.

This way, we can create one class Pet and have the Cat and Dog classes inherit from it. This way, we can
reduce the amount of code we write and also make it easier to maintain.

This is called inheritance. We can create a class that inherits from another class.
This class Pet is a parent class and the classes Cat and Dog are child classes.
The parent class will have all the common methods and attributes that the child classes can inherit and use.
It will also be the onyl class that has an __init__ method.
"""

# parent class  -will contain all the common methods and attributes that the child classes can inherit and use
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        # showing all the attributes of the object
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what to say")

# child class - will contain on top of the methods and attributes of the parent class, its own methods
# and attributes
class Cat(Pet):
    def speak(self):
        print("Meow")

class Dog(Pet):
    def speak(self):
        print("Bark")

Animal = Pet("Animal", 10)
Animal.show()

# creating an instance of the Cat class - cat specificaly has no attributes or methods of its own
# the arguments passed to the Cat class are the arguments that will be passed to the Pet class
cat1 = Cat("Cat1", 5)
cat1.show()
# the speak method of the Cat class is called and this is one is different from any other class. If a child
# class has a method with the same name as the parent class, then the child class method will be called
cat1.speak()

# creating an instance of the Dog class
dog1 = Dog("Dog1", 7)
dog1.show()
# the speak method of the Dog class is called and this is one is different from any other class
dog1.speak()
print("===============================================================================================================")


# ======================================================================================================================
# lets say you want the child class to have its own __init__ method, then you can do the following:
# parent class is the PET class
class BigPet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        # showing all the attributes of the object
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what to say")

# child class is the BIGCAT class
class bigCat(BigPet):
    def __init__(self, name, age, color): # we are passing all the arg our parent needs to be initialized and our own as well
        super().__init__(name, age) # we are referencing the parent class and calling its __init__ method - it will run the parent class naturally
        self.color = color
    
    def speak(self):
        print("Roar")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

# creating an instance of the BigCat class
bigCat1 = bigCat("BigCat1", 10, "Brown")
bigCat1.show()