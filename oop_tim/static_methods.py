"""
you want to create classes that organize functions together.
static methods are used when you want to create a function that does not use any of the class's attributes.
A method that doesn't change the class's state is a good candidate for a static method.
"""
class Math:
    @staticmethod
    def add5(x):
        return x + 5

# static methods are called directly from the class - they do not need an instance
print(Math.add5(5))