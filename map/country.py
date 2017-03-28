import json
from .database_operations import *
from array import *
from .arrays import *

# functions for creating json for map of INDIA

def return_data_array(_to, _from, _teacher_cat):

    data_array_in_json = []
    for i in range(0, len(state)):
        current_state = state[i]
        current_state_link = "../mapstate?state=" + current_state + "&stateid=" + state_id_int[i] + "&to=" + _to +"&from=" +_from + "&teachercategory=" + _teacher_cat
        data_json = {}
        data_json["id"] = state_id_int[i]
        data_json["value"] = student_teacher_ratio_state(state_id_int[i])
        data_json["showLabel"] = "0"
        data_json["color"] = "#008ee4"
        data_json["link"] = current_state_link
        data_json["hoverColor"] = "#ffccff"
        data_json["showHoverEffect"] = "1"
        data_array_in_json.append(data_json)
    return data_array_in_json


def country_map_function(_to, _from, _teacher_cat):

    final_json = {
        'type': 'india',
        'renderAt': 'chart-container',
        'width': '800',
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

    final_json["dataSource"]["data"] = return_data_array(_to, _from, _teacher_cat)
    return json.dumps(final_json)
