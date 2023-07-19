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
