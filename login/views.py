from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
import json
from api.models import *
from login.models import *
from array import *
from .map import main_map_function

@login_required(login_url="login/")
def home(request):
    return render(request,"home.html")


def map_function(request):
    json = main_map_function()
    return render(request,"rough.html", {'json_map':json})
