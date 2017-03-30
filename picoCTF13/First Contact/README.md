# Challenge

Score: 40

You notice that the indicator light near the robot’s antenna begins to blink. Perhaps the robot is connecting to a network? Using a wireless card and the network protocol analyzer Wireshark, you are able to create a PCAP file containing the packets sent over the network.

You suspect that the robot is communicating with the crashed ship. Your goal is to find the location of the ship by inspecting the network traffic.

You can perform the analysis online on Cloudshark or you can download the PCAP file.

# Walkthrough/Solution

When we visit https://www.cloudshark.org/captures/bc1c0a7fae2c to analyse the network traffic, we noticed tcp streams. TCP is a connection-oriented protocol meaning it first sets up a connection to the receiver then sends the data in segments (PDU for transport layer) which is carried by IP packets. This way it's called stream because it keeps the stream of data between to ends during transfer. Using analysis tools to follow one of the tcp stream, we noticed that the new location coordinates are `37 14'06"N 115 48'40"W`

# Learning outcome

1) Analysing pcap files
2) TCP streams
