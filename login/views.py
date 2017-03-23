from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf

@login_required(login_url="login/")
def home(request):
    return render(request,"home.html")


def map_function(request):
    return render(request,"rough.html")
