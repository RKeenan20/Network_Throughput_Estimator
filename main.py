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

#FIXME for the best case rate, the data rate entered by the person will always have the same NBits and CRate but the NChan
# will change between the bandwidths and as a result, we can just do (NBits * CRate * NChan) * Nss
def main():
    print("Choose a protocol from the following: \n")
    func.print_out_a_choice(config.protocol)
    while True:
        chosen_protocol = config.protocol[int(input("Enter choice in numerical form: \n")) - 1]
        if chosen_protocol in config.protocol:
            break
        else:
            continue
    print("Please choose a relevant 802.11 Standard from the below list:")
    func.print_dict(config.standards, None)

    while True:
        chosen_standard = list(config.standards)[int(input("Enter choice in numerical form: \n")) - 1]
        if chosen_standard in config.standards:
            break
        else:
            continue
    # Now that I have the input from the user, we need to see what type of data rate they want to use
    print("Choose a data rate from the following list:")
    # This will print out the "Data Rates" list of the chosen standard which is stored as a string
    func.print_dict(config.standards[chosen_standard]["Data Rates"], config.standards[chosen_standard])
    while True:
        chosen_data_rate = list(config.standards[chosen_standard]["Data Rates"])[int(input("Enter choice in numerical form: \n")) - 1]
        if chosen_data_rate in config.standards[chosen_standard]["Data Rates"]:
            break
        else:
            continue


    chosen_data_rate_info = list(config.standards[chosen_standard]["Data Rate's Data"])[
        list(config.standards[chosen_standard]["Data Rates"]).index(chosen_data_rate)]
    MAC_header = config.standards[chosen_standard]["MAC Header"]
    SIFS = config.standards[chosen_standard]["SIFS"]
    Preamble = config.standards[chosen_standard]["Preamble"]
    print(chosen_standard)
    if str(chosen_standard).split('\n')[0] == "802.11g":
        signal_extension = 6
    else:
        signal_extension = 0


    #FIXME this is where the indentation happened
    # I now have the chosen_data_rate and the chosen standards
    # I can now process the data rate values

    # Gathering all of the relevant information for the calculation
    NBits = chosen_data_rate_info[0]
    CRate = chosen_data_rate_info[1]
    NChan = chosen_data_rate_info[2]
    SDur = chosen_data_rate_info[3]
    DIFS = (2 * SLOT_TIME) + SIFS

    # FIXME should be multiplied by Nss once we have concluded what the answer to that is
    bits_per_ofdm_symbol = NBits * CRate * NChan
    print(ceil(((RTS_SIZE * 8) + 6) / bits_per_ofdm_symbol), SDur)
    total_packet_size = PACKET_SIZE + MAC_header + SNAP_LLC  # bytes

    # at the data rate, I can see how many bits are encoded by one symbol
    RTS_Dur = ceil(((RTS_SIZE * 8) + 6) / bits_per_ofdm_symbol) * SDur + signal_extension
    CTS_Dur = ceil(((CTS_SIZE * 8) + 6) / bits_per_ofdm_symbol) * SDur + signal_extension
    Data_Frame_Dur = ceil(((total_packet_size * 8) + 6) / bits_per_ofdm_symbol) * SDur + signal_extension
    ACK_Dur = ceil(((14 * 8) + 6) / bits_per_ofdm_symbol) * SDur + signal_extension
    TCP_ACK_Dur = ceil((((TCP_ACK_SIZE + MAC_header + SNAP_LLC) * 8) + 6) / bits_per_ofdm_symbol) * SDur + signal_extension
    print(RTS_Dur, CTS_Dur, Data_Frame_Dur, ACK_Dur, TCP_ACK_Dur)

    transmission_dur = DIFS + Preamble + RTS_Dur + SIFS + Preamble + CTS_Dur + SIFS + Preamble + Data_Frame_Dur + SIFS + Preamble + ACK_Dur
    if chosen_protocol == "TCP":
        transmission_dur += DIFS + Preamble + RTS_Dur + SIFS + Preamble + CTS_Dur + SIFS + Preamble + TCP_ACK_Dur + SIFS + Preamble + ACK_Dur

    throughput = (PACKET_SIZE * 8) / transmission_dur  # This result is given in Mbps

    # 10GB of data can be written as 10e3 with reference to the bits per second which is in Mb
    data_test = 10e3 * 8  # in bits

    # Time taken to transfer 10GB of data
    time_taken = data_test / throughput

    print("Results are as follows: \nProtocol: " + chosen_protocol + "\nStandard: " + str(chosen_standard) + "\nData Rate: %d Mbps\nThroughput: %.3f Mbps\n" % (chosen_data_rate, throughput ))
    print("The time taken to transfer 10GB of data is: %.2f seconds or %.2f minutes\n" % (time_taken, time_taken/60))


if __name__ == "__main__":
    main()
