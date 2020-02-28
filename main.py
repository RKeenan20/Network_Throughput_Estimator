import config, func
from math import ceil

# Standard Values used throughout the program
PACKET_SIZE = 1500  # bytes
SNAP_LLC = 8        # bytes
SLOT_TIME = 9       # microseconds
TCP_ACK_SIZE = 40   # bytes
RTS_SIZE = 20       # bytes
CTS_SIZE = 14       # bytes


def main():
    # Print out the choices for the user
    chosen_protocol, chosen_standard, chosen_data_rate = func.user_choice()

    # Obtaining all of the specific data rate's information such as NBits and CRate etc
    chosen_data_rate_info = config.standards[chosen_standard]["Data Rates"][chosen_data_rate]

    # Obtaining the values of the specific data rate chosen
    MAC_header = config.standards[chosen_standard]["MAC Header"]
    SIFS = config.standards[chosen_standard]["SIFS"]
    # Number of Bits
    NBits = chosen_data_rate_info["NBits"]
    # Coding Rate
    CRate = chosen_data_rate_info["CRate"]
    # Symbol Duration
    SDur = chosen_data_rate_info["SDur"]
    # Number of Channels
    NChan = chosen_data_rate_info["NChan"]
    # Number of Spatial Streams
    Nss = chosen_data_rate_info["Nss"]
    #Preamble
    preamble = config.standards[chosen_standard]["Preamble"][0]
    DIFS = (2 * SLOT_TIME) + SIFS
    #Setting the default (normal) case channel bandwidth to 20MHz
    bandwidth = 20

    # If the signal is 802.11g, then a signal extension is needed for each OFDM frame
    if str(chosen_standard).split('\n')[0] == "802.11g":
        signal_extension = 6
    else:
        signal_extension = 0

    # This loop is used for the normal case and best case situations where some values differ
    for cases in range(len(config.standards[chosen_standard]["Preamble"])):

        # "cases" keeps track if it is the Normal Case or the Best case being calculated
        # If cases is 1, this is the best case so we need to change NChan, Nss and Preamble
        if cases == 1:
            Nss = config.standards[chosen_standard]["Max Nss"]
            NChan = config.standards[chosen_standard]["Max NChan"]
            preamble = config.standards[chosen_standard]["Preamble"][1]
            bandwidth = config.standards[chosen_standard]["Max Bandwidth"]

        # Calculation of bits per OFDM symbol
        bits_per_ofdm_symbol = int((NBits * CRate * NChan) * Nss)

        # Data Packet size in bytes
        total_packet_size = PACKET_SIZE + MAC_header + SNAP_LLC

        #Duration calculations in microseconds (us) adding the 6 tail bits and a potential signal extension
        # RTS Duration
        RTS_Dur = ceil(((RTS_SIZE * 8) + 6) / bits_per_ofdm_symbol) * SDur + signal_extension
        # CTS Duration
        CTS_Dur = ceil(((CTS_SIZE * 8) + 6) / bits_per_ofdm_symbol) * SDur + signal_extension
        # Data Frame Duration
        Data_Frame_Dur = ceil(((total_packet_size * 8) + 6) / bits_per_ofdm_symbol) * SDur + signal_extension
        #ACK Duration
        ACK_Dur = ceil(((14 * 8) + 6) / bits_per_ofdm_symbol) * SDur + signal_extension
        #TCP ACK frame duration
        TCP_ACK_Dur = ceil(
            (((TCP_ACK_SIZE + MAC_header + SNAP_LLC) * 8) + 6) / bits_per_ofdm_symbol) * SDur + signal_extension

        # Calculating the total time elapsed to transmit 1500byte data packet in UDP
        transmission_dur = DIFS + preamble + RTS_Dur + SIFS + preamble + CTS_Dur + SIFS + preamble + Data_Frame_Dur \
                           + SIFS + preamble + ACK_Dur

        # If TCP has been specified, add on to the calculation done above
        if chosen_protocol == "TCP":
            transmission_dur += DIFS + preamble + RTS_Dur + SIFS + preamble + CTS_Dur + SIFS + preamble + TCP_ACK_Dur \
                                + SIFS + preamble + ACK_Dur

        # Throughput is the original 1500bytes in bits divided by total time in microseconds. Result is in Mbps
        throughput = (PACKET_SIZE * 8) / transmission_dur  # Mbps

        # 10GB of data with reference to Mb is 10x10^3
        #I have purposely set it this way as I know the throughput will be in Mbps
        data_test = 10e3 * 8  # in bits

        # Time taken to transfer 10GB of data
        time_taken = data_test / throughput

        # Taking account of best case, print this when the loop is on 2nd iteration
        if cases == 1:
            print("-----------------------------------------------------------------------------------")
            print("The results for the best case for " + str(chosen_standard) + " of " + str(Nss) + " spatial streams"
                  + "(Nss) are given below")
            print("-----------------------------------------------------------------------------------\n")

        # Print results of protocol, standard, data rate and more information
        print("Results are as follows: \nProtocol: " + chosen_protocol + "\nStandard: " + str(
            chosen_standard) + "\nData Rate: %.2f Mbps\nChannel Bandwidth: %d MHz\nNss: %d\nNo. of Channels: %d\nThroughput: %.3f Mbps\n" % (
                  chosen_data_rate, bandwidth, Nss, NChan, throughput))
        print("The time taken to transfer 10GB of data is: %.2f seconds or %.2f minutes\n" % (
            time_taken, time_taken / 60))


if __name__ == "__main__":
    main()
