from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import random
import string
from .models import *
from datetime import datetime
from login.models import *
from django.contrib.auth.models import User

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
access_token
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
Sample http request: (create) http://127.0.0.1:8000/
'''
def updateUserDetails(req):
	_username = req.GET['username']
	_access_token = req.GET['access_token']
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

	try:
		query_check_user = Teacher.objects.filter(username = _username)[0]
		if (query_check_user.accessToken == _access_token) :
			Teacher.objects.filter(username = _username).update (
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
								 					   		   currentSchool = _current_school )
			return JsonResponse({"status":"updated", "message":"user data updated successfully"}, status=200)
		else:
			return JsonResponse({"status":"error", "message":"user not authenticated"}, status=403)
	except:
		return JsonResponse({"status":"error", "message":"user not present"}, status=404)


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
		return JsonResponse({"message":"user not found", "access_token":"N/A", "name":"N/A", "username":_username}, status=404)

	query_get_user = Teacher.objects.filter(username = _username)[0]
	password_in_db = query_get_user.password
	_name = query_get_user.name
	if(password_in_db == _password):
		Teacher.objects.filter(username = _username).update ( username = _username, accessToken = _access_token)
		return JsonResponse({"message":"login done, access token granted", "access_token":_access_token, "name":_name, "username":_username}, status=200)
	else:
		return JsonResponse({"message":"wrong password", "access_token":"N/A", "name":"N/A", "username":_username}, status=400)


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
latitude_1
longitude_1
latitude_2
longitude_2
latitude_3
longitude_3
latitude_4
longitude_4
accuracy
presence
Sample http request: http://127.0.0.1:8000/api/markattendance/?teacher_username=abcd&date=2012-10-09&latitude=12.11&longitude=340.99&accuracy=80&presence=1
'''
def markAttendance(request):
	_teacher_username = request.GET['teacher_username']
	_date = request.GET['date']
	_latitude_1 = float(request.GET['latitude_1'])
	_longitude_1 = float(request.GET['longitude_1'])
	_latitude_2 = float(request.GET['latitude_2'])
	_longitude_2 = float(request.GET['longitude_2'])
	_latitude_3 = float(request.GET['latitude_3'])
	_longitude_3 = float(request.GET['longitude_3'])
	_latitude_4 = float(request.GET['latitude_4'])
	_longitude_4 = float(request.GET['longitude_4'])
	_accuracy = float(request.GET['accuracy'])
	_presence = int(request.GET['presence'])

	try:
		query_check_user = Teacher.objects.filter(username = _teacher_username)[0]
		query_add_attendance = Attendance(
									teacher_username = query_check_user,
									date = datetime.strptime(_date, "%Y-%m-%d").date(),
									latitude_1 = _latitude_1,
									longitude_1 = _longitude_1,
									latitude_2 = _latitude_2,
									longitude_2 = _longitude_2,
									latitude_3 = _latitude_3,
									longitude_3 = _longitude_3,
									latitude_4 = _latitude_4,
									longitude_4 = _longitude_4,
									accuracy = _accuracy,
									presence = _presence)
		query_add_attendance.save()
		return JsonResponse({'status':'true','message':"User attendance added successfully"}, status=200)
	except:
		return JsonResponse({'status':'false','message':"User not present"}, status=404)

''' JSON format
username
access_token
'''
def isSchoolAdded(request):
	_username = request.GET['username']
	_access_token = request.GET['access_token']
	try:
		teacher = Teacher.objects.filter(username = _username)[0]
		if(teacher.accessToken == _access_token):
			school = teacher.currentSchool
			if school is not null:
				return JsonResponse({'status':'true','message':"school present", 'school_username':school.user.username}, status=200)
			else:
				return JsonResponse({'status':'true','message':"no school", 'school_username':'N/A'}, status=200)
	except:
		return JsonResponse({'status':'false','message':"User not present"}, status=404)


''' JSON format
username
access_token
school_username
Sample http request: http://127.0.0.1:8000/api/addschool?username=abcdefgh&access_token=jXL9F2iL0j2Agjou&school_username=abcd
'''
def addSchoolToUser(request):
	_username = request.GET['username']
	_access_token = request.GET['access_token']
	_school_username = request.GET['school_username']
	try:
		query_get_user = Teacher.objects.filter(username = _username)[0]
		if(query_get_user.accessToken == _access_token):
			try:
				query_get_school_user = User.objects.filter(username = _school_username)[0]
				query_get_user_in_school_table = SchoolUser.objects.filter(user = query_get_school_user)[0]
				Teacher.objects.filter(username = _username).update ( username = _username, currentSchool = query_get_user_in_school_table)
				return JsonResponse({'status':'true','message':"school added successfully"}, status=200)
			except:
				return JsonResponse({'status':'false','message':"School username not present"}, status=404)
		else:
			return JsonResponse({'status':'false','message':"Access Token don't match"}, status=400)
	except:
		return JsonResponse({'status':'false','message':"User not present"}, status=404)


''' JSON format
username
access_token
school_username
Sample http request: http://127.0.0.1:8000/api/latlong?username=abcdefgh&access_token=jXL9F2iL0j2Agjou&school_username=abcd
'''
def getLatLong(request):
	_username = request.GET['username']
	_access_token = request.GET['access_token']
	_school_username = request.GET['school_username']
	try:
		query_get_user = Teacher.objects.filter(username = _username)[0]
		if(query_get_user.accessToken == _access_token):
			try:
				query_get_school_user = User.objects.filter(username = _school_username)[0]
				query_get_user_in_school_table = SchoolUser.objects.filter(user = query_get_school_user)[0]
				_latitude = query_get_user_in_school_table.latitude
				_longitude = query_get_user_in_school_table.longitude
				return JsonResponse({'status':'true','message':"school data returned successfully",
						'latitude':_latitude, 'longitude':_longitude}, status=200)
			except:
				return JsonResponse({'status':'false','message':"School username not present"}, status=404)
		else:
			return JsonResponse({'status':'false','message':"Access Token don't match"}, status=400)
	except:
		return JsonResponse({'status':'false','message':"User not present"}, status=404)


''' JSON format
username
access_token
school_username
from_day
from_month
from_year
to_day
to_month
to_year
Sample http request: http://127.0.0.1:8000/api/presentholidays/?username=random1&access_token=abcdefgh&school_username=megha&from_day=8&from_month=3&from_year=2017&to_day=23&to_month=3&to_year=2017
'''
def getPresentAndHolidays(request):
	_username = request.GET['username']
	_access_token = request.GET['access_token']
	_school_username = request.GET['school_username']
	_from_year = request.GET['from_year']
	_from_month = request.GET['from_month']
	_from_day = request.GET['from_day']
	_to_year = request.GET['to_year']
	_to_month = request.GET['to_month']
	_to_day = request.GET['to_day']
	try:
		_query_get_teacher = Teacher.objects.filter(username = _username)[0]
		_query_get_school_user = User.objects.filter(username = _school_username)[0]
		_query_get_school = SchoolUser.objects.filter(user = _query_get_school_user)[0]
		if(_query_get_teacher.accessToken == _access_token):
			_present_dates = Attendance_Present.objects.filter(teacher_username = _query_get_teacher,
								date__range=[_from_year+"-"+_from_month+"-"+_from_day, _to_year+"-"+_to_month+"-"+_to_day])
			_holiday_dates = Attendance_Holiday.objects.filter(school_user = _query_get_school,
								date__range=[_from_year+"-"+_from_month+"-"+_from_day, _to_year+"-"+_to_month+"-"+_to_day])

			_present_dates_array = []
			_holiday_dates_array = []

			for date in _present_dates:
				_present_date = {'year': date.date.year,
								 'month': date.date.month,
								 'day': date.date.day }
				_present_dates_array.append(_present_date)

			for date in _holiday_dates:
				_holiday_date = {'year': date.date.year,
								 'month': date.date.month,
								 'day': date.date.day }
				_holiday_dates_array.append(_holiday_date)

			return JsonResponse({'status':'true','message':"school data returned successfully",
								  'present':_present_dates_array, 'holiday':_holiday_dates_array}, status=200)
		else:
			return JsonResponse({'status':'false','message':"Access Token don't match"}, status=400)
	except:
		return JsonResponse({'status':'false','message':"User not present"}, status=404)
