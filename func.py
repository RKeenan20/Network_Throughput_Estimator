#Prints out a choice from an array
def print_out_a_choice(list):
    for i in range(len(list)):
            print(str(i+1) + ": " + list[i] + "\n")

#Prints out a choice from a dictionary
def print_dict(dict, value_1):
    #This is for selecting a 802.11 standard
    if value_1 is None:
        for i, value in enumerate(dict.keys()):
            print(str(i + 1) + ": " + str(value))
    #This is for standard's data rates
    else:
        for i, value in enumerate(value_1["Data Rates"]):
            print(str(i + 1) + ": " + str(value) + " Mbps")
