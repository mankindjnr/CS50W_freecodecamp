from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search", views.search, name="search"),
    path("create", views.create, name="create_entry"),
    path("save_page", views.save_page, name="save_page"),
    path("edit_page/<str:title>", views.edit_page, name="edit_page"),
    path("update_page", views.update_page, name="update_page"),
    path("random_page", views.random_page, name="random_page")
]
