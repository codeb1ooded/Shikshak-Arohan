from api.models import *
from login.models import *
from datetime import date

def districts_in_state(_state_id):
    return District.objects.filter(state_foreign_id = _state_id)

def cities_in_district(_district_id):
    return City.objects.filter(district_foreign_id = _district_id)

def schools_in_a_state(_state_id):
    return SchoolUser.objects.filter(state_id = _state_id)


def schools_in_a_district(_district_id):
    return SchoolUser.objects.filter(district_id = _district_id)


def schools_in_a_city(_city_id):
    return SchoolUser.objects.filter(city_id = _city_id)


def student_teacher_ratio_school(school, _teacher_cat):
    _students = school.numOfStudentsPrimary + school.numOfStudentsSeconadry + school.numOfStudentsSenior
    _teachers = school.numOfTeachers
    if _teacher_cat == 'primary':
        _students = school.numOfStudentsPrimary
        _teachers = len(Teacher.objects.filter(currentSchool=school, category=_teacher_cat))
    elif _teacher_cat == 'secondary':
        _students = school.numOfStudentsSeconadry
        _teachers = len(Teacher.objects.filter(currentSchool=school, category=_teacher_cat))
    elif _teacher_cat == 'senior':
        _students = school.numOfStudentsSenior
        _teachers = len(Teacher.objects.filter(currentSchool=school, category=_teacher_cat))
    else:
        _students = school.numOfStudentsPrimary + school.numOfStudentsSeconadry + school.numOfStudentsSenior
    try:
        return _students / _teachers
    except:
        return 0


def student_teacher_ratio_city(city_id, _teacher_cat):
    school_city = schools_in_a_city(city_id)
    ratio = 0
    for school in school_city:
        ratio += student_teacher_ratio_school(school, _teacher_cat)
    return float(ratio) / float(len(school_city))


def student_teacher_ratio_district(district_id, _teacher_cat):
    school_district = schools_in_a_district(district_id)
    ratio = 0
    for school in school_district:
        ratio += student_teacher_ratio_school(school, _teacher_cat)
    try:
        return float(ratio) / float(len(school_district))
    except:
        return 0


def student_teacher_ratio_state(state_id, _teacher_cat):
    school_state = schools_in_a_state(state_id)
    ratio = 0
    for school in school_state:
        ratio += student_teacher_ratio_school(school, _teacher_cat)
    try:
        return float(ratio) / float(len(school_state))
    except:
        return 0


def present_days_of_teacher(_teacher, _from_day, _from_month, _from_year, _to_day, _to_month, _to_year):
    _present_dates = Attendance_Present.objects.filter(teacher_username = _teacher,
                        date__range=[_to_year+"-"+_to_month+"-"+_to_day, _from_year+"-"+_from_month+"-"+_from_day])
    _present = len(_present_dates)
    return _present


def teacher_attendance_school(_school, _from_day, _from_month, _from_year, _to_day, _to_month, _to_year, _teacher_cat):

    holidays = Attendance_Holiday.objects.filter(school_user = _school,
                        date__range=[_from_year+"-"+_from_month+"-"+_from_day, _to_year+"-"+_to_month+"-"+_to_day])
    _num_of_holidays = len(holidays)

    _total_days = (date(int(_from_year), int(_from_month), int(_from_day)) - date(int(_to_year), int(_to_month), int(_to_day))).days

    _teachers_in_school = Teacher.objects.filter(currentSchool = _school)
    if _teacher_cat == 'primary':
        _teachers_in_school = Teacher.objects.filter(currentSchool=_school, category=_teacher_cat)
    elif _teacher_cat == 'secondary':
        _teachers_in_school = Teacher.objects.filter(currentSchool=_school, category=_teacher_cat)
    elif _teacher_cat == 'senior':
        _teachers_in_school = Teacher.objects.filter(currentSchool=_school, category=_teacher_cat)
    _total_teachers = len(_teachers_in_school)
    _total_attendence_ratio = 0
    for teacher in _teachers_in_school:
        attendance = present_days_of_teacher(teacher, _from_day, _from_month, _from_year, _to_day, _to_month, _to_year)
        try:
            attendance_ratio = (float(attendance) / float((_total_days - _num_of_holidays)))
            _total_attendence_ratio += attendance_ratio
        except:
            _total_attendence_ratio = _total_attendence_ratio
    try:
        return float(_total_attendence_ratio) / float(_total_teachers)
    except:
        return 0


def teacher_attendance_city(city_id, _from_day, _from_month, _from_year, _to_day, _to_month, _to_year, _teacher_cat):
    school_city = schools_in_a_city(city_id)
    ratio = 0
    num_of_schools = len(school_city)
    for school in school_city:
        ratio += teacher_attendance_school(school, _from_day, _from_month, _from_year, _to_day, _to_month, _to_year, _teacher_cat)
    try:
        ratio = float(ratio) / float(num_of_schools)
        return ratio
    except:
        return 0


def teacher_attendance_district(district_id, _from_day, _from_month, _from_year, _to_day, _to_month, _to_year, _teacher_cat):
    school_district = schools_in_a_district(district_id)
    ratio = 0
    num_of_schools = len(school_district)
    for school in school_district:
        ratio += teacher_attendance_school(school, _from_day, _from_month, _from_year, _to_day, _to_month, _to_year, _teacher_cat)
    try:
        ratio = float(ratio) / float(num_of_schools)
        return ratio
    except:
        return 0

def teacher_attendance_state(state_id, _from_day, _from_month, _from_year, _to_day, _to_month, _to_year, _teacher_cat):
    school_state = schools_in_a_state(state_id)
    ratio = 0
    num_of_schools = len(school_state)
    for school in school_state:
        ratio += teacher_attendance_school(school, _from_day, _from_month, _from_year, _to_day, _to_month, _to_year, _teacher_cat)
    try:
        ratio = float(ratio) / float(num_of_schools)
        return ratio
    except:
        return 0
