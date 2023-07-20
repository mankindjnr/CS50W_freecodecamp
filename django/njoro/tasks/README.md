# A NEW APP FOR A TODO LIST
## --------------------------------------------------------------------------------

# This is a new app for a todo list. It is a simple app that allows you to add, delete, and update tasks. It also allows you to mark tasks as complete.

# ## Getting Started
we have gone into the views.py file and created the default fnction thats called to display the initial page. It displays our tasks. But since that is not dynamic, we want to have the ability to add a task ourselves.

For this, we have created another  function _add_, this function renders an html page add.html that contains a form that takes in a value and a submit button.

## TEMPLATE INHERITANCE
We have created a layout.html file that contains the basic html structure of our app.
Any page that will follwo the same structure, will only have to extend it and write the content that differs only to avoid repetition.
```django
{% extends 'layout.html' %}
```
### ---------------------------------------------------------------------------
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tasks</title>
</head>
<body>
    {% block content %}
    {% endblock %}
</body>
</html>
```
### DESCRIPTION OF THE ABOVE CODE
The above code is the basic html structure of our app. It contains a block tag that will be used to extend the layout.html file. The block tag is used to write the content that differs from the layout.html file.
any file that wants to follow this structure, will extend the layout.html file and write the content that differs inside the block tags.

#### EXAMPLE
```django
{% extends "tasks/layout.html" %}

{% block body %}

    <h1> ALL TASKS </h1>
    <ul>
    {% for tasks in tasks %}
            <li>{{tasks}}</li>
    {% endfor %}
    </ul>

{% endblock %}
```
here, the body of the template will be replace with the content inside _block body_ and _endblock_ and the rest of the layout will be inherited from the layout.html file.

## LINKS
adding links is a bit different in django. We have to use the _url_ tag to add links. This makes it easy and not hardcoded. the tags we give our urls are the ones we will use to refer to them.

```django
<a href="{% url 'add' %}">Add a New Task</a>
```
### --------------------------------------------------------------------------
with the links we have created and the multiple apps we have, we may encounter a problem due to multiple apps having similar url names tags. To avoid links navigating to the wrong app, we will and an **app_name** to the urls.py file of each app. This will make the url tags unique to each app. 
the updated urls.py file will look like this:
```python
from django.urls import path
from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add")
]
```
While the updated links will look like this: they are now unique to the app tasks.
```django
<a href="{% url 'tasks:add' %}">Add a New Task</a>
```
### ------------------------------------------------------------------------------
## FORMS
we have our add.html page that has a form to submit tasks but the button submit does nothing, to change that, we add actions to the form tag and method POST. That method is used to send data to the server. In this form, django will throw an error if we don't add the csrf_token tag. While it may not matter for a simple form as one that adds tasks, imagine forms where we add our banks info or idetities.
When we add the toke to our form, it will create tokens for every time the user submits the form and submits the form with it. It will then check if the token is valid and if it is, it will submit the form. If not, it will throw an error.

** How it secures is that the token is unique to each user and each session. So if a hacker tries to submit the form, they will not have the token since they don't know what it is and the form will not be submitted.**


** DJANGO has the token builtin by default under MIDDLEWARE, you can view it in the settings.py file  with other middleware.**

### {% csrf_token %}
this is a security measure to prevent cross site request forgery. It is a unique token that is generated for each user and each session. It is used to verify that the user is the one who submitted the form.

```html
<form action="{% url 'tasks:add' %}" method="post">
        {% csrf_token %}
        <input type="text" name="task">
```
### ------------------------------------------------------------------------------
Forms tend to be repetitive, so django has a way to make it easier. We can create a form class in the forms.py file and use it in the views.py file. This will make it easier to create forms and also to validate them. sO, in the views.py file add the following

- import the forms class
- create a class that inherits from forms.Form

add all the fields you want to be in the form as attributes of the class.

```python
from django import forms

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)
    # category = forms.CharField(label="Category")
```
- priority - we have added a min and max value to the priority field to make sure the user enters a value between 1 and 10. If they don't, django will throw an error. Client side validation.

After creating the form class, you can then pass it to the any function/template that needs it. In our case, we will pass it to the add function in the views.py file.

```python
def add(request):
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })
```

Then, in the template where you want the form to appear your refernce it using the form tag
{{ form }}.
it will appear as:
```html
{% extends "tasks/layout.html" %}

{% block body %}

    <h1> Add a New Task </h1>
    <form action="{% url 'tasks:add' %}" method="post">
        {% csrf_token %}
        {{ form }}
        <input type="submit" value="Add">
    </form>

{% endblock %}
```

Now all you have to do to change this form is change whats in the class in views.py and anywhere the form is used, it will be updated.

### ------------------------------------------------------------------------------
## VALIDATION
The priority field we have provided to our form, is a client side validation technique, this data is not received by the server but the web has been configured to ensure that the values needed match. But it os a good practice with forms to do both client side validation and server side validation. This is because the client side validation can be bypassed by the user. So we have to make sure that the data we receive is valid.

in the function add we will request the data user has entered through the 
** request.POST **

```python
def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })
```
- form = NewTaskForm() without any arguments just creates a new form but when we populate it with request.POST, it will populate the form with the data the user has entered.

```python
return render(request, "tasks/add.html", {
                "form": form
```
This piece of code only runs when the data is not valid. It will render the add.html page with the form and the data the user has entered. This is because the form is not valid and we want to show the user the errors they have made.

Even if the server side validation is changed while the user is still in the old form, the form will be updated with the new validation. It will throw an error if the user tries to submit the form with invalid data.

```python
from django.http import HttpResponse
from django.urls import reverse

return HttpResponseRedirect(reverse("tasks:index"))
```
This piece of code only runs when the data is valid. It will redirect the user to the index page. This is because the form is valid and we want to show the user the tasks they have entered.

The import above it is used to redirect the user to the index page. It is the same as using the url tag but it is used in the backend.

### ------------------------------------------------------------------------------
We currently have a flaw in the app, the tasks currently are a global variable, meaning that every user who visits the website sees the same tasks. You can simulate an new user with a private tab.

### ------------------------------------------------------------------------------
## SESSIONS
Sessions are a way to store data on the server. It is a way to store data for each user. It is a dictionary that is unique to each user. It is stored in the database. 
They also help the server remember the user. This is how when you log in to a website, you don't have to log in again when you go to another page. The server remembers you.

### Solution
We will use sessions to store the tasks for each user. We will create a new list for each user and store it in the session. This way, each user will have their own list of tasks.

```python
if "tasks" not in request.session:
        request.session["tasks"] = []
```
Session is a dictionary like object, we check if for this user, in their session dict, does the tasks list exist. If it doesn't, we create it and set it to an empty list.

In our index function so far, we have been using the global tasks list, we will change that to use the session tasks list.

```python
return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })
```

DjANGO stores data by default in tables (can be changed), Initially the table doesn't exists, so we need to create it. To do that, run the following command in your terminal, in the same directory as the manage.py file.

```python
python manage.py migrate
```
 This will create all the default tables. Later we will create our own tables and store our own custom data.

### ------------------------------------------------------------------------------
### INDEX PAGE
Initially we have no tasks, if we are iterating over an empty list, django allows you to add a condition to check if the list is empty. If it is, it will display a message. If not, it will display the list.

```django
<ul>
    {% for tasks in tasks %}
        <li>{{tasks}}</li>
        {% empty %}
            <li>No tasks have been added yet.</li>
    {% endfor %}
    </ul>
```