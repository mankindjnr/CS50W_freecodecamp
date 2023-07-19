"""
decorators a re functions that take in a function and return a modified version of that function
it adds more behaviour to that function

here we have function announce that takes in a function f
announce wraps the function f with additionals behaviors hence known as wrapper
"""

def announce(f):
    def wrapper():
        print("about to run the func")
        f()
        print("done with the function")
    
    return wrapper

@announce #we are adding the decorator to this function hello
def hello():
    print("hellow, world")

hello()