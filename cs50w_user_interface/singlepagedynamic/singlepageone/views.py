from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.

def index(request):
    return render(request, "singlepageone/index.html")

texts = ["This is the first section", "This is the second section", "This is the third section"
, "This is the fourth section", "This is the fifth section"]

def index2(request):
    return render(request, "singlepageone/index2.html")

def section(request, num):
    if 1 <= num <= 5:
        return HttpResponse(texts[num - 1])
    else:
        raise Http404("Section not found")

def scroll(request):
    return render(request, "singlepageone/scroll.html")