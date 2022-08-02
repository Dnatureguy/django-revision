from django.urls import path
from . import views

#urlpatterns is the list of the allowable urls that can be accessed into.
urlpatterns = [
    path("", views.index, name="index")
]
