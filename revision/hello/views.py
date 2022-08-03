from django.http import HttpResponse   #for us to use httpresponse, we have to import httpresponse
from django.shortcuts import render

# Create your views here.
"""
class HttpResponse¶
In contrast to HttpRequest objects, which are created automatically by Django, 
HttpResponse objects are your responsibility. 
Each view you write is responsible for instantiating, populating, and returning an HttpResponse.
HttpResponse is only used to request for strings and not files.
The HttpResponse class lives in the django.http module.
Rendering of strings is when HttpResponse comes in. Now to render an entire html file, the use of render functionj is needed.
"""
def index(request):
    return render(request, "hello/index.html") #to render an html file, you pass in a request and then an template.

def david(request):
    return HttpResponse("Hi, david!")

def greet(request, name): #remember a function can have more than two arguments, here "name" is trying to be  placeholder.
    return HttpResponse(f"Hello, {name.capitalize()}") #now,"name" is added to represent any other string.

def half(request, name):
    return render(request, "hello/half.html", {
        "name": name.capitalize()
    }) #Now, there was an optional third argument in the render function, it being the context.
       #Context contains the information or variables that i want the template to have access to.
       #"Name" is the key to the value to capitalize the second argument to request function.