from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.contrib.auth.models import User
import json
import string
from api.models import *
from login.models import *
from array import *
from api.models import *
from login.models import *
from datetime import date
from login.forms import schoolAdd, LoginForm
from map.country import *
from map.district import *
from map.state import *
from map.city import *
import random
from datetime import datetime
import time

@login_required(login_url="login/")
def home(request):
    return render(request,"home.html")


def map_country_function(request):
    _to = 'undefined'
    _from = 'undefined'
    _teacher_cat = 'undefined'
    if 'to' in request.GET:                     _to = request.GET['to']
    if 'from' in request.GET:                   _from = request.GET['from']
    if 'teachercategory' in request.GET:        _teacher_cat = request.GET['teachercategory']

    if _to == 'undefined':                       _to = '01-01-2000'
    if _from == 'undefined':                     _from = time.strftime("%d-%m-%Y")
    if _teacher_cat == 'undefined':              _teacher_cat = ''
    json = country_map_function(_to, _from, _teacher_cat)
    return render(request,"index.html", {'json_map':json, 'url':'../mapcountry?country=india',
                                            'to':_to, 'from':_from, 'teacher_category':_teacher_cat})


def map_state_function(request):
    if 'state' in request.GET and 'stateid' in request.GET:
        _state = request.GET['state']
        _state_id = request.GET['stateid']
        _to = 'undefined'
        _from = 'undefined'
        _teacher_cat = 'undefined'
        if 'to' in request.GET:                     _to = request.GET['to']
        if 'from' in request.GET:                   _from = request.GET['from']
        if 'teachercategory' in request.GET:        _teacher_cat = request.GET['teachercategory']

        if _to == 'undefined' or len(_to) == 0:              _to = '01-01-2000'
        if _from == 'undefined' or len(_from) == 0:          _from = time.strftime("%d-%m-%Y")
        if _teacher_cat == 'undefined':              _teacher_cat = ''

        json = state_map_function(_state_id, _state, _to, _from, _teacher_cat)
        _url = '../mapstate?state=' + _state + '&stateid=' + _state_id
        return render(request,"index.html", {'json_map':json, 'url':_url,
                                                'to':_to, 'from':_from, 'teacher_category':_teacher_cat})
    else:
        return render(request,"error400.html")


def map_district_function(request):
    if 'district' in request.GET and 'districtid' in request.GET:
        _district = request.GET['district']
        _district_id = request.GET['districtid']
        _to = 'undefined'
        _from = 'undefined'
        _teacher_cat = 'undefined'
        if _to == 'undefined' or len(_to) == 0:              _to = '01-01-2000'
        if _from == 'undefined' or len(_from) == 0:          _from = time.strftime("%d-%m-%Y")
        if 'teachercategory' in request.GET:        _teacher_cat = request.GET['teachercategory']

        json = district_map_function(_district_id, _district, _to, _from, _teacher_cat)
        _url = '../mapdistrict?district=' + _district + "&districtid=" + _district_id
        return render(request,"index.html", {'json_map':json, 'url':_url,
                                                'to':_to, 'from':_from, 'teacher_category':_teacher_cat})
    else:
        return render(request,"error400.html")


def map_city_function(request):
    if 'city' in request.GET and 'cityid' in request.GET:
        _city = request.GET['city']
        _city_id = request.GET['cityid']
        _to = 'undefined'
        _from = 'undefined'
        _teacher_cat = 'undefined'
        if _to == 'undefined' or len(_to) == 0:              _to = '01-01-2000'
        if _from == 'undefined' or len(_from) == 0:          _from = time.strftime("%d-%m-%Y")
        if 'teachercategory' in request.GET:        _teacher_cat = request.GET['teachercategory']

        json = city_map_function(_city_id, _city, _to, _from)
        _url = '../mapcity?city=' + _city + '&cityid=' + _city_id
        return render(request,"index.html", {'json_map':json, 'url':_url,
                                                'to':_to, 'from':_from, 'teacher_category':_teacher_cat})
    else:
        return render(request,"error400.html")


def test_map(request):
    json = country_map_function()
    return render(request,"index.html", {'json_map':json, 'url':'../mapcountry?country=india'})


def dummy_data(request):
    dummy = []
    dummy.append("Government High School")
    dummy.append("Government Boys Secondary School")
    dummy.append("Zilla Parishad High School Boys")
    dummy.append("Zilla Parishad High School")
    dummy.append("Govt Girls High School")
    dummy.append("Municipal School Board")
    dummy.append("Kendriya Vidyalaya")
    dummy.append("Holy Cross School")
    dummy.append("Govt Middle School")
    dummy.append("Government Girls High School Co-Op Society")
    dummy.append("M B N Govt Girls Higher Secondary School")
    dummy.append("Shri Guru Harkishan Girls School")
    dummy.append("Wesley Higher Secondary School")
    dummy.append("Garagacha Sishu Bharati High School")
    dummy.append("Pratibha Sr. Seconday School")
    dummy.append("Sinnatha Govt Girls Hr Sec School")
    dummy.append("Arignar Anna Govt Hr Sec School")
    num = random.randint(10,20)
    cities = City.objects.filter(district_foreign_id = '010011')
    for city in cities:
        city_id = city.id
        city_name = city.city_name
        print (city_id + "\t" + city_name)
        for i in range(0, num):
            print( username)
            password = 'qwertyuiop'
            j = random.randint(0, len(dummy)-1)
            name = dummy[j]
            query_add_user = User(username = username, password = password)
            query_add_user.save()
            SchoolUser.objects.filter(user = query_add_user).update (
    									user = query_add_user,
    									name = name,
                                        state = "Delhi",
                                        state_id = "010",
                                        district = "East Delhi",
                                        district_id = "010011",
                                        city = city_name,
                                        city_id = city_id,
                                        numOfStudents = random.randint(500, 1000),
                                        numOfTeachers = random.randint(10, 500),
                                        )
    return render(request,"index.html", {'json_map':'', 'url':'../mapcountry?country=india'})

def AddSchool(req):
    username=" "
    
    if not req.user.is_authenticated() :
        return render(req,'login.html')
    check=req.user.username
    set_admin =["admin"]
    if not req.user.is_superuser:
    	return render(req,'login.html')
    print(req.user.username)
    if req.method == 'POST':

        
        
        form=schoolAdd(req.POST)
        pass1=req.POST.get('pass1',"")
        name = req.POST.get("name","")
        state_id = req.POST.get("state","")
        state_name=State.objects.get(id=state_id).getName()
        city_id = req.POST.get("city","")
        timing = req.POST.get("timing","")
        address = req.POST.get("address","")
        city_name=City.objects.get(id=city_id).getName()
        district_id = req.POST.get("district","")
        numOfStudents = req.POST.get("numOfStudents","")
        numOfTeachers = req.POST.get("numOfTeachers","")
        longitude = req.POST.get("longitude","")
        latitude = req.POST.get("latitude","")
        wifi_zone = req.POST.get("wifi_zone","")
        district_name=District.objects.get(id=district_id).getName()
        trying=True
        i=0
        while(trying):
            username = city_id + '0'
            if i < 9:
                username = username + "0" + str(i+1)
            else:
                username = username + str(i+1)
            i+=1
            try:
                x=User.objects.raw('SELECT * from auth_user where username = "'+username+'"')[0].username
            except:
                trying = False
        w=User(username=username,password=pass1)
        w.set_password(pass1)
        w.is_staff=True
        w.save()
        print (state)
        try:
            q=SchoolUser(user=w,name=name,timing=timing, address=address,state=state_name,state_id= state_id,district=district_name, district_id=district_id,city=city_name,city_id=city_id,numOfStudents=numOfStudents,numOfTeachers=numOfTeachers,latitude=latitude,longitude=longitude,wifi_zone=wifi_zone)
            q.save()
            return render(req, 'school.htm', {'user_name': username, 'pass':pass1,'is_registered':True })
        except:
            raise
            return render(req, 'error')
    else:
        form = schoolAdd()  # an unboundform
        return render(req,'school.htm', {'form': form})


def dummy_teacher(request):
    cat = []
    cat.append('primary')
    cat.append('secondary')
    cat.append('senior')
    schools = SchoolUser.objects.all()
    for i in range(0, 1000):
        _school = schools[random.randint(0, len(schools)-1)]
        print (_school.city)
        _username = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(16))
        _password = 'qwertyuiop'
        _category = cat[random.randint(0, 2)]
        teacher = Teacher(
                            username = _username,
                        	password = _password,
                        	accessToken = "N/A",
                        	name = _username,
                        	category = _category,
                        	email = _username + "@gmail.com",
                        	age = random.randint(30,50),
                        	currentSchool  = _school
                            )
        teacher.save()
    return render(request,"index.html", {'json_map':'', 'url':'../mapcountry?country=india'})


def dummy_attendance(request):
    teacher = Teacher.objects.all()
    for i in range(0, 50000):
        _teacher = teacher[random.randint(0, len(teacher)-1)]
        year = random.choice(range(2000, 2017))
        month = random.choice(range(1, 13))
        day = random.choice(range(1, 29))
        date = datetime(year, month, day)
        Attendance_Present(teacher_username=_teacher, date=date).save()
    return render(request,"index.html", {'json_map':'', 'url':'../mapcountry?country=india'})



def dummy_attendance_holiday(request):
    school = SchoolUser.objects.all()
    for i in range(0, 1000):
        _school = school[random.randint(0, len(school)-1)]
        year = random.choice(range(2000, 2017))
        month = random.choice(range(1, 13))
        day = random.choice(range(1, 29))
        date = datetime(year, month, day)
        Attendance_Holiday(school_user=_school, date=date).save()
    return render(request,"index.html", {'json_map':'', 'url':'../mapcountry?country=india'})
