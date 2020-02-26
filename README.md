# Advances in Wireless Networking COMP40660
## Assignment 1: 802.11 Throughput
### Robert Keenan 15333066

### Design and Usage
In this Assignment, I was tasked to build a throughput calculator for a number of 802.11 Wi-Fi standards from 802.11a all the way to 802.11ax. 
The program takes input of the protocol the user wants to use (TCP or UDP), the 802.11 standard they wish to use
and then the corresponding data rate of that 802.11 standard. 

We must output the calculated throughput for the chosen protocol and 802.11 standard for a data rate at 20MHz, 1 Spatial Stream 
which will be referred to as the "Normal" case and then the best case for this data rate will be using the maximum number of spatial streams and channels for the channel bandwidth.

My program can be interacted with in the following way. It will prompt you for input of the chosen protocol in terms of a numbered index first of all.
Following this, you can enter a numbered choice of 802.11 standard which are printed to the screen for your benefit. 
From here, the available data rates at a channel bandwidth of 20MHz 1SS are printed to the screen where you can choose a choice.
An example is shown below:

ADD IN THE IMAGE OF THE ENTRY OF DATA

In terms of the results printed to the screen for the throughput, the program will calculate the throughput in Mbps and then the time 
taken to transfer a 10GB file at the calculated throughput. It also prints out additional information such as the Protocol, 802.11 Standard, 
Data Rate, Number of Spatial Streams (Nss) and Number of Channels (NChan).

SHOW THE PRINT OUT

The main output of my program is the throughput and time taken to transfer 10GB of data for the "Normal" case and "Best" case. It does this by storing the best
case or maximum values for NChan and Nss in the config.py file and using these to change the number of bits per OFDM symbol.
This results in a normal case result for 20MHz 1SS and a best case result for the throughput for example 160MHz 8SS for 802.11ax. 

THIS IS SHOWN HERE

#### Design 
In this section, I will speak about the design of my program between the 3 Python files, config.py, main.py and func.py.

- Main.py is the main Python file which handles the majority of the calculations and output to the Terminal for the user so they can understand their results.

- Func.py has 2 functions which are used to print out lists of items from either dictionaries or Python lists.

- Config.py is used to hold all of the 802.11 standard information from MAC Header sizes, SIFS, Preambles and other data rate
specific data. This data is used for all of the calculations and this makes sure that the program is as interchangeable and usable to multiple people. They only need
a specifically setup configuration file and all of the program's source code should work interchangeably. 

#### Usage
- Running the program, you will first be prompted to enter a number stating your choice of protcol of either TCP or UDP 
followed by pressing "Enter". 
- Then choose a relevant 802.11 standard from the list shown by entering a relevant numerical choice and pressing "Enter"
- Choose a data rate for this chosen standard from the list shown in the 20MHz, 1SS Normal case. 
- From here, the result will be printed to the screen for throughput and the time taken to transfer 10GB of data for both
the "Normal" case and the "Best" case. 

### Why is there a difference between the actual throughput and the advertised data rate?
The answer to this question lies with the amount of overhead required to send a simple 1500 byte data packet at an advertised data rate.
For each advertised data rate, the number of bits per OFDM symbol, number of channels and bits all change thus representing a different result everytime between seemingly very close data rates.
We can also see the amount of overhead or extra items needing to be transmitted with the data packet such as CTS, RTS, ACKs and Preambles. We also have to take account for all of the delays 
placed in the channel such as DIFS, SIFS and in the case of 802.11g, a signal extension. We also need to encapsulate the data frame with a MAC Header and SNAP LLC headers. Each OFDM frame has 6 tail bits 
appended to each frame and this adds to the overhead associated with the transmission. 

We can also consider the case of TCP. In the case of TCP, you are transmitting a lot more overhead and data as you need a whole data stream for the TCP ACK and you can also not transmit again until the
TCP ACK has been received. This obviously results in a lower throughput than the advertised data rate. 
There are also other cases not associated with the physical data or headers transferred with the data. This is most notable in the case of interference on the WLAN channel such as other 
devices interfering nearby and random noise in the channel but this does not apply to our program's results as it does not take into account real world interferences. 

### 802.11 performance improves after each release. Briefly discuss the trade-offs involved in such improvements. 
Some of the improvements in 802.11 standards over recent years are higher reliability, larger bandwidths and more channels to transfer data on as well as supporting MIMO and MU-MIMO (Multi user MIMO).
There have also been improvements to support both 2.4GHz and 5GHz in terms of WLAN frequency. The tradeoffs for these improvements mainly lie in the range and coverage of the improving standards 
which are in turn influenced by the transmit power as more power is needed to be used to transmit at the much higher rates advertised. This obviously means that such Access Points or Wireless devices 
must either be connected to a Mains power connection or have a very large battery to be used. As the standards have improved and such improvements such as 802.11n to 802.11ac with MIMO to MU-MIMO,
the channels suffer from interference and noise from adjacent channels and co-channels between multiple users. 
This means that thought and care must be taken when locating cells or APs so as to not cause large amounts of interference. 
