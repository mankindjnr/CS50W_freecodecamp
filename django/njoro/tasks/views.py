from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    # category = forms.CharField(label="Category")

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
        tasks = request.session["tasks"]
    else:
        tasks = request.session["tasks"]

    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            # category = form.cleaned_data["category"]
            # taking the data from the form and add it to the tasks list
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })
    
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })
