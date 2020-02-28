##
#   This file is used fr the configurations of each data rate.
#   The protocols in terms of TCP and UDP are defined as an array.
#   The 802.11 standards are defined as nested dictionaries where the "standards" dictionary's keys are the standards themselves
#   followed by their Data Rates,  their MAC Header, SIFS, Preamble, Max Nss and Max NChan and potentially a Max Bandwidth
#
#   Values are laid out in terms of the individual standards, their data rates and then MAC Header, SIFS and Preamble
#   The Preamble is an array of either 1 or 2 values. If there are 2 values, the first corresponds to the 20MHz 1SS case
#   while the 2nd value corresponds to the best case.
##

#The protocols to choose from
protocol = ["TCP", "UDP"]
standards = {
    "802.11a": {
        "Data Rates": {
            54: {"NBits": 6, "CRate": 3/4, "NChan": 48, "SDur": 4, "Nss": 1},
            48: {"NBits": 6, "CRate": 2/3, "NChan": 48, "SDur": 4, "Nss": 1},
            36: {"NBits": 4, "CRate": 3/4, "NChan": 48, "SDur": 4, "Nss": 1},
            24: {"NBits": 4, "CRate": 1/2, "NChan": 48, "SDur": 4, "Nss": 1},
            18: {"NBits": 2, "CRate": 3/4, "NChan": 48, "SDur": 4, "Nss": 1},
            12: {"NBits": 2, "CRate": 1/2, "NChan": 48, "SDur": 4, "Nss": 1},
            9:  {"NBits": 1, "CRate": 3/4, "NChan": 48, "SDur": 4, "Nss": 1},
            6:  {"NBits": 1, "CRate": 1/2, "NChan": 48, "SDur": 4, "Nss": 1}
        },
        "MAC Header": 34,
        "SIFS": 16,
        "Preamble": [20]
    },
    "802.11g": {
        "Data Rates": {
            54: {"NBits": 6, "CRate": 3/4, "NChan": 48, "SDur": 4, "Nss": 1},
            48: {"NBits": 6, "CRate": 2/3, "NChan": 48, "SDur": 4, "Nss": 1},
            36: {"NBits": 4, "CRate": 3/4, "NChan": 48, "SDur": 4, "Nss": 1},
            24: {"NBits": 4, "CRate": 1/2, "NChan": 48, "SDur": 4, "Nss": 1},
            18: {"NBits": 2, "CRate": 3/4, "NChan": 48, "SDur": 4, "Nss": 1},
            12: {"NBits": 2, "CRate": 1/2, "NChan": 48, "SDur": 4, "Nss": 1},
            9:  {"NBits": 1, "CRate": 3/4, "NChan": 48, "SDur": 4, "Nss": 1},
            6:  {"NBits": 1, "CRate": 1/2, "NChan": 48, "SDur": 4, "Nss": 1}
        },
        "MAC Header": 34,
        "SIFS": 10,
        "Preamble": [20]
    },
    "802.11n":{
        "Data Rates": {
            72.2: {"NBits": 6, "CRate": 5/6, "NChan": 52, "SDur": 3.6, "Nss": 1},
            65:   {"NBits": 6, "CRate": 3/4, "NChan": 52, "SDur": 3.6, "Nss": 1},
            57.8: {"NBits": 6, "CRate": 2/3, "NChan": 52, "SDur": 3.6, "Nss": 1},
            43.3: {"NBits": 4, "CRate": 3/4, "NChan": 52, "SDur": 3.6, "Nss": 1},
            28.9: {"NBits": 4, "CRate": 1/2, "NChan": 52, "SDur": 3.6, "Nss": 1},
            21.7: {"NBits": 2, "CRate": 3/4, "NChan": 52, "SDur": 3.6, "Nss": 1},
            14.4: {"NBits": 2, "CRate": 1/2, "NChan": 52, "SDur": 3.6, "Nss": 1},
            7.2:  {"NBits": 1, "CRate": 1/2, "NChan": 52, "SDur": 3.6, "Nss": 1}
        },
        "MAC Header": 40,
        "SIFS": 16,
        "Max NChan": 108,
        "Max Nss": 4,
        "Preamble": [20, 46],
        "Max Bandwidth": 40
    },
    "802.11ac_w1" : {
        "Data Rates": {
            96.3: {"NBits": 8, "CRate": 5/6, "NChan": 52, "SDur": 3.6, "Nss": 1},
            86.7: {"NBits": 8, "CRate": 3/4, "NChan": 52, "SDur": 3.6, "Nss": 1},
            72.2: {"NBits": 6, "CRate": 5/6, "NChan": 52, "SDur": 3.6, "Nss": 1},
            65:   {"NBits": 6, "CRate": 3/4, "NChan": 52, "SDur": 3.6, "Nss": 1},
            57.8: {"NBits": 6, "CRate": 2/3, "NChan": 52, "SDur": 3.6, "Nss": 1},
            43.3: {"NBits": 4, "CRate": 3/4, "NChan": 52, "SDur": 3.6, "Nss": 1},
            28.9: {"NBits": 4, "CRate": 1/2, "NChan": 52, "SDur": 3.6, "Nss": 1},
            21.7: {"NBits": 2, "CRate": 3/4, "NChan": 52, "SDur": 3.6, "Nss": 1},
            14.4: {"NBits": 2, "CRate": 1/2, "NChan": 52, "SDur": 3.6, "Nss": 1} ,
            7.2:  {"NBits": 1, "CRate": 1/2, "NChan": 52, "SDur": 3.6, "Nss": 1}
        },
        "MAC Header": 40,
        "SIFS": 16,
        "Max NChan": 234,
        "Max Nss": 3,
        "Preamble": [20, 56.8],
        "Max Bandwidth": 80
    },
    "802.11ac_w2": {
        "Data Rates": {
            96.3: {"NBits": 8, "CRate": 5/6, "NChan": 52, "SDur": 3.6, "Nss": 1},
            86.7: {"NBits": 8, "CRate": 3/4, "NChan": 52, "SDur": 3.6, "Nss": 1},
            72.2: {"NBits": 6, "CRate": 5/6, "NChan": 52, "SDur": 3.6, "Nss": 1},
            65:   {"NBits": 6, "CRate": 3/4, "NChan": 52, "SDur": 3.6, "Nss": 1},
            57.8: {"NBits": 6, "CRate": 2/3, "NChan": 52, "SDur": 3.6, "Nss": 1},
            43.3: {"NBits": 4, "CRate": 3/4, "NChan": 52, "SDur": 3.6, "Nss": 1},
            28.9: {"NBits": 4, "CRate": 1/2, "NChan": 52, "SDur": 3.6, "Nss": 1},
            21.7: {"NBits": 2, "CRate": 3/4, "NChan": 52, "SDur": 3.6, "Nss": 1},
            14.4: {"NBits": 2, "CRate": 1/2, "NChan": 52, "SDur": 3.6, "Nss": 1},
            7.2:  {"NBits": 1, "CRate": 1/2, "NChan": 52, "SDur": 3.6, "Nss": 1}
        },
        "MAC Header": 40,
        "SIFS": 16,
        "Max NChan": 468,
        "Max Nss": 8,
        "Preamble": [20, 92.8],
        "Max Bandwidth": 160
    },
    "802.11ax": {
        "Data Rates": {
            143.4: {"NBits": 10, "CRate": 5/6, "NChan": 234, "SDur": 13.6, "Nss": 1},
            129:   {"NBits": 10, "CRate": 3/4, "NChan": 234, "SDur": 13.6, "Nss": 1},
            114.7: {"NBits": 8, "CRate": 5/6, "NChan": 234, "SDur": 13.6, "Nss": 1},
            103.2: {"NBits": 8, "CRate": 3/4, "NChan": 234, "SDur": 13.6, "Nss": 1},
            86:    {"NBits": 6, "CRate": 5/6, "NChan": 234, "SDur": 13.6, "Nss": 1},
            77.4:  {"NBits": 6, "CRate": 3/4, "NChan": 234, "SDur": 13.6, "Nss": 1},
            68.8:  {"NBits": 6, "CRate": 2/3, "NChan": 234, "SDur": 13.6, "Nss": 1},
            51.6:  {"NBits": 4, "CRate": 3/4, "NChan": 234, "SDur": 13.6, "Nss": 1},
            34.4:  {"NBits": 4, "CRate": 1/2, "NChan": 234, "SDur": 13.6, "Nss": 1},
            25.8:  {"NBits": 2, "CRate": 3/4, "NChan": 234, "SDur": 13.6, "Nss": 1},
            17.2:  {"NBits": 2, "CRate": 1/2, "NChan": 234, "SDur": 13.6, "Nss": 1},
            8.6:   {"NBits": 1, "CRate": 1/2, "NChan": 234, "SDur": 13.6, "Nss": 1}
        },
        "MAC Header": 40,
        "SIFS": 16,
        "Max NChan": 1960,
        "Max Nss": 8,
        "Preamble": [20, 92.8],
        "Max Bandwidth": 160
    }
}
