from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("sections/<int:num>/", views.section, name="section"),
    path("index2/", views.index2, name="index2"),
    path("scroll/", views.scroll, name="scroll")
]