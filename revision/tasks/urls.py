from django.urls import path
from . import views


app_name = "tasks" #to create a namespace for the index routes in all apps.
urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add") #when you call the route of add, it will reveal
]
