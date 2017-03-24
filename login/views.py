from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
import json
from api.models import *
from login.models import *
from array import *

@login_required(login_url="login/")
def home(request):
    return render(request,"home.html")


def map_function(request):
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
            },
            "linkeddata": [{
                "id": "JammuKashmir",
                "linkedchart": {
                    "chart": {
                        "caption": "California - Shipment Summary",
                        "subCaption": "Last Month",
                        "pyaxisname": "Units",
                        "syaxisname": "Cost",
                        "xAxisName": "State",
                        "showvalues": "0",
                        "labelDisplay": "rotate",
                        "slantLabel": "1",
                        "formatNumberScale": "0",
                        "sNumberPrefix": "$",
                        "theme": "fint"
                    },
                    "categories": [{
                        "category": [{
                            "label": "Washington"
                        }, {
                            "label": "Nevada"
                        }, {
                            "label": "Arizona"
                        }, {
                            "label": "Wyoming"
                        }, {
                            "label": "Idaho"
                        }, {
                            "label": "Utah"
                        }, {
                            "label": "Montana"
                        }]
                    }],
                    "dataset": [{
                        "seriesname": "Daily Shipment",
                        "data": [{
                            "value": "20540"
                        }, {
                            "value": "19300"
                        }, {
                            "value": "18400"
                        }, {
                            "value": "18400"
                        }, {
                            "value": "17400"
                        }, {
                            "value": "16500"
                        }, {
                            "value": "15600"
                        }]
                    }, {
                        "seriesname": "Average Shipment Cost",
                        "parentyaxis": "S",
                        "data": [{
                            "value": "1.2"
                        }, {
                            "value": "0.4"
                        }, {
                            "value": "1.6"
                        }, {
                            "value": "0.5"
                        }, {
                            "value": "1.1"
                        }, {
                            "value": "0.5"
                        }, {
                            "value": "1.3"
                        }]
                    }]
                }
            }, {
                "id": "Gujarat",
                "linkedchart": {
                    "chart": {
                        "caption": "Texas - Shipment Summary",
                        "subCaption": "Last Month",
                        "pyaxisname": "Units",
                        "syaxisname": "Cost",
                        "xAxisName": "State",
                        "showvalues": "0",
                        "labelDisplay": "rotate",
                        "slantLabel": "1",
                        "formatNumberScale": "0",
                        "sNumberPrefix": "$",
                        "theme": "fint"
                    },
                    "categories": [{
                        "category": [{
                            "label": "New Mexico"
                        }, {
                            "label": "North Dakota"
                        }, {
                            "label": "Arkansas"
                        }, {
                            "label": "Mississippi"
                        }, {
                            "label": "Illinois"
                        }, {
                            "label": "South Dakota"
                        }, {
                            "label": "Colorado"
                        }, {
                            "label": "Nebraska"
                        }, {
                            "label": "Oklahoma"
                        }, {
                            "label": "Minnesota"
                        }, {
                            "label": "Iowa"
                        }, {
                            "label": "Louisiana"
                        }, {
                            "label": "Wisconsin"
                        }, {
                            "label": "Kansas"
                        }, {
                            "label": "Missouri"
                        }]
                    }],
                    "dataset": [{
                        "seriesname": "Daily Shipment",
                        "data": [{
                            "value": "21300"
                        }, {
                            "value": "19900"
                        }, {
                            "value": "19200"
                        }, {
                            "value": "18760"
                        }, {
                            "value": "17650"
                        }, {
                            "value": "17300"
                        }, {
                            "value": "17200"
                        }, {
                            "value": "16870"
                        }, {
                            "value": "16800"
                        }, {
                            "value": "16100"
                        }, {
                            "value": "15600"
                        }, {
                            "value": "15440"
                        }, {
                            "value": "14890"
                        }, {
                            "value": "13670"
                        }, {
                            "value": "12560"
                        }]
                    }, {
                        "seriesname": "Average Shipment Cost",
                        "parentyaxis": "S",
                        "data": [{
                            "value": "0.4"
                        }, {
                            "value": "1.7"
                        }, {
                            "value": "0.4"
                        }, {
                            "value": "0.6"
                        }, {
                            "value": "1.4"
                        }, {
                            "value": "1.6"
                        }, {
                            "value": "1.1"
                        }, {
                            "value": "1.4"
                        }, {
                            "value": "0.3"
                        }, {
                            "value": "1.7"
                        }, {
                            "value": "1.3"
                        }, {
                            "value": "0.3"
                        }, {
                            "value": "1.7"
                        }, {
                            "value": "0.5"
                        }, {
                            "value": "1.3"
                        }]
                    }]
                }
            }, {
                "id": "Haryana",
                "linkedchart": {
                    "chart": {
                        "caption": "North Carolina - Shipment Summary",
                        "subCaption": "Last Month",
                        "pyaxisname": "Units",
                        "syaxisname": "Cost",
                        "xAxisName": "State",
                        "showvalues": "0",
                        "labelDisplay": "rotate",
                        "slantLabel": "1",
                        "formatNumberScale": "0",
                        "sNumberPrefix": "$",
                        "theme": "fint"
                    },
                    "categories": [{
                        "category": [{
                            "label": "New York"
                        }, {
                            "label": "Florida"
                        }, {
                            "label": "Indiana"
                        }, {
                            "label": "Vermont"
                        }, {
                            "label": "Connecticut"
                        }, {
                            "label": "Michigan"
                        }, {
                            "label": "Georgia"
                        }, {
                            "label": "Virginia"
                        }, {
                            "label": "New Hampshire"
                        }, {
                            "label": "Massachusetts"
                        }, {
                            "label": "Ohio"
                        }, {
                            "label": "West Virginia"
                        }, {
                            "label": "South Carolina"
                        }, {
                            "label": "Kentucky"
                        }, {
                            "label": "Pennsylvania"
                        }, {
                            "label": "Indiana"
                        }, {
                            "label": "Maine"
                        }, {
                            "label": "Alabama"
                        }]
                    }],
                    "dataset": [{
                        "seriesname": "Daily Shipment",
                        "data": [{
                            "value": "23600"
                        }, {
                            "value": "21200"
                        }, {
                            "value": "19800"
                        }, {
                            "value": "18400"
                        }, {
                            "value": "18340"
                        }, {
                            "value": "18200"
                        }, {
                            "value": "17400"
                        }, {
                            "value": "17260"
                        }, {
                            "value": "16900"
                        }, {
                            "value": "16590"
                        }, {
                            "value": "16540"
                        }, {
                            "value": "16430"
                        }, {
                            "value": "16230"
                        }, {
                            "value": "15850"
                        }, {
                            "value": "15600"
                        }, {
                            "value": "14700"
                        }, {
                            "value": "14680"
                        }, {
                            "value": "13400"
                        }]
                    }, {
                        "seriesname": "Average Shipment Cost",
                        "parentyaxis": "S",
                        "data": [{
                            "value": "1.4"
                        }, {
                            "value": "1.6"
                        }, {
                            "value": "0.6"
                        }, {
                            "value": "1.4"
                        }, {
                            "value": "1.6"
                        }, {
                            "value": "1"
                        }, {
                            "value": "0.3"
                        }, {
                            "value": "0.2"
                        }, {
                            "value": "1.4"
                        }, {
                            "value": "1.2"
                        }, {
                            "value": "1.3"
                        }, {
                            "value": "0.3"
                        }, {
                            "value": "0.2"
                        }, {
                            "value": "0.4"
                        }, {
                            "value": "0.3"
                        }, {
                            "value": "4"
                        }, {
                            "value": "1.7"
                        }, {
                            "value": "0.4"
                        }]
                    }]
                }
            }]
        }
    }
    final_json["dataSource"]["data"] = data_array_in_json
    print json.dumps(final_json)
    return render(request,"rough.html", {'json_map':json.dumps(final_json)})
