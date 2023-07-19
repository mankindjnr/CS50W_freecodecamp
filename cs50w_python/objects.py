"""
creating a class
 -- a template of for a type of object

 here we are going to create a class point, and there one, we can
 create other points, that reflect on this class
"""

class Point():
    """__init__
    this is a method/function that will be auto called everytime we are going to create a point
    all the methods that operate on the object will have to take an argument, SELF
    SELF - represents the object we are working on
    x and y - these are the arg we will need to have to create a point
    """
    def __init__(self, x, y):
        """
        to store any data in the point, need to reference it using self.
        the data we are passing (x and y) need to refernce the object
        the self ensures that they are stored in the object
        """
        self.x = x
        self.y = y

"""
creating a new point
we have already defined a point class, now, we are just creating new points with that template
var.obj_arg = accesses that value i.e p.x accesses the value of x in p
"""
p = Point(2, 8)
print(p.x)
print(p.y)