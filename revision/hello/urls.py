from django.urls import path
from . import views

#urlpatterns is the list of the allowable urls that can be accessed into.
urlpatterns = [
    path("", views.index, name="index"),
    path("david", views.david, name="david"), #david being in the url string means it is now a url and it can be accessed into.
    path("greet", views.greet, name="greet"), #<str:name> means any string of name is welcome to acess this route.
    path("<str:name>", views.half, name="half")
]
