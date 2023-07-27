# AIRLINE PROJECT
## ======================================================================
### continuing from the django readme file
### ======================================================================

** Before you even add urls to your app, what you want to do is create models for you app, this is done in the models.py file in the app folder. **

They will represent the data you want to be fed to django app.
All models will be a python class.

All these models will represent a table in the database.

## ======================================================================
### creating a model
```python
from django.db import models

class Flight(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"
```
### ----------------------------------------------------------------------
** The above code is a model for a flight, it has 3 fields, origin, destination and duration. **
** The class name is the name of the table in the database. **
** The fields are the columns in the table. **
** The id field is automatically created by django. **
** The __str__ method is used to represent the object in a string format. **
** The max_length argument is used to specify the maximum length of the field. **
** The duration field is an integer field, it will only accept integers. **

## ========================================================================
# Migrations
Even after creating the classes, they are yet to be recognized by django, to ensure django is updated with my models, I will run the following command in the terminal:

it is a two step process:
- first step is to create the migration file - the instructions for django to update the database

- second step is to apply the migration file to the database - take those instructions and apply them to the underlying database

#### this commands are run in the project folder, where the manage.py file is located

### ----------------------------------------------------------------------
### making migrations
```python
python manage.py makemigrations
```
### output
```python
Migrations for 'flights':
  flights/migrations/0001_initial.py
    - Create model Flight
```
__the model is now recognized by django__

** to view the model success, go to yourApp/migrations/0001_initial.py **
** this file contains the instructions for django to update the database **
__here you will see the instructions for creating the table and the columns in the database__

### applying migrations ot django database
```python
python manage.py migrate
```

## ==========================================================================
To interact with the database, django provides a python shell, this is a python interpreter that is connected to the django project.
```bash
python manage.py shell
```
### ----------------------------------------------------------------------
This will open a python shell where you can run python commands that are executed on our web application.

### in the shell
```python
from flights.models import Flight

f = Flight(origin="New York", destination="London", duration=415)
f.save()
```
** the above code will create a new flight object and save it to the database. **
** the save() method is used to save the object to the database. **
** I no longer have to write sql queries to interact with the database, python statement work **

### querying the database
```python
Flight.objects.all()
```
And due to the __str__ method in our class, thee output wil be pretty:
```python
<QuerySet [<Flight: 1: Nairobi to Persia>]>
```

since these are python classes, you can create an instance of the class
```python
flights = Flight.objects.all()
```
** this will return a list of all the flights in the database **

** you can also query a single flight **
```python
f = Flight.objects.get(id=1)
```

**retrieve the first flight**
```python
flight = Flight.objects.first()
```

** query that output in a pythonic manner **
```python
flight.origin

flight.destination

flight.duration

flight.id
```
** delete a flight **
```python
    flight.delete()
```

### ----------------------------------------------------------------------
creating a new model so we can have relationships between them
```python
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"
```

And now, the flight model will have a foreign key to the airport model
```python
class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()
    
    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"
```
** the origin field is now a foreign key to the airport model **
** the on_delete argument is used to specify what happens when the airport is deleted, CASCADE means that when the airport is deleted, all the flights that have that airport as the origin will also be deleted. **

** the related_name argument is used to specify how to access the flights from the airport model. -Accessing in reverse order (Flight.origin) gives you all the flights from that airport**

### ----------------------------------------------------------------------
** to update the database with the new model, run the following commands **
```python
python manage.py makemigrations
python manage.py migrate
```
### ----------------------------------------------------------------------
** to add a new airport to the database **
#### ......................................
```python
a = Airport(code="NBO", city="Nairobi")
a.save()
b = Airport(code="LAX", city="Los Angeles")
b.save()
c = Airport(code="JFK", city="New York")
c.save()
d = Airport(code="LHR", city="London")
d.save()
```
** to add a new flight to the database **
#### ......................................
```python
f = Flight(origin=a, destination=b, duration=415)
f.save()
```
you can now query the database to see the new flight
```python
Flight.objects.all()
f
f.origin
f.destination
f.duration
```
** to query the airport model **
```python
Airport.objects.all()
f.origin.city
f.origin.code

# reverse lookup
a.departures.all()
a.arrivals.all()

```
## ========================================================================
We now go back to our views.py file and add the following code to retrieve all flights and loop with them in the template:
```python
from django.shortcuts import render

from .models import Flight

# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })
```
** the above code will retrieve all the flights from the database and pass them to the template **
### ----------------------------------------------------------------------
### Filter the Airport model
```python
Airport.objects.filter(city="Nairobi")
```
** this will return all the airports with the city Nairobi **
### ----------------------------------------------------------------------

# ADMIN
The creation of models and manipulation of the data in them is so common that django has a built in admin interface that allows you to do this without writing any code.

To use the admin account we need to create an admin account and it is done on the command line. 
Run the following command in the your application folder in the same directory as the manage.py file.
```python
python manage.py createsuperuser
```
I now have the credentials to log into the admin interface and manipulate the data in the database.

** To do this, i have to first take my models and add them to admin app, this is done in the admin.py file in the app folder. **

In the admin.py file:

```python
from django.contrib import admin
from .models import Airport, Flight

# Register your models here.
admin.site.register(Airport)
admin.site.register(Flight)
```
** the above code will register the models to the admin app. **

### ----------------------------------------------------------------------
## Accessing the admin interface
go to the url and add /admin to the end of the url
```python
http://127.0.0.1:8000/admin
```
** this will take you to the admin login page, enter the credentials you created earlier. **
** you can now add airports and flights to the database. **

## ========================================================================
** we a re now going to add move templates to our app **

we are creating a template for every flight so as to display their info separately.
we will do this by retrieving and passing the flight to the template using their id as follows:
```python
def flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id) 
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    })
```
** the above code will retrieve the flight with the id passed in the url and pass it to the template. **

Django also allows you to use the _pk_ variable which references the primary key of the object.
```python
def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id) 
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    })
```
```python
"non_passengers": Passenger.objects.exclude(flights=flight).all()
```
** the above code will retrieve all the passengers that are not on that flight. **
** the exclude() method is used to exclude the passengers on that flight. **
** the all() method is used to retrieve all the passengers. **

## ========================================================================
we are creating a new model now, the passenger model.
```python
class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"
```
Whats in the class are the attriubutes of a passenger, first name, last name and the flights they have taken. A passenger should have a one to many relationship with the flights model since a single passenger may book more than one flight.

This line here describes the relationship between the passenger and the flight model:
```python
flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")
```
- blank=True means that the passenger may not have any flights
- related_name="passengers" is used to access the passengers from the flight model

** to update the database with the new model, run the following commands **
```python
python manage.py makemigrations
python manage.py migrate
```
** we will now add it to our admin page and also add it to the flight template **
```python
 "passengers": flight.passengers.all(),
 ```
    ** the above code will retrieve all the passengers on that flight. **
    - passengers is the related name we gave the flight model

## ========================================================================
### we will now add a function that will allow us to add passengers to a flight
```python
def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id) 
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))
    return render(request, "flights/book.html", {
        "flight": Flight.objects.get(pk=flight_id),
        "passengers": Passenger.objects.all(),
    })

```
### description
- **if request.method == "POST":** is used to check if the form has been submitted
- the above code will retrieve the flight and the passenger from the database
- the passenger is retrieved from the form in the template **(request.POST["passenger"])**
- the passenger is then added to the flight **passenger.flights.add(flight)**
- the user is then redirected to that flight page **return HttpResponseRedirect(reverse("flight", args=(flight.id,)))**
- **Passenger.objects.get(pk=int)** is used to convert the string to an integer and retrieve the passenger from the database

## ========================================================================
# ADMIN CUSTOMIZATION - checkout the django documentation for more info

It is possible to customize the admin interface given to you by django.
here is how to do it:

### ----------------------------------------------------------------------
Go to the admin.py file in the app folder and add the following code:
```python
from django.contrib import admin
from .models import Airport, Flight, Passenger

# Register your models here.
class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")

admin.site.register(Flights, FlightAdmin)
```
### description
- **list_display** is used to specify the fields to be displayed in the admin interface
- **admin.site.register(Flights, FlightAdmin)** is used to register the model and the admin interface -  it tells the admin interface how to display the model flights, it directs it to use the FlightAdmin class as settings.

### ----------------------------------------------------------------------
** to customize the admin interface for the passenger model, add the following code to the admin.py file **
```python
class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)

admin.site.register(Passenger, PassengerAdmin)
```
### description
- **filter_horizontal** is used to specify the fields to be displayed in the admin interface
** helps me to show the relationship between the passenger and the flight model **

## ========================================================================
# AUTHENTICATION - LOGGING IN, USER REGISTRATION, LOGGING OUT

in out airline app, we will create another app called users, this app will be used to handle the authentication of users.

### ----------------------------------------------------------------------
** to create the users app, run the following command in the terminal **
```python
python manage.py startapp users
```

After creating the app users, don't forget to install it and add it to the urls in the project folder.

### ----------------------------------------------------------------------
## user - urls.py
```python
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"), # new
    path("logout", views.logout_view, name="logout"), # new
]
```
### ----------------------------------------------------------------------
