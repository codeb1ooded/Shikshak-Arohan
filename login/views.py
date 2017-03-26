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
from map.country import *
from map.district import *
from map.state import *
from map.city import *

@login_required(login_url="login/")
def home(request):
    return render(request,"home.html")


def map_country_function(request):
    _to = 'undefined'
    _from = 'undefined'
    if 'to' in request.GET and 'from' in request.GET:
        _to = request.GET['to']
        _from = request.GET['from']
    if _to == 'undefined': _to =''
    if _from == 'undefined': _from =''
    json = country_map_function(_to, _from)
    return render(request,"index.html", {'json_map':json, 'url':'../mapcountry?country=india', 'to':_to, 'from':_from})


def map_state_function(request):
    if 'state' in request.GET and 'stateid' in request.GET:
        _state = request.GET['state']
        _state_id = request.GET['stateid']
        _to = 'undefined'
        _from = 'undefined'
        if 'to' in request.GET and 'from' in request.GET:
            _to = request.GET['to']
            _from = request.GET['from']

        if _to == 'undefined': _to =''
        if _from == 'undefined': _from =''

        json = state_map_function(_state_id, _state, _to, _from)
        _url = '../mapstate?state=' + _state + '&stateid=' + _state_id
        return render(request,"index.html", {'json_map':json, 'url':_url, 'to':_to, 'from':_from})
    else:
        return render(request,"error400.html")


def map_district_function(request):
    if 'district' in request.GET and 'districtid' in request.GET:
        _district = request.GET['district']
        _district_id = request.GET['districtid']
        _to = 'undefined'
        _from = 'undefined'
        if 'to' in request.GET and 'from' in request.GET:
            _to = request.GET['to']
            _from = request.GET['from']

        if _to == 'undefined': _to =''
        if _from == 'undefined': _from =''

        json = district_map_function(_district_id, _district, _to, _from)
        _url = '../mapdistrict?district=' + _district + "&districtid=" + _district_id
        return render(request,"index.html", {'json_map':json, 'url':_url, 'to':_to, 'from':_from})
    else:
        return render(request,"error400.html")


def map_city_function(request):
    if 'city' in request.GET and 'cityid' in request.GET:
        _city = request.GET['city']
        _city_id = request.GET['cityid']
        _to = 'undefined'
        _from = 'undefined'
        if 'to' in request.GET and 'from' in request.GET:
            _to = request.GET['to']
            _from = request.GET['from']

        if _to == 'undefined': _to =''
        if _from == 'undefined': _from =''

        json = city_map_function(_city_id, _city, _to, _from)
        _url = '../mapcity?city=' + _city + '&cityid=' + _city_id
        return render(request,"index.html", {'json_map':json, 'url':_url, 'to':_to, 'from':_from})
    else:
        return render(request,"error400.html")


def test_map(request):
    json = country_map_function()
    return render(request,"index.html", {'json_map':json, 'url':'../mapcountry?country=india'})
