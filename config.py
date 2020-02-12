global PACKET_SIZE  #bytes
global SNAP_LLC #bytes
global SLOT_TIME #microseconds
global TCP_ACK_SIZE #bytes
global RTS_SIZE #bytes
global CTS_SIZE #bytes
global TAIL_BITS_APPENDED #bits

PACKET_SIZE = 1500 #bytes
SNAP_LLC = 8 #bytes
SLOT_TIME = 9 #microseconds
TCP_ACK_SIZE = 40 #bytes
RTS_SIZE = 20 #bytes
CTS_SIZE = 14 #bytes
TAIL_BITS_APPENDED = 6 #bits


#Here all of the standards are used
standards = ["802.11a", "802.11g", "802.11n", "802.11ac_w1", "802.11ac_w2", "802.11ax"]
#The protocol needing to be usedgi
protocol = ["TCP", "UDP"]

#create a dictionary out of the information whereby the data rates are stored in one array and in the other array we have the NBits info etc
#The standard data is in the form of [NBits, CRate, NChan, SDur (microsecs)]
#The individual values can be accessed from the


#In this section I will add all of the Nss = 1 data as well as the max rates
#FIXME for the max data rates
#FIXME this is for the SDur = 3.6 micro
data_rates_n_ac = {"Data Rates" : [96.3, 86.7, 72.2, 65, 57.8, 43.3, 28.9, 21.7, 14.4, 7.2],
                   "Data Rate's Data": [[8, 5/6, 52, 3.6],
                                        [8, 3/4, 52, 3.6],
                                        [6, 5/6, 52, 3.6],
                                        [6, 3/4, 52, 3.6],
                                        [6, 2/3, 52, 3.6],
                                        [4, 3/4, 52, 3.6],
                                        [4, 1/2, 52, 3.6],
                                        [2, 3/4, 52, 3.6],
                                        [2, 1/2, 52, 3.6],
                                        [1, 1/2, 52, 3.6]]
                   }

max_rates_n_ac = {"Data Rates": [6933.6, 866.7, 3466.4, 433.3, 1600, 200, 577.8, 96.3, 600, 150, 288.8, 72.2],
                  "Data Rate's Data": [[8, 5/6, 468, 3.6],
                                      [8, 5/6, 468, 3.6],
                                      [8, 5/6, 234, 3.6],
                                      [8, 5/6, 234, 3.6],
                                      [8, 5/6, 108, 3.6],
                                      [8, 5/6, 108, 3.6],
                                      [8, 5/6, 52, 3.6],
                                      [8, 5/6, 52, 3.6],
                                      [6, 5/6, 108, 3.6],
                                      [6, 5/6, 108, 3.6],
                                      [6, 5/6, 52, 3.6],
                                      [6, 5/6, 52, 3.6]]
                  }

data_rates_ag = {"Data Rates" : [54,48,36,4,18,12,9,6],
                 "Data Rate's Data": [[6, 3/4, 48, 4],
                                      [6, 2/3, 48, 4],
                                      [4, 3/4, 48, 4],
                                      [4, 1/2, 48, 4],
                                      [2, 3/4, 48, 4],
                                      [2, 1/2, 48, 4],
                                      [1, 1/2, 48, 4]]
                 }

#This has been done for Nss = 8 rather than Nss = 1
#FIXME need to do Nss = 1
#FIXME the info on the last column of the Nss = 8 seems to be incorrect
data_rates_ax = {"Data Rates" : [9608, 6768.4, 5764.8, 3459.2, 1729.6, 576.8, 1147.2, 917.6, 688, 412.8, 206.4, 68.8],
                 "Data Rate's Data" : [[10, 5/6, 234, 13.6],
                                     [8, 5/6, 234, 13.6],
                                     [6, 5/6, 234, 13.6],
                                     [4, 3/4, 234, 13.6],
                                     [2, 3/4, 234, 13.6],
                                     [1, 1/2, 234, 13.6],
                                    [10, 5/6, 234, 13.6],
                                     [8, 5/6, 234, 13.6],
                                     [6, 5/6, 234, 13.6],
                                     [4, 3/4, 234, 13.6],
                                     [2, 3/4, 234, 13.6],
                                     [1, 1/2, 234, 13.6]]
                 }
#SIFS in micro seconds
#MAC Headers in bytes
#Preamble is in microseconds

standards_info = {
    "802.11n" : {"MAC Header" : 40, "SIFS" : 16, "Preamble" : 46},
    "802.11ac_w1" : {"MAC Header" : 40, "SIFS" : 16, "Preamble" : 46},
    "802.11ac_w2" : {"MAC Header" : 40, "SIFS" : 16, "Preamble" : 46},
    "802.11ax" : {"MAC Header" : 40, "SIFS" : 16, "Preamble" : 46},
    "802.11g" : {"MAC Header" : 34, "SIFS" : 10, "Preamble" : 46},
    "802.11a" : {"MAC Header" : 34, "SIFS" : 16, "Preamble" : 46},
}
#I need to take account for the slot time, DIFS, MAC header, preamble, signal extension, ACK length,