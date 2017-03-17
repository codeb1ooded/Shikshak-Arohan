from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import random
import string
from .models import Teacher

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
'''
def loginUser(req):
	_username = req.GET['username']
	_password = req.GET['password']
	_access_token = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
	try:
		query_check_user = Teacher.objects.filter(username = _username)[0].username
	except:
		return JsonResponse({"Error":"UserNotFound"})

	password_in_db = Teacher.objects.filter(username = _username)[0].password
	if(password_in_db == _password):
		Teacher.objects.filter(username = _username).update ( username = _username, auth12 = _access_token)
		return JsonResponse({"Authentication":_access_token, "Username":_username})
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
		if (query_check_user.auth12 == _access_token) :
			return JsonResponse({"Error":"Authentication Successfull"})
		else:
			return JsonResponse({"Success":"User Not Verified"})
	except:
		return JsonResponse({"Error":"User not present"})

''' JSON format
username
access_token
'''
def logoutUser(req):
	_username = req.GET['username']
	try:
		query_get_user = Teacher.objects.filter(username = _username)[0]
		Teacher.objects.filter(username = _username).update ( username = _username, auth12 = 'N/A')
		return JsonResponse({"Success":"Logout Successfull"})
	except:
		return JsonResponse({"Error":"User not present"})
