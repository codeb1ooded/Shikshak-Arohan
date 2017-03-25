import json
from .database_operations import *
from array import *

state = [ 'Andaman and Nicobar Islands', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam',
          'Bihar', 'Chandigarh', 'Chhattisgarh', 'Dadra and Nagar Haveli', 'Daman and Diu', 'Delhi',
          'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir', 'Jharkhand',
          'Karnataka', 'Kerala', 'Lakshadweep', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya',
          'Mizoram', 'Nagaland', 'Odisha', 'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu',
          'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal', 'Telangana']

state_ids = [ 'AndamanNicobarIslands', 'AndhraPradesh', 'ArunachalPradesh', 'Assam',
          'Bihar', 'Chandigarh', 'Chhattisgarh', 'DadraNagarHaveli', 'DamanDiu', 'Delhi',
          'Goa', 'Gujarat', 'Haryana', 'HimachalPradesh', 'JammuKashmir', 'Jharkhand',
          'Karnataka', 'Kerala', 'Lakshadweep', 'MadhyaPradesh', 'Maharashtra', 'Manipur', 'Meghalaya',
          'Mizoram', 'Nagaland', 'Odisha', 'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim', 'TamilNadu',
          'Tripura', 'UttarPradesh', 'Uttarakhand', 'WestBengal', 'Telangana']

state_id_int = ['001', '002', '003', '004', '005', '006', '007', '008', '009', '010', '011', '012', '013', '014',
            '015', '016', '017', '018', '019', '020', '021', '022', '023', '024', '025', '026', '027', '028',
            '029', '030', '031', '032', '033', '034', '035', '036']


def return_city_categories_dataset():
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

    for i in range(0, 20):
        label_dict = {}
        label_dict['label'] = "abcdefgh"
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


def return_city_chart(current_city):
    chart= {}
    chart["caption"] = current_city + " - Monitoring"
    chart["subCaption"] = "<Add time here>"
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


def city_map_function(_city):
    json_city = {}
    data_city = {}

    data_city['chart'] = return_city_chart(_city)
    categories_dataset = return_city_categories_dataset()
    data_city['categories'] = categories_dataset["categories"]
    data_city['dataset'] = categories_dataset["dataset"]

    json_city["type"] = "mscombidy2d"
    json_city["renderAt"] = "chart-container"
    json_city["width"] = "4000"
    json_city["height"] = "600"
    json_city["dataFormat"] = "json"
    json_city['dataSource'] = data_city

    return json.dumps(json_city)


def return_district_categories_dataset():
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

    for i in range(0, 10):
        label_dict = {}
        label_dict['label'] = "abcdefgh"
        label_dict['link'] = "../mapcity?city=" + "avscb"
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


def return_district_chart(current_district):
    chart= {}
    chart["caption"] = current_district + " - Monitoring"
    chart["subCaption"] = "<Add time here>"
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


def district_map_function(_district):
    json_district = {}
    data_district = {}

    data_district['chart'] = return_district_chart(_district)
    categories_dataset = return_district_categories_dataset()
    data_district['categories'] = categories_dataset["categories"]
    data_district['dataset'] = categories_dataset["dataset"]

    json_district["type"] = "mscombidy2d"
    json_district["renderAt"] = "chart-container"
    json_district["width"] = "4000"
    json_district["height"] = "600"
    json_district["dataFormat"] = "json"
    json_district['dataSource'] = data_district

    return json.dumps(json_district)


def return_state_categories_dataset():
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

    for i in range(0, 50):
        label_dict = {}
        label_dict['label'] = "abcd"
        label_dict['link'] = "../mapdistrict?district=" + "avscb"
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


def return_state_chart(current_state):
    chart= {}
    chart["caption"] = current_state + " - Monitoring"
    chart["subCaption"] = "<Add time here>"
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


def state_map_function(_state):
    json_state = {}
    data_state = {}

    data_state['chart'] = return_state_chart(_state)
    categories_dataset = return_state_categories_dataset()
    data_state['categories'] = categories_dataset["categories"]
    data_state['dataset'] = categories_dataset["dataset"]

    json_state["type"] = "mscombidy2d"
    json_state["renderAt"] = "chart-container"
    json_state["width"] = "4000"
    json_state["height"] = "600"
    json_state["dataFormat"] = "json"
    json_state['dataSource'] = data_state

    return json.dumps(json_state)


def return_data_array():

    data_array_in_json = []
    for i in range(0, len(state)):
        current_state = state[i]
        current_state_id = "../mapstate?state=" + state[i]
        data_json = {}
        data_json["id"] = state_id_int[i]
        data_json["value"] = student_teacher_ratio_state(state_id_int[i])
        data_json["showLabel"] = "0"
        data_json["color"] = "#008ee4"
        data_json["link"] = current_state_id
        data_json["hoverColor"] = "#ffccff"
        data_json["showHoverEffect"] = "1"
        data_array_in_json.append(data_json)
    return data_array_in_json


def country_map_function():

    final_json = {
        'type': 'india',
        'renderAt': 'chart-container',
        'width': '1200',
        'height': '600',
        'dataFormat': 'json',
        'dataSource': {
            "map": {
                "theme": "fint",
                "caption": "Shikshak Arohan",
                "subcaption": "Teacher-student ratio, Teacher attendance monitoring",
                "numberSuffix": "%",
                "fillColor": "#cccccc",
                "showHoverEffect": "0",
                "showCanvasBorder": "0",
                "showMarkerLabels": "1",
                "showConnectorLabels": "0",
                "connectorColor": "#80a83c",
                "connectorThickness": "2",
                "connectorHoverColor": "#f8bd19",
                "connectorHoverThickness": "3",
                "borderColor": "#ffffff",
                "showShadow": "0"
            }
        }
    }

    final_json["dataSource"]["data"] = return_data_array()
    return json.dumps(final_json)
