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

## django is designed to work as a collection of other django apps
For this reason, when you cd into the parent project folder, start a new app and add install it

To create an app in the project, run the following command in the same location as the manage.py file
```python
python3 manage.py startapp <app_name>
```
this will create a folder with the app name and a subfolder with the same name and starter files for the app.

### next step after creating the app is to add it to the project
Install the app in the project by adding it to the INSTALLED_APPS list in the settings.py file in the project folder.

```python
INSTALLED_APPS = [
    'your app name',
    'app_name.apps.AppNameConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages', 
    'django.contrib.staticfiles',
]
```

### next step is to add the urls.py file in the project folder
go to the urls.py file in the project folder and add your app urls to the urlpatterns list.

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_name.urls'))
]
```

### next step is to add the urls.py file in the app folder
You can now headover to your newly installed app folder and add a urls.py file, this file will contain the urls for the app.

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')
]
```

## -> FOLLOW IN THE README FILE OF FLIGHTS APP