from django.urls import path

from . import views

urlpatterns = [ 
    path('', views.index, name='index'),
    path('posts', views.posts, name='posts'),
    path('animate', views.animate, name='animate'),
    path('react', views.react, name='react'),
    path('counter', views.counter, name='counter'),
    path('addition', views.addition, name='addition')
]