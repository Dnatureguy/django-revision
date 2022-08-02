from django.http import HttpResponse   #for us to use httpresponse, we have
from django.shortcuts import render

# Create your views here.
"""
class HttpResponse¶
In contrast to HttpRequest objects, which are created automatically by Django, 
HttpResponse objects are your responsibility. 
Each view you write is responsible for instantiating, populating, and returning an HttpResponse.

The HttpResponse class lives in the django.http module.

"""
def index(request):
    return HttpResponse("Hello, world!")
