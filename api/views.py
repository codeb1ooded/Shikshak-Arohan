from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import random
import string
from .models import *
from datetime import datetime

# Create your views here.
def index(req):
	data=req.POST.get('Name','')
	return HttpResponse(data)

def isValid():
	return True


''' JSON format
username
password
name
age
contact_num
email
area_of_expertise
address
city
state
preferred_location
qualification
teaching_experience
current_school
Sample http request: http://127.0.0.1:8000/signUp?username=abcd&password=abc&name=abc&age=12&contact_num=34547&email=gasdsh&area_of_expertise=avdvs&address=andxvs&city=abvdvbns&state=delhi&preferred_location=delhi&qualification=btech&teaching_experience=3&current_school=igdtuw
'''
def createUser(req):
	_username = req.GET['username']
	_password = req.GET['password']
	_name = req.GET['name']
	_age = req.GET['age']
	_contact_num = req.GET['contact_num']
	_email = req.GET['email']
	_area_of_expertise = req.GET['area_of_expertise']
	_address = req.GET['address']
	_city = req.GET['city']
	_state = req.GET['state']
	_preferred_location = req.GET['preferred_location']
	_qualification = req.GET['qualification']
	_teaching_experience = req.GET['teaching_experience']
	_current_school = req.GET['current_school']
	query_add_user = Teacher( username = _username,
							   password = _password,
							   name = _name,
							   age = _age,
							   contactNum = _contact_num,
					   		   email = _email,
					   		   areaOfExpertise = _area_of_expertise,
					   		   address = _address,
					   		   city = _city,
					   		   state = _state,
					   		   preferredLocation = _preferred_location,
					   		   qualification = _qualification,
					   		   teachingExperience = _teaching_experience,
					   		   currentSchool = _current_school ) # foreign key need to be done
	query_add_user.save()
	query_check_user_added = Teacher.objects.filter(username = _username)
	print(qquery_check_user_added[0].username)
	return JsonResponse({"Status":"Success"})

''' JSON format
username
password
name
email
Sample http request: http://127.0.0.1:8000/api/signup/?username=abcdefgh&password=abc&name=abc&age=12&contact_num=34547&email=gasdsh
'''
def signupUser(req):
	_username = req.GET['username']
	_password = req.GET['password']
	_name = req.GET['name']
	_email = req.GET['email']

	query_check_user = Teacher.objects.filter(username = _username)
	if len(query_check_user) >= 1:
		return JsonResponse({"access_token":"N/A", "name":_name, "username":_username}, status=400)

	_access_token = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
	query_add_user = Teacher( username = _username,
							   password = _password,
							   accessToken = _access_token,
							   name = _name,
							   email = _email)
	query_add_user.save()
	query_check_user_added = Teacher.objects.filter(username = _username)
	print(query_check_user_added[0].username)
	return JsonResponse({"access_token":_access_token, "name":_name, "username":_username}, status=200)


''' JSON format
username
password
'''
def loginUser(req):
	_username = req.GET['username']
	_password = req.GET['password']
	_access_token = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
	try:
		query_check_user = Teacher.objects.filter(username = _username)[0].username
	except:
		return JsonResponse({"Error":"UserNotFound"})

	query_get_user = Teacher.objects.filter(username = _username)[0]
	password_in_db = query_get_user.password
	_name = query_get_user.name
	if(password_in_db == _password):
		Teacher.objects.filter(username = _username).update ( username = _username, accessToken = _access_token)
		return JsonResponse({"access_token":_access_token, "name":_name, "username":_username})
	else:
		return JsonResponse({"Error":"Passwords don't match"})

''' JSON format
username
access_token
'''
def verifyUser(req):
	_username = req.GET['username']
	_access_token = req.GET['access_token']

	try:
		query_check_user = Teacher.objects.filter(username = _username)[0]
		if (query_check_user.accessToken == _access_token) :
			return JsonResponse({"Error":"Authentication Not Successfull"})
		else:
			return JsonResponse({"Success":"User not verified"})
	except:
		return JsonResponse({"Error":"User not present"})

''' JSON format
username
access_token
'''
def logoutUser(req):
	_username = req.GET['username']
	_access_token = req.GET['access_token']
	try:
		query_get_user = Teacher.objects.filter(username = _username)[0]
		if(query_get_user.accessToken == _access_token):
			Teacher.objects.filter(username = _username).update ( username = _username, accessToken = 'N/A')
			return JsonResponse({'status':'true','message':"Logout Successfull"}, status=200)
		else:
			return JsonResponse({'status':'false','message':"Access Token don't match"}, status=400)
	except:
		return JsonResponse({'status':'false','message':"User not present"}, status=404)

''' JSON format
teacher_username
date
latitude
longitude
accuracy
presence
Sample http request: http://127.0.0.1:8000/api/markattendance/?teacher_username=abcd&date=2012-10-09&latitude=12.11&longitude=340.99&accuracy=80&presence=1
'''
def markAttendance(request):
	_teacher_username = request.GET['teacher_username']
	_date = request.GET['date']
	_latitude = float(request.GET['latitude'])
	_longitude = float(request.GET['longitude'])
	_accuracy = float(request.GET['accuracy'])
	_presence = int(request.GET['presence'])

	try:
		query_check_user = Teacher.objects.filter(username = _teacher_username)[0]
		query_add_attendance = Attendance(
									teacher_username = query_check_user,
									date = datetime.strptime(_date, "%Y-%m-%d").date(),
									latitude = _latitude,
									longitude = _longitude,
									accuracy = _accuracy,
									presence = _presence)
		query_add_attendance.save()
		return JsonResponse({'status':'true','message':"User attendance added successfully"}, status=200)
	except:
		return JsonResponse({'status':'false','message':"User not present"}, status=404)
