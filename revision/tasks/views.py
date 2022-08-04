from django import forms #this is when i want to create a form using djamgo. i will not need to write html tags from scratch.
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


#tasks = []  tasks is a python variable.

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    
    
# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
        
    return render(request, "tasks/index.html", {
        "tasks":request.session["tasks"] #"tasks" is the name the html template will have access to when django is rendering it.
    })
    
def add(request):
    if request.method == "POST": #checking if the request method is post, meaning if the user submits a data.
        form = NewTaskForm(request.POST) #then we figure out the form they submitted and save it in the "form" variable.
        if form.is_valid():
            task =  form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })
        
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })    