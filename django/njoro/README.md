# CREATING DJANGO APPS IN OUR NJORO PROJECT.
# ==========================================
all apps in django are created in the same way and from the same location.
to create an app in the project, run the following command in the same location as the manage.py file

```python
python3 manage.py startapp <app_name>
```
**
this will create a folder with the app name and a subfolder with the same name and starter files for the app.**

*** As soon as you create the app, you need to install the new app in the project folder in the same location as manage.py file. The folder name matches that of the project folder. In this case, the project folder is njoro.***

**To install the app, open the settings.py file in the project folder and add the app name to the list of installed apps.**

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions', 
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hello',
    'newyear',
]
```

### FINAL STEP IN INSTALLING THE APP
**The final step is to create a url for the app in the urls.py file in the project folder.
In the same folder as the settings.py file, locate the urls.py and add the url to these new app as follows to ensure django finds it when users go to that url**

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include('hello.urls')),
    path('newyear/', include('newyear.urls')),
]
```

**The app is now installed and ready to be used.**

_remember that the urls file we have highlighted above is the one in the project folder and not the one in the app folder and it is not given to us by default, hence we need to create ourselves.
**go to your new apps folder and create that urls.py file**_

### CREATING THE URLS.PY FILE IN THE APP FOLDER - default
```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
```

## CURRENT LIST OF APPS CREATED
- hello
- newyear
- tasks