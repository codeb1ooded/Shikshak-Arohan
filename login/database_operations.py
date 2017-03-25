from api.models import *
from login.models import *
from datetime import date

def districts_in_state(_state_id):
    return District.objects.filter(state_id = _state_id)

def schools_in_a_state(_state_id):
    return SchoolUser.objects.filter(state_id = _state_id)


def schools_in_a_district(_district_id):
    return SchoolUser.objects.filter(district_id = _district_id)


def schools_in_a_city(_city_id):
    return SchoolUser.objects.filter(city_id = _city_id)


def student_teacher_ratio_school(school):
    _students = school.numOfStudents
    _teachers = school.numOfTeachers
    _ratio = _students / _teachers
    return _ratio


def student_teacher_ratio_city(city_id):
    school_city = schools_in_a_city(city_id)
    ratio = 0
    for school in school_city:
        ratio += student_teacher_ratio_school(school)
    return ratio


def student_teacher_ratio_district(district_id):
    school_district = schools_in_a_district(district_id)
    ratio = 0
    for school in school_district:
        ratio += student_teacher_ratio_school(school)
    return ratio


def student_teacher_ratio_state(state_id):
    school_state = schools_in_a_state(state_id)
    ratio = 0
    for school in school_state:
        ratio += student_teacher_ratio_school(school)
    return ratio


def present_days_of_teacher(_teacher, _from_day, _from_month, _from_year, _to_day, _to_month, _to_year):
    _present_dates = Attendance_Present.objects.filter(teacher_username = _query_get_teacher,
                        date__range=[_from_year+"-"+_from_month+"-"+_from_day, _to_year+"-"+_to_month+"-"+_to_day])
    _present = len(_present_dates)
    return _present


def teacher_attendance_school(_school, _from_day, _from_month, _from_year, _to_day, _to_month, _to_year):

    holidays = Attendance_Holiday.objects.filter(school_user = _school,
                        date__range=[_from_year+"-"+_from_month+"-"+_from_day, _to_year+"-"+_to_month+"-"+_to_day])
    _num_of_holidays = len(holidays)

    _total_days = (date(_to_year, _to_month, _to_day) - date(_from_year, _from_month, _from_day)).days

    _teachers_in_school = Teacher.objects.filter(currentSchool = _school)
    _total_teachers = len(_teachers_in_school)
    _total_attendence_ratio = 0
    for teacher in _teachers_in_school:
        attendance = present_days_of_teacher(teacher, _from_day, _from_month, _from_year, _to_day, _to_month, _to_year)
        attendance_ratio = attendance / (_total_days - _num_of_holidays) * 100
        _total_attendence_ratio += attendance_ratio
    return _total_attendence_ratio / _total_teachers


def teacher_attendance_city(city_id, _from_day, _from_month, _from_year, _to_day, _to_month, _to_year):
    school_city = schools_in_a_city(city_id)
    ratio = 0
    num_of_schools = len(school_city)
    for school in school_city:
        ratio += teacher_attendance_school(school)
    return ratio / num_of_schools


def teacher_attendance_district(district_id, _from_day, _from_month, _from_year, _to_day, _to_month, _to_year):
    school_district = schools_in_a_district(district_id)
    ratio = 0
    num_of_schools = len(school_district)
    for school in school_district:
        ratio += teacher_attendance_school(school)
    return ratio / num_of_schools


def teacher_attendance_state(state_id, _from_day, _from_month, _from_year, _to_day, _to_month, _to_year):
    school_state = schools_in_a_state(state_id)
    ratio = 0
    num_of_schools = len(school_state)
    for school in school_state:
        ratio += teacher_attendance_school(school)
    return ratio / num_of_schools
