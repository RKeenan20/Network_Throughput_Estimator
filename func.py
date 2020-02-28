import config


# Prints out a choice from an array
def print_out_a_choice(list_choice):
    for i in range(len(list_choice)):
        print(str(i + 1) + ": " + list_choice[i])


# Prints out a choice from a dictionary
def print_dict(dictionary, value_1):
    # This is for selecting a 802.11 standard
    if value_1 is None:
        for i, value in enumerate(dictionary.keys()):
            print(str(i + 1) + ": " + str(value))
    # This is for each standard's data rates
    else:
        for i, value in enumerate(value_1["Data Rates"]):
            print(str(i + 1) + ": " + str(value) + " Mbps")


# This function prints out the choices to the user and takes input such as the chosen protocol, standard and data rates.
def user_choice():
    print("Choose a protocol from the following: ")
    # Print out the protocols (TCP vs UDP)
    print_out_a_choice(config.protocol)
    # Input from the user and assign to chosen_protocol variable
    # Chosen Protocol (TCP vs UDP)
    chosen_protocol = config.protocol[int(input("Enter choice in numerical form: \n")) - 1]

    # Entering a valid 802.11 standard
    print("Please choose a relevant 802.11 Standard from the below list:")
    print_dict(config.standards, None)
    chosen_standard = list(config.standards)[int(input("Enter choice in numerical form: \n")) - 1]

    # Ask the user for input of their chosen 1SS, 20MHz data rate for the chosen standard
    print("Choose a data rate from the following list:")
    print_dict(config.standards[chosen_standard]["Data Rates"], config.standards[chosen_standard])
    # Data rate that the user has selected
    chosen_data_rate = list(config.standards[chosen_standard]["Data Rates"])[
            int(input("Enter choice in numerical form: \n")) - 1]

    #Return the variables
    return chosen_protocol, chosen_standard, chosen_data_rate
