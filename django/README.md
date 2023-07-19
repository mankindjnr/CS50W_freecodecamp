# DJANGO - PYTHON WEB FRAMEWORK
## INSTALLATION
pip3 install django

## command to run to enable creation of a django project
django-admin startproject <project_name>

this will create a folder with the project name and a subfolder with the same name and starter files for the project.

## running the project
```python
python3 manage.py runserver
```

**django is designed to work as a collection of other django apps**
to create an app in the project, run the following command in the same location as the manage.py file
```python
python3 manage.py startapp <app_name>
```
this will create a folder with the app name and a subfolder with the same name and starter files for the app.

#### we will describe what the files in that folder as we continue with the project
## file <1> **views.py**
These file lets us describe what the user sees when they visit a particular url/route in our website.

### information
**we have created this app _hello_ app that we want to install into this project _njoro_**
**To install, we go to the settings.py file in the _njoro_ folder and add the app name to the list of installed apps**
```python
INSTALLED_APPS = [
    'hello',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    ...
]
```
**we now want to make the app display something when visited**

To do this, we go to the views.py file in the _hello_ folder and add the following code:
To create a View in django, we create a function that takes in a request and returns a response
```python
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```
**we now want to map this view to a url**
**we are mapping these view to an url because we want to tell django when to execute the above function and return its response**

_we create a url configuration file in the app folder to tell django what to do when a user visits a particular url_

Django comes with a default urls.py file for the whole project. but sometimes we want to create a urls.py file for a specific app. So, for hello app, we will create a urls.py file in the hello folder.

in the urls.py file we will define a variable **urlpatterns** that will be a list of urls that will be accessed in this app _hello_
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```
# Description of the above code
**from django.urls import path** - this is a function that will be used to map urls to views

**urlpatterns** - this is a list of urls that will be accessed in this app _hello_

**from . import views** - tells it from the current directory, import the views.py file

### path('', views.index, name='index')**
- **path('')** - this is the url that will be accessed in this app _hello_ - meaning the root url of the app

- **views.index** - this is the view that will be executed when the above url is accessed - it stands for the views.py file and a function called index. This function will be executed when the above url is accessed

- **name='index'** - this is the name of the url. It is used to identify it - it makes it easy to reference the url in other parts of the code. **its optional**

## **we now want to tell django to use this urls.py file in the hello app**
we go back to the main urls file in the _njoro_ folder and add the following code:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # this tells django to use the urls.py file in the hello app
    path('hello/', include('hello.urls')),
]
```

## Description of the above code
- path('hello/', include('hello.urls')) - this tells django to use the urls.py file in the hello app when hello/ path is accessed. it also hands over its urls.py file so that any other urls in the hello app can be accessed

## description of a dynamic url
```python
path('<str:name>', views.greet, name='greet'),
```
- **<str:name>** - this is a dynamic url. it means that the url can be accessed with any string. the string will be passed to the view function as an argument.

so, any time we access the route _hello/<str:name>_, the view function greet will be executed and the string will be passed to it as an argument. and remember <str:name> stands for any string passed after the hello/ route, it will be taken as an argument to the view function greet.
- [sample url](http://127.0.0.1:8000/hello/kikie)

## ADDING HTML TO THE VIEW FUNCTION
instead of returning a httprresponse, we can return an html file. to do this, we create a **templates** and inside that folder optionally create another folder after the apps name **hello** and add an html file in it. we then return the html file in the view function

**we go from this**
```python
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```
**to this**
```python
def index(request):
    return render(request, "hello/index.html")
```

## description of the above code
- **"hello/index.html"** - here we can use index.html but we prefix them with the app name to avoid conflicts with other apps. so, we use hello/index.html to identify that index.html file with its app.

## passing data to the html file
```python
def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
        })
```
## description of the above code
- **"name": name.capitalize()** - this is a python dictionary that will be passed to the html file. the key is name and the value is the name passed to the view function _greet_. we can use the value in the html file by using the key name. we can also manipulate the value before passing it to the html file. in this case, we are capitalizing the name before passing it to the html file.