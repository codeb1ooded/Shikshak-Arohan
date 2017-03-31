import json
from .database_operations import *
from array import *
from .arrays import *

def return_city_categories_dataset(_city_id, _to, _from, _teacher_cat):
    categories_dataset = {}
    categories = []
    category_array = []
    dataset = []
    dataset1 = {}
    dataset2 = {}

    dataset1["seriesname"] = "Student-Teacher ratio"
    dataset2["seriesname"] = "Teacher Attendance Monitoring"

    data1 = []
    data2 = []

    _to_day = _to[0] + _to[1]
    _to_month = _to[3] + _to[4]
    _to_year = _to[6] + _to[7] + _to[8] + _to[9]
    _from_day = _from[0] + _from[1]
    _from_month = _from[3] + _from[4]
    _from_year = _from[6] + _from[7] + _from[8] + _from[9]

    schools = schools_in_a_city(_city_id)
    max_ratio = 0.0

    for school in schools:
        label_dict = {}
        label_dict['label'] = school.name
        label_dict['link'] = ""
        category_array.append(label_dict)
        data1_ = {}
        ratio = student_teacher_ratio_school(school, _teacher_cat)
        data1_['value'] = ratio
        data1_['displayValue'] = ratio
        data1_['showValue'] = 1
        if ratio > max_ratio:
            max_ratio = ratio
        data1.append(data1_)

    for school in schools:
        data2_ = {}
        percent = teacher_attendance_school(school, _from_day, _from_month, _from_year, _to_day, _to_month, _to_year, _teacher_cat)
        data2_['value'] = percent * max_ratio
        data2_['displayValue'] = str("{0:.2f}".format(percent * 100)) + "%"
        data2_['showValue'] = 1
        data2_['toolText'] = "Teachers' Attendance Percentage: " + str("{0:.2f}".format(percent * 100)) + "%"
        data2.append(data2_)

    dataset1["data"] = data1
    dataset2["data"] = data2
    dataset2["parentyaxis"] = "S"

    category = {}
    category['category'] = category_array
    categories.append(category)
    dataset.append(dataset1)
    dataset.append(dataset2)
    categories_dataset["categories"] = categories
    categories_dataset["dataset"] = dataset
    return categories_dataset


def return_city_chart(current_city, _to, _from):
    chart= {}
    chart["caption"] = current_city + " - Monitoring"
    if len(_from) != 0 and len(_to) != 0:
        chart["subCaption"] = _to + " : " + _from
    else:
        chart["subCaption"] = "For all the records"
    chart["pyaxisname"] = "Student teacher ratio"
    chart["syaxisname"] = "Attendance ratio"
    chart["xAxisName"] = "Schools"
    chart["showvalues"] = "0"
    chart["labelDisplay"] = "rotate"
    chart["slantLabel"] = "1"
    chart["formatNumberScale"] = "0"
    chart["sNumberPrefix"] = "$"
    chart["theme"] = "fint"
    return chart


def city_map_function(_city_id, _city, _to, _from, _teacher_cat):
    json_city = {}
    data_city = {}

    data_city['chart'] = return_city_chart(_city, _to, _from)
    categories_dataset = return_city_categories_dataset(_city_id, _to, _from, _teacher_cat)
    data_city['categories'] = categories_dataset["categories"]
    data_city['dataset'] = categories_dataset["dataset"]

    json_city["type"] = "msbar2d"
    json_city["renderAt"] = "chart-container"
    json_city["width"] = "800"
    json_city["height"] = "600"
    json_city["dataFormat"] = "json"
    json_city['dataSource'] = data_city

    return json.dumps(json_city)
