from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
import time

def index(request):
    return render(request, "infinitescroll/index.html")

def animate(request):
    return render(request, "infinitescroll/animate.html")

def react(request):
    return render(request, "infinitescroll/react.html")

def counter(request):
    return render(request, "infinitescroll/counter.html")

def addition(request):
    return render(request, "infinitescroll/addition.html")

def posts(request):
    
    # get start and end posts
    start = int(request.GET.get("start") or 0)
    end = int(request.GET.get("end") or (start + 9))

    # generate list of posts
    data = []
    for i in range(start, end + 1):
        data.append(f"Post #{i}")

    # artificial delay speed of response
    time.sleep(1)

    return JsonResponse({
        "posts": data
    })