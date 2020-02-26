import config, func, json
from math import ceil

#Define the standard values in terms of bytes and microseconds
PACKET_SIZE = 1500  # bytes
SNAP_LLC = 8  # bytes
SLOT_TIME = 9  # microseconds
TCP_ACK_SIZE = 40  # bytes
RTS_SIZE = 20  # bytes
CTS_SIZE = 14  # bytes

def main():
    print("Choose a protocol from the following: \n")
    #Print out the protocols
    func.print_out_a_choice(config.protocol)
    #Keep asking for input from the user
    while True:
        #Chosen Protocol (TCP vs UDP)
        chosen_protocol = config.protocol[int(input("Enter choice in numerical form: \n")) - 1]
        #Check it's valid
        if chosen_protocol in config.protocol:
            break
        else:
            continue

    #Entering a valid 802.11 standard
    print("Please choose a relevant 802.11 Standard from the below list:")
    func.print_dict(config.standards, None)
    while True:
        chosen_standard = list(config.standards)[int(input("Enter choice in numerical form: \n")) - 1]
        if chosen_standard in config.standards:
            break
        else:
            continue

    #Ask the user for input of their chosen 1SS, 20MHz data rate for the chosen standard
    print("Choose a data rate from the following list:")
    func.print_dict(config.standards[chosen_standard]["Data Rates"], config.standards[chosen_standard])
    while True:
        #Data rate that the user has selected
        chosen_data_rate = list(config.standards[chosen_standard]["Data Rates"])[
            int(input("Enter choice in numerical form: \n")) - 1]
        if chosen_data_rate in config.standards[chosen_standard]["Data Rates"]:
            break
        else:
            continue

    #Obtaining all of the specific data rate's information such as NBits and CRate etc
    chosen_data_rate_info = list(config.standards[chosen_standard]["Data Rate's Data"])[
        list(config.standards[chosen_standard]["Data Rates"]).index(chosen_data_rate)]

    #MAC Header and SIFS
    MAC_header = config.standards[chosen_standard]["MAC Header"]
    SIFS = config.standards[chosen_standard]["SIFS"]

    # Gather all information needed for calculating signal duration and bits per OFDM symbol.
    NBits = chosen_data_rate_info[0]
    CRate = chosen_data_rate_info[1]
    SDur = chosen_data_rate_info[3]
    DIFS = (2 * SLOT_TIME) + SIFS

    #This loop is used for the normal case and best case situations where some values differ
    for i in range(len(config.standards[chosen_standard]["Preamble"])):

        #i is used to track if the Best case is being selected, e.g. 160MHz for 802.11ax.
        #In this case, Nss
        if i==1:
            Nss = config.standards[chosen_standard]["Max Nss"]
            NChan = config.standards[chosen_standard]["Max NChan"]
            Preamble = config.standards[chosen_standard]["Preamble"][1]
        #This is for the Nss=1 20MHz case
        else:
            NChan = chosen_data_rate_info[2]
            Nss = chosen_data_rate_info[4]
            Preamble = config.standards[chosen_standard]["Preamble"][0]

        #If the signal is 802.11g, then a signal extension is needed for each OFDM frame
        if str(chosen_standard).split('\n')[0] == "802.11g":
            signal_extension = 6
        else:
            signal_extension = 0

        #Calculation of bits per OFDM symbol
        bits_per_ofdm_symbol = int((NBits * CRate * NChan) * Nss)

        #Data Packet size in bytes
        total_packet_size = PACKET_SIZE + MAC_header + SNAP_LLC  # bytes

        # Calculating the duration of each 802.11 frame such as RTS, CTS in microseconds
        RTS_Dur = ceil(((RTS_SIZE * 8) + 6) / bits_per_ofdm_symbol) * SDur + signal_extension
        CTS_Dur = ceil(((CTS_SIZE * 8) + 6) / bits_per_ofdm_symbol) * SDur + signal_extension
        Data_Frame_Dur = ceil(((total_packet_size * 8) + 6) / bits_per_ofdm_symbol) * SDur + signal_extension
        ACK_Dur = ceil(((14 * 8) + 6) / bits_per_ofdm_symbol) * SDur + signal_extension
        TCP_ACK_Dur = ceil(
            (((TCP_ACK_SIZE + MAC_header + SNAP_LLC) * 8) + 6) / bits_per_ofdm_symbol) * SDur + signal_extension

        #Calculating the total time elapsed to transmit 1500byte data packet in UDP
        transmission_dur = DIFS + Preamble + RTS_Dur + SIFS + Preamble + CTS_Dur + SIFS + Preamble + Data_Frame_Dur + SIFS + Preamble + ACK_Dur

        #If TCP has been specified, add to original UDP calculation
        if chosen_protocol == "TCP":
            transmission_dur += DIFS + Preamble + RTS_Dur + SIFS + Preamble + CTS_Dur + SIFS + Preamble + TCP_ACK_Dur + SIFS + Preamble + ACK_Dur

        #Throughput is the original 1500bytes in bits divided by total time in mircroseconds. Result is in Mbps
        throughput = (PACKET_SIZE * 8) / transmission_dur  # Mbps

        #10GB of data with reference to Mb is 10x10^3
        data_test = 10e3 * 8  # in bits

        # Time taken to transfer 10GB of data
        time_taken = data_test / throughput

        #If we are taking account for the best case
        if i == 1:
            print("-----------------------------------------------------------------------------------")
            print("The results for the best case for " + str(chosen_standard) + " of " + str(Nss) + " spatial streams (Nss) are given below")
            print("-----------------------------------------------------------------------------------\n")

        #Print results
        print("Results are as follows: \nProtocol: " + chosen_protocol + "\nStandard: " + str(chosen_standard) + "\nData Rate: %.2f Mbps\nNss: %d\nNo. of Channels: %d\nThroughput: %.3f Mbps\n" % (chosen_data_rate, Nss, NChan, throughput))
        print("The time taken to transfer 10GB of data is: %.2f seconds or %.2f minutes\n" % (time_taken, time_taken / 60))



if __name__ == "__main__":
    main()
