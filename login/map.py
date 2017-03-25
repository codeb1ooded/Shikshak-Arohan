import json
from api.models import *
from login.models import *
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


def return_map_dict():
    map_dict = {}
    map_dict["theme"] = "fint",
    map_dict["caption"] = "Shikshak Arohan",
    map_dict["subcaption"] = "Teacher-student ratio, Teacher attendance monitoring",
    map_dict["numberSuffix"] = "%",
    map_dict["fillColor"] = "#cccccc",
    map_dict["showHoverEffect"] = "0",
    map_dict["showCanvasBorder"] = "0",
    map_dict["showMarkerLabels"] = "1",
    map_dict["showConnectorLabels"] = "0",
    map_dict["connectorColor"] = "#80a83c",
    map_dict["connectorThickness"] = "2",
    map_dict["connectorHoverColor"] = "#f8bd19",
    map_dict["connectorHoverThickness"] = "3",
    map_dict["borderColor"] = "#ffffff",
    map_dict["showShadow"] = "0"
    return map_dict

def return_data_array():

    data_array_in_json = []
    for i in range(0, len(state)):
        current_state = state[i]
        current_state_id = "newchart-json-" + state_ids[i]
        data_json = {}
        data_json["id"] = state_id_int[i]
        data_json["showLabel"] = "0"
        data_json["color"] = "#008ee4"
        data_json["link"] = current_state_id
        data_json["hoverColor"] = "#ffccff"
        data_json["showHoverEffect"] = "1"
        data_array_in_json.append(data_json)

    return data_array_in_json


def return_state_chart_dict(current_state):
    chart= {}
    chart["caption"] = current_state + " - Monitoring"
    chart["subCaption"] = "Last Month"
    chart["pyaxisname"] = "Units"
    chart["syaxisname"] = "Cost"
    chart["xAxisName"] = "State"
    chart["showvalues"] = "0"
    chart["labelDisplay"] = "rotate"
    chart["slantLabel"] = "1"
    chart["formatNumberScale"] = "0"
    chart["sNumberPrefix"] = "$"
    chart["theme"] = "fint"
    return chart


def return_state_categories_dataset():
    categories_dataset = {}
    categories = []
    category_array = []
    dataset = []
    dataset1 = {}
    dataset2 = {}

    dataset1["seriesname"] = "Series 1"
    dataset2["seriesname"] = "Series 2"

    data1 = []
    data2 = []

    for i in range(0, 10):
        label_dict = {}
        label_dict['label'] = "abcd"
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
    print dataset
    return categories_dataset


def return_linked_chart_dict(i):

    current_state = state[i]
    linked_chart = {}

    linked_chart["chart"] = return_state_chart_dict(current_state)
    categories_dataset = return_state_categories_dataset()
    linked_chart["categories"] = categories_dataset["categories"]
    linked_chart["dataset"] = categories_dataset["dataset"]
    return linked_chart


def return_linked_data():
    linked_data_array_in_json = []
    for i in range(0, len(state)):
        current_state = state[i]
        linked_data = {}
        linked_data["id"] = state_ids[i]
        linked_data["linkedchart"] = return_linked_chart_dict(i)
        linked_data_array_in_json.append(linked_data)

    return linked_data_array_in_json


def main_map_function():

    data_array_in_json = []
    linkeddata_array = []

    for i in range(0, len(state)):
        current_state = state[i]
        current_state_id = "newchart-json-" + state_ids[i]

        data_json = {}
        data_json["id"] = state_id_int[i]
        data_json["showLabel"] = "0"
        data_json["color"] = "#008ee4"
        data_json["link"] = current_state_id
        data_json["hoverColor"] = "#ffccff"
        data_json["showHoverEffect"] = "1"
        data_array_in_json.append(data_json)

        linkeddata_json = {}
        linkeddata_json['id'] = state_ids[i]

    final_json = {
        'type': 'india',
        'renderAt': 'chart-container',
        'width': '650',
        'height': '450',
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
    final_json["dataSource"]["linkeddata"] = return_linked_data()
    #print final_json["dataSource"]["linkeddata"][0]
    return json.dumps(final_json)
