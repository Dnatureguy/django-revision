from django.shortcuts import render

import datetime #import the calender in order to be able to use it in this code. 


# Create your views here.

def index(request):
    now = datetime.datetime.now()
    return render(request, "newyear/index.html", {
        "newyear": now.month == 1 and now.day == 1
    })
"""
So basically, when the function "datetime..." finishes running and saves the result in the
variable "now". if the context "now.month" is equal to 1 then the value of the variable "newyear"
is going true when the template gets access to it.

"""