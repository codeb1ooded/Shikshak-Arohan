import json
from .database_operations import *
from array import *
from .arrays import *

def return_district_categories_dataset(_district_id, _to, _from):
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

    cities = cities_in_district(_district_id)

    for i in range(0, len(cities)):
        city = cities[i]
        label_dict = {}
        label_dict['label'] = city.city_name
        label_dict['link'] = "../mapcity?city=" + city.city_name + "&cityid=" + city.id + "&to=" + _to +"&from=" +_from
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


def return_district_chart(current_district, _to, _from):
    chart= {}
    chart["caption"] = current_district + " - Monitoring"
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


def district_map_function(_district_id, _district, _to, _from):
    json_district = {}
    data_district = {}

    data_district['chart'] = return_district_chart(_district, _to, _from)
    categories_dataset = return_district_categories_dataset(_district_id, _to, _from)
    data_district['categories'] = categories_dataset["categories"]
    data_district['dataset'] = categories_dataset["dataset"]

    json_district["type"] = "mscombidy2d"
    json_district["renderAt"] = "chart-container"
    json_district["width"] = "1000"
    json_district["height"] = "600"
    json_district["dataFormat"] = "json"
    json_district['dataSource'] = data_district

    return json.dumps(json_district)
