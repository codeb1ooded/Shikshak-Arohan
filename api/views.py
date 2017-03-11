from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import random
import string
from api.models import User
from api.models import Resume
from api.forms import resumeForm

# Create your views here.
def index(req):
	data=req.POST.get('Name','')
	return HttpResponse(data)

def isValid():
	return True
def registerUserResume(req):
	if req.method == 'POST':
		form=resumeForm(req.POST)
		us = req.POST.get("username","")
		na = req.POST.get("name","")
		ag = req.POST.get("age","")
		co = req.POST.get("contactNum","")
		em = req.POST.get("email","")
		ar = req.POST.get("areaOfExpertise","")
		ad = req.POST.get("address","")
		ci = req.POST.get("city","")
		st = req.POST.get("state","")
		pr = req.POST.get("prefferedLocation","")
		qu = req.POST.get("qualification","")
		te = req.POST.get("teachingExperience","")
		cu = req.POST.get("currentSchool","")
		if isValid():
		
			try:
				q=Resume(username=us,name=na,age=ag,contactNum=co,email = em,areaOfExpertise = ar,address = ad,city = ci,state = st,prefferedLocation = pr,qualification = qu,teachingExperience = te,currentSchool =cu)
				q.save()
				return render(req, 'signUp.htm', {'user_obj': q,'is_registered':True })
			except:
				raise
				return HttpResponse("error")
	else:
		form = resumeForm()  # an unboundform
		return render(req,'signUp.htm', {'form': form})

def createUser(req):
	un = req.GET['un']
	p = req.GET['p']
	n=req.GET['n']
	
	try:
		z=User.objects.raw('SELECT * from api_user where username = "'+un+'"')[0].name

	except:
		q=User(username=un,password=p,auth12="NA",name=n)
		q.save()
		print("here")
		return JsonResponse({"Status":"Success"})
	return JsonResponse({"Status":"Fail"})


def loginUser(req): 
	un = req.GET['un']
	p = req.GET['p']
	a=''.join(random.choice(string.ascii_uppercase + string.digits+ string.ascii_lowercase) for _ in range(16))
	q="error"
	try:
		q=User.objects.raw('SELECT * from api_user where username = "'+un+'" and password = "'+p+'"')[0].name
		a=User.objects.raw('SELECT * from api_user where username = "'+un+'" and password = "'+p+'"')[0].auth12
	except:
		return JsonResponse({"Error":"UserNotFound"})
	trying=False	
	if len(a)<=5 :
		trying=True
	while(trying):
		a=''.join(random.choice(string.ascii_uppercase + string.digits+ string.ascii_lowercase) for _ in range(16))
		try:
			x=User.objects.raw('SELECT * from api_user where auth12 = "'+a+'"')[0].name
		except:
			trying = False
	w=User(username=un,password=p,name=q,auth12=a)
	w.save()
	return JsonResponse({"Authentication":a,"Name":q})


def verifyUser(req): 
	un = req.GET['un']
	a = req.GET['a']
	
	if len(a) <=5 :
		return JsonResponse({"Error":"UserNotVerified"})
	try:
		q=User.objects.raw('SELECT * from api_user where username = "'+un+'" and auth12 = "'+a+'"')[0].name
		
	except:
		return JsonResponse({"Error":"UserNotVerified"})
	
	return JsonResponse({"Success":"Authentication Successfull"})

def logoutUser(req): 
	un = req.GET['un']
	
	try:
		q=User.objects.raw('SELECT * from api_user where username = "'+un+'"')[0].name
		p=User.objects.raw('SELECT * from api_user where username = "'+un+'"')[0].password
		
	except:
		return JsonResponse({"Error":"UserNotFound"})
	w=User(username=un,password=p,name=q,auth12='NA')
	w.save()
	return JsonResponse({"Success":"Logout Successfull"})


