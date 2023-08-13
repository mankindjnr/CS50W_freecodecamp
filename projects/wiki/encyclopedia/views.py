from django.shortcuts import render, redirect, reverse
from . import util
import re
from django import forms
from pprint import pprint
import random
from markdown2 import Markdown


class new_entry(forms.Form):
    title = forms.CharField(min_length=3, max_length=200, required=True)
    content = forms.CharField(min_length=50, required=True)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    markdowner = Markdown()
    req_entry = util.get_entry(title)
    if req_entry:
        content = markdowner.convert(req_entry)
        request.session['content_data'] = content
    else:
        return render(request, "encyclopedia/404.html")

    context = {
        "all_data": content
    }
    return render(request, "encyclopedia/entry.html", {
        "all_data": context,
        "title": title.upper(),
        "content": content
    })


def pattern_match(strings_list, pattern):
    match_str = [_str for _str in  strings_list if re.search(pattern, _str)]
    return match_str


def lowercase(the_list):
    return [a_list.lower() for a_list in the_list]

def search(request):
    if request.method == "GET":
        query = request.GET["q"]
        entries = lowercase(util.list_entries())
        if query.lower() in entries:
            return redirect("entry", title=query)
        else:
            match_entries = pattern_match(entries, query.lower())
            if match_entries:
                return render(request, "encyclopedia/search.html", {
                    "entries": match_entries
                })
            else:
                return redirect("index")


def create(request):
    return render(request, "encyclopedia/create_entry.html", {
        "form": new_entry
    })


def title_str(string):
    words = string.split()
    modified = [word.title() for word in words]
    return "_".join(modified)

def save_page(request):
    title = ""
    content = ""

    if request.method == "POST":
        form = new_entry(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            title = title_str(title)
            content = form.cleaned_data['content']

            current_titles = lowercase(util.list_entries())
            if title.lower() not in current_titles:
                util.save_entry(title, content)
                return redirect("entry", title=title)
            else:
                form.add_error('title', "This title already exists")
        else:
            if len(request.POST.get('title')) > 0:
                title = request.POST.get('title')
            if len(request.POST.get('content')) > 0:
                content = request.POST.get('content')

    else:
        form = new_entry()
    
    return render(request, "encyclopedia/create_entry.html", {
        "title": title,
        "content": content,
        "form": form
    })

def edit_page(request, title):
    all_data = request.session.get('content_data', None)
    
    context = {
        'title': title,
        'content': all_data
    }

    current_data = {
        "title": context['title'],
        "content": context['content']
    }

    form = new_entry(current_data)
    return render(request, "encyclopedia/edit_page.html", {
        "update": "yes",
        "title": context['title'],
        "content": context['content'],
        "form": form
    })


def update_page(request):
    title = ""
    content = ""

    if request.method == "POST":
        form = new_entry(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            title = title_str(title)
            content = form.cleaned_data['content']

            util.save_entry(title, content)
            return redirect("entry", title=title)
        else:
            if len(request.POST.get('content')) > 0:
                content = request.POST.get('content')

    else:
        form = new_entry()
    
    current_data = {
        "title": request.POST.get('title'),
        "content": content
    }
    title = request.POST.get('title')
    form = new_entry(current_data)
    return render(request, "encyclopedia/edit_page.html", {
        "update": "yes",
        "title": title,
        "content": content,
        "form": form
    })

def random_page(request):
    pages = util.list_entries()
    rand_page = random.choice(pages)
    return entry(request, rand_page)