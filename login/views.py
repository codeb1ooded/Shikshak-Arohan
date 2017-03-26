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
from .map import *

@login_required(login_url="login/")
def home(request):
    return render(request,"home.html")


def map_country_function(request):
    json = country_map_function()
    return render(request,"index.html", {'json_map':json, 'url':'../mapcountry?country=india'})


def map_state_function(request):
    _state = request.GET['state']
    json = state_map_function(_state)
    return render(request,"index.html", {'json_map':json, 'url':'../mapstate?state='+_state})


def map_district_function(request):
    _district = request.GET['district']
    json = district_map_function(_district)
    return render(request,"index.html", {'json_map':json, 'url':'../mapdistrict?district='+_district})


def map_city_function(request):
    _city = request.GET['city']
    json = city_map_function(_city)
    return render(request,"index.html", {'json_map':json, 'url':'../mapcity?city='+_city})


def test_map(request):
    json = country_map_function()
    return render(request,"index.html", {'json_map':json, 'url':'../mapcountry?country=india'})
