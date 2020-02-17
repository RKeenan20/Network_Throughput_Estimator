import config, func, json
from math import ceil
import sys

PACKET_SIZE = 1500  # bytes
SNAP_LLC = 8  # bytes
SLOT_TIME = 9  # microseconds
TCP_ACK_SIZE = 40  # bytes
RTS_SIZE = 20  # bytes
CTS_SIZE = 14  # bytes


# TAIL_BITS_APPENDED = 6 #bits


def main():
    with open('standards.json') as json_file:
        config = json.loads(json_file.read())
        print("Choose a protocol from the following: \n")
        func.print_out_a_choice(config["protocols"])
        print(config['protocols'][0])
        # Check whether the relevant protocol has been entered
        while True:
            chosen_protocol = config['protocols'][int(input("Enter choice in numerical form: \n")) - 1]
            if chosen_protocol in config["protocols"]:
                break
            else:
                continue
        print("Please choose a relevant 802.11 Standard from the below list:")
        func.print_out_a_choice(config["standards"])
        while True:
            chosen_standard = config['standards'][input("Enter choice in numerical form: \n") - 1]
            if chosen_standard in config['standards']:
                break
            else:
                continue
        # Now that I have the input from the user, we need to see what type of data rate they want to use
        print("Choose a data rate from the following list:")
        # This will print out the "Data Rates" list of the chosen standard which is stored as a string
        func.print_out_a_choice(config[chosen_standard]["Data Rates"])
        while True:
            chosen_data_rate = config[chosen_standard]["Data Rates"][input("Enter choice in numerical form: \n") - 1]
            if chosen_data_rate in config[chosen_standard]["Data Rates"]:
                break
            else:
                continue
        chosen_data_rate_info = config[chosen_standard]["Data Rate Encoding Data"][
            config[chosen_standard]["Data Rates"].indexof(chosen_data_rate)]
        MAC_header = config[chosen_standard]["MAC Header"]
        SIFS = config[chosen_standard]["SIFS"]
        Preamble = config[chosen_standard]["Preamble"]
        if config[chosen_standard] is "802.11g":
            signal_extension = config[chosen_standard]["Signal Extension"]
        else:
            signal_extension = 0

    # I now have the chosen_data_rate and the chosen standards
    # I can now process the data rate values

    # Gathering all of the relevant information for the calculation
    NBits = chosen_data_rate_info[0]
    CRate = chosen_data_rate[1]
    NChan = chosen_data_rate_info[2]
    SDur = chosen_data_rate_info[3]
    DIFS = (2 * SLOT_TIME) + SIFS
    # FIXME should be multiplied by Nss once we have conluded what the answer to that is
    bits_per_OFDM_symbol = NBits * CRate * NChan

    total_packet_size = PACKET_SIZE + MAC_header + SNAP_LLC  # bytes

    # at the data rate, I can see how many bits are encoded by one symbol
    RTS_Dur = ceil(((RTS_SIZE * 8) + 6) / bits_per_OFDM_symbol) * SDur
    CTS_Dur = ceil(((CTS_SIZE * 8) + 6) / bits_per_OFDM_symbol) * SDur
    Data_Frame_Dur = ceil(((total_packet_size * 8) + 6) / bits_per_OFDM_symbol) * SDur
    ACK_Dur = SDur
    TCP_ACK_Dur = ceil(((TCP_ACK_SIZE * 8) + 6) / bits_per_OFDM_symbol)

    transmission_dur = DIFS + Preamble + RTS_Dur + SIFS + Preamble + CTS_Dur + SIFS + Preamble + Data_Frame_Dur + SIFS + Preamble + ACK_Dur
    if chosen_protocol.isequals("TCP"):
        transmission_dur = transmission_dur + DIFS + Preamble + RTS_Dur + SIFS + Preamble + CTS_Dur + SIFS + Preamble + TCP_ACK_Dur + SIFS + Preamble + ACK_Dur

    bits_per_second = (PACKET_SIZE * 8) / transmission_dur  # This result is given in Mbps

    # 10GB of data can be written as 10e3 with reference to the bits per second which is in Mb
    data_test = 10e3 * 8  # in bits

    # Time taken to transfer 10GB of data
    time_taken = data_test / bits_per_second

    print(
        "The actual throughput for Protocol: " + chosen_protocol + " Standard: " + chosen_standard + " Data Rate: " + chosen_data_rate + "Mbps is: " +
        bits_per_second+"\n")
    print("The time taken to transfer 10GB of data is: "+time_taken + "\n")


if __name__ == "__main__":
    main()
