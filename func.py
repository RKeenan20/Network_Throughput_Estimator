from operator import itemgetter


def getList(dict):
    return list(map(itemgetter(0), dict.items()))
def print_out_a_choice(list):
    for i in range(len(list)):
            print(str(i+1) + ": " + list[i] + "\n")

def print_dict(dict, value_1):
    if value_1 is None:
        for i, value in enumerate(dict.keys()):
            print(i+1, value)

    else:
        for i, value in enumerate(value_1["Data Rates"]):
            print(str(i + 1) + ": " + str(value) + "Mbps")



    #chosen_number = input("Enter choice in numerical form: \n")
    #chosen_value = ((list_array[int(chosen_number)-1])[0])
    #return chosen_value.split(":")[1]

    #number_input = input("Enter choice in numerical form: \n")
    #print(type(list))
    #chosen_answer = str(list[number_input-1])
    #print(chosen_answer)
    #return chosen_answer
