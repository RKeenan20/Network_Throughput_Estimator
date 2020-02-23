protocol = ["TCP", "UDP"]
# Here all of the standards are used
standards = {
    "802.11a": {
        "Data Rates": [54, 48, 36, 24, 18, 12, 9, 6],
        "Data Rate's Data": [[6, 3 / 4, 48, 4],
                          [6, 2 / 3, 48, 4],
                          [4, 3 / 4, 48, 4],
                          [4, 1 / 2, 48, 4],
                          [2, 3 / 4, 48, 4],
                          [2, 1 / 2, 48, 4],
                          [1, 1 / 2, 48, 4]],
        "MAC Header": 34,
        "SIFS": 16,
        "Preamble": 20
    },
    "802.11g": {
        "Data Rates": [54, 48, 36, 24, 18, 12, 9, 6],
        "Data Rate's Data": [[6, 3 / 4, 48, 4],
                          [6, 2 / 3, 48, 4],
                          [4, 3 / 4, 48, 4],
                          [4, 1 / 2, 48, 4],
                          [2, 3 / 4, 48, 4],
                          [2, 1 / 2, 48, 4],
                          [1, 1 / 2, 48, 4]],
        "MAC Header": 34,
        "SIFS": 10,
        "Preamble": 20
    },
    "802.11n":{
        "Data Rates": [96.3, 86.7, 72.2, 65, 57.8, 43.3, 28.9, 21.7, 14.4, 7.2],
        "Data Rate's Data": [[8, 5 / 6, 52, 3.6],
                            [8, 3 / 4, 52, 3.6],
                            [6, 5 / 6, 52, 3.6],
                            [6, 3 / 4, 52, 3.6],
                            [6, 2 / 3, 52, 3.6],
                            [4, 3 / 4, 52, 3.6],
                            [4, 1 / 2, 52, 3.6],
                            [2, 3 / 4, 52, 3.6],
                            [2, 1 / 2, 52, 3.6],
                            [1, 1 / 2, 52, 3.6]],
        "MAC Header": 40,
        "SIFS": 16,
        # This will be for the base value, then max .n, max .ac_w1, max .ac_w2
        "Preamble": [20, 46]
    },
    "802.11ac_w1":{
        "Data Rates": [96.3, 86.7, 72.2, 65, 57.8, 43.3, 28.9, 21.7, 14.4, 7.2],
        "Data Rate's Data": [[8, 5 / 6, 52, 3.6],
                            [8, 3 / 4, 52, 3.6],
                            [6, 5 / 6, 52, 3.6],
                            [6, 3 / 4, 52, 3.6],
                            [6, 2 / 3, 52, 3.6],
                            [4, 3 / 4, 52, 3.6],
                            [4, 1 / 2, 52, 3.6],
                            [2, 3 / 4, 52, 3.6],
                            [2, 1 / 2, 52, 3.6],
                            [1, 1 / 2, 52, 3.6]],
        "MAC Header": 40,
        "SIFS": 16,
        # This will be for the base value, then max .n, max .ac_w1, max .ac_w2
        "Preamble": [20, 56.8]
    },
    #FIXME check the preambles in this case and how to access
    "802.11ac_w2":{
        "Data Rates": [96.3, 86.7, 72.2, 65, 57.8, 43.3, 28.9, 21.7, 14.4, 7.2],
        "Data Rate's Data": [[8, 5 / 6, 52, 3.6],
                            [8, 3 / 4, 52, 3.6],
                            [6, 5 / 6, 52, 3.6],
                            [6, 3 / 4, 52, 3.6],
                            [6, 2 / 3, 52, 3.6],
                            [4, 3 / 4, 52, 3.6],
                            [4, 1 / 2, 52, 3.6],
                            [2, 3 / 4, 52, 3.6],
                            [2, 1 / 2, 52, 3.6],
                            [1, 1 / 2, 52, 3.6]],
        "MAC Header": 40,
        "SIFS": 16,
        # This will be for the base value, then max .n, max .ac_w1, max .ac_w2
        "Preamble": [20, 92.8]
    },
    #FIXME this data is for the 160MHz channel and I need to enter the data for the Nss = 1 case
    "802.11ax": {
        "Data Rates": [9608, 6768.4, 5764.8, 3459.2, 1729.6, 576.8, 1147.2, 917.6, 688, 412.8, 206.4, 68.8],
        "Data Rate's Data": [[10, 5 / 6, 234, 13.6],
                              [8, 5 / 6, 234, 13.6],
                              [6, 5 / 6, 234, 13.6],
                              [4, 3 / 4, 234, 13.6],
                              [2, 3 / 4, 234, 13.6],
                              [1, 1 / 2, 234, 13.6],
                              [10, 5 / 6, 234, 13.6],
                              [8, 5 / 6, 234, 13.6],
                              [6, 5 / 6, 234, 13.6],
                              [4, 3 / 4, 234, 13.6],
                              [2, 3 / 4, 234, 13.6],
                              [1, 1 / 2, 234, 13.6]],
        "MAC Header": 40,
        "SIFS": 16,
        "Preamble": [20, 46]
    }
}
# The protocol needing to be usedgi
protocol = ["TCP", "UDP"]

# create a dictionary out of the information whereby the data rates are stored in one array and in the other array we have the NBits info etc
# The standard data is in the form of [NBits, CRate, NChan, SDur (microsecs)]
# The individual values can be accessed from the


# In this section I will add all of the Nss = 1 data as well as the max rates
# FIXME for the max data rates
# FIXME this is for the SDur = 3.6 micro
# FIXME change the preamble to add for the max values
