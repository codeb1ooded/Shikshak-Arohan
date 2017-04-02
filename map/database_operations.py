from api.models import *
from login.models import *
from datetime import date
from django.contrib.auth.models import User

RED = "#ff0000"
BLUE = "#00ff00"
GREEN = "#0000ff"

def districts_in_state(_state_id):
    state = State.objects.filter(id=_state_id)[0]
    return District.objects.filter(state_foreign_id = state)


def cities_in_district(_district_id):
    district = District.objects.filter(id=_district_id)[0]
    return City.objects.filter(district_foreign_id = district)


def schools_in_a_state(_state_id):
    print _state_id
    state = State.objects.filter(id=_state_id)[0]
    return SchoolUser.objects.filter(state_instance = state)


def schools_in_a_district(_district_id):
    district = District.objects.filter(id=_district_id)[0]
    return SchoolUser.objects.filter(district_instance = district)


def schools_in_a_city(_city_id):
    city = City.objects.filter(id=_city_id)[0]
    return SchoolUser.objects.filter(city_instance = city)


def teachers_in_school(_school_username):
    _user = User.objects.filter(username=_school_username)[0]
    _school_user = SchoolUser.objects.filter(user=_user)[0]
    _teacher_list = Teacher.objects.filter(currentSchool=_school_user)
    return _teacher_list


def student_teacher_ratio_school(school, _teacher_cat):
    _students = school.numOfStudentsPrimary + school.numOfStudentsSecondary + school.numOfStudentsSenior
    _teachers = school.numOfTeachersPrimary + school.numOfTeachersSecondary + school.numOfTeachersSenior
    if _teacher_cat == 'primary':
        _students = school.numOfStudentsPrimary
        _teachers = len(Teacher.objects.filter(currentSchool=school, category=_teacher_cat))
    elif _teacher_cat == 'secondary':
        _students = school.numOfStudentsSecondary
        _teachers = len(Teacher.objects.filter(currentSchool=school, category=_teacher_cat))
    elif _teacher_cat == 'senior':
        _students = school.numOfStudentsSenior
        _teachers = len(Teacher.objects.filter(currentSchool=school, category=_teacher_cat))
    else:
        _students = school.numOfStudentsPrimary + school.numOfStudentsSecondary + school.numOfStudentsSenior
    try:
        return _students / _teachers
    except:
        return 0


def student_teacher_ratio_city(city_id, _teacher_cat):
    school_city = schools_in_a_city(city_id)
    ratio = 0
    for school in school_city:
        ratio += student_teacher_ratio_school(school, _teacher_cat)
    try:
        return float(ratio) / float(len(school_city))
    except:
        return 0


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


def teacher_attendance(_teacher, _school, _from_day, _from_month, _from_year, _to_day, _to_month, _to_year):
    holidays = Attendance_Holiday.objects.filter(school_user = _school,
                        date__range=[_from_year+"-"+_from_month+"-"+_from_day, _to_year+"-"+_to_month+"-"+_to_day])
    _num_of_holidays = len(holidays)
    _total_days = (date(int(_from_year), int(_from_month), int(_from_day)) - date(int(_to_year), int(_to_month), int(_to_day))).days
    attendance = present_days_of_teacher(_teacher, _from_day, _from_month, _from_year, _to_day, _to_month, _to_year)

    data = {}
    data['name'] = _teacher.name
    data['days_present'] = attendance
    percent = float(attendance) / float((_total_days - _num_of_holidays))
    data['percent_present'] = str("{0:.2f}".format(percent * 100)) + "%"

    if percent <= 0.33:
        data['colour'] = RED
    elif percent <= 0.67:
        data['colour'] = BLUE
    else:
        data['colour'] = GREEN
    return data


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


def school_json(_school_username, _to, _from, _teacher_cat):
    _user = User.objects.filter(username = _school_username)[0]
    _school_user = SchoolUser.objects.filter(user = _user)[0]
    teachers = []

    _to_day = _to[0] + _to[1]
    _to_month = _to[3] + _to[4]
    _to_year = _to[6] + _to[7] + _to[8] + _to[9]
    _from_day = _from[0] + _from[1]
    _from_month = _from[3] + _from[4]
    _from_year = _from[6] + _from[7] + _from[8] + _from[9]

    holidays = Attendance_Holiday.objects.filter(school_user = _school_user,
                        date__range=[_from_year+"-"+_from_month+"-"+_from_day, _to_year+"-"+_to_month+"-"+_to_day])
    _num_of_holidays = len(holidays)
    _total_days = (date(int(_from_year), int(_from_month), int(_from_day)) - date(int(_to_year), int(_to_month), int(_to_day))).days

    _teachers_in_school = teachers_in_school(_school_username)
    for _teacher in _teachers_in_school:
        obj = teacher_attendance(_teacher, _school_user, _from_day, _from_month, _from_year, _to_day, _to_month, _to_year)
        teachers.append(obj)

    return {'teachers':teachers, 'name':_school_user.name, 'working_days':(_total_days - _num_of_holidays)}


import random
def state_total_teacher(_state_id):
    teacher_count = len(Teacher.objects.filter(state=State.objects.get(id = _state_id).state_name))
    return random.randint(30, 50)

def state_school_count(_state_id):
    return len(schools_in_a_state(_state_id))

def state_total_students(_state_id):
    student_count = len(SchoolUser.objects.filter(state_id=_state_id))
    return student_count

def state_avg_STR(_state_id):
    ratio = 0.0
    for d in District.objects.filter(state_foreign_id = _state_id):
        school_district = schools_in_a_district(d.id)

        for school in school_district:
            ratio += student_teacher_ratio_school(school, '')

    return ratio


def country_total_teachers():
    teacher_count = len(Teacher.objects.all())
    return teacher_count


def country_total_students():
    schools = SchoolUser.objects.all()
    count = 0
    for school in schools:
        count_in_school = school.numOfStudentsPrimary + school.numOfStudentsSecondary + school.numOfStudentsSenior
        count += count_in_school
    return count


def avg_STR_country():
    total = 0.0
    for s in State.objects.all():
        total += float(state_total_students(s.id))/float(state_total_teacher(s.id))

    return round(total, 2)

def country_total_schools():
    school_count = len(SchoolUser.objects.all())
    return school_count
