import json
from .database_operations import *
from array import *
from .arrays import *

def return_city_categories_dataset(_city_id, _to, _from):
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

    schools = schools_in_a_city(_city_id)

    for i in range(0, len(schools)):
        school = schools[i]
        label_dict = {}
        label_dict['label'] = school.name
        label_dict['link'] = ""
        category_array.append(label_dict)
        data1_ = {}
        data1_['value'] = i * 1000 + 2*i
        data1.append(data1_)
        data2_ = {}
        data2_['value'] = 2*i - 0.1 *i
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
    chart["xAxisName"] = "Cities"
    chart["showvalues"] = "0"
    chart["labelDisplay"] = "rotate"
    chart["slantLabel"] = "1"
    chart["formatNumberScale"] = "0"
    chart["sNumberPrefix"] = "$"
    chart["theme"] = "fint"
    return chart


def city_map_function(_city_id, _city, _to, _from):
    json_city = {}
    data_city = {}

    data_city['chart'] = return_city_chart(_city, _to, _from)
    categories_dataset = return_city_categories_dataset(_city_id, _to, _from)
    data_city['categories'] = categories_dataset["categories"]
    data_city['dataset'] = categories_dataset["dataset"]

    json_city["type"] = "mscombidy2d"
    json_city["renderAt"] = "chart-container"
    json_city["width"] = "800"
    json_city["height"] = "600"
    json_city["dataFormat"] = "json"
    json_city['dataSource'] = data_city

    return json.dumps(json_city)
