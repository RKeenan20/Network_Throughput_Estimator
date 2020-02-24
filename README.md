# Advances in Wireless Networking COMP40660
## Assignment 1: 802.11 Throughput
### Robert Keenan 15333066

#### Design and Usage
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

##### Design 
In this section, I will speak about the design of my program between the 3 Python files, config.py, main.py and func.py.

- Main.py is the main Python file which handles the majority of the calculations and output to the Terminal for the user so they can understand their results.

- Func.py has 2 functions which are used to print out lists of items from either dictionaries or Python lists.

- Config.py is used to hold all of the 802.11 standard information from MAC Header sizes, SIFS, Preambles and other data rate
specific data. This data is used for all of the calculations and this makes sure that the program is as interchangeable and usable to multiple people. They only need
a specifically setup configuration file and all of the program's source code should work interchangeably. 
