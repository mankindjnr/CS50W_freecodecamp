"""
here we are creating a class Flight to represent a real flight.
by default, the flight accepts the argumnets capacity only.
passengers is a list of passengers but we will only get it if there is a flight, hence not needed as a default

we then continue to create mehtods - functions that represent the actions that we might need to perform 
to the flight
"""
class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    #method of adding a passenger to the flight - we are adding them using their name
    #here we append the name of the passenger to the list using their name, self has an attribute
    #passengers - we add them to the object flight using self
    def add_passenger(self, name):
        if self.open_seats():
            self.passengers.append(name)
            return True

    #a function to check the number of open seats
    def open_seats(self):
        return self.capacity - len(self.passengers)

    

#creating a flight
flight = Flight(3)
people = ["kibe", "kris", "kikie", "michell", "mankind"]


#we are trying to add people to the flight.abs
#success will either be true or false, it its true, we add
#flight.add_passenger(person) - references the flight we have create above(line 30)
for person in people:
    sits_available = flight.add_passenger(person)
    if sits_available:
        print(f"Added {person} to flight")
    else:
        print(f"NO SITS AVAILABLE FOR {person}")