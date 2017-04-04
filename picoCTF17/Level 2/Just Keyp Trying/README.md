# Challenge

Here's an interesting capture of some data. But what exactly is this data? Take a look: data.pcap

# Walkthrough/Solution

Opening the packet file in Wireshark showed us 66 frames of data with the information `URB_INTERRUPT IN`. The frames also suggested that this packet capture is related to USB devices. </br>

Scrolling through the packets, we see that the value `0x1d` in the `packet bytes` view keeps changing. Correlating to the [pdf file](http://www.usb.org/developers/hidpage/Hut1_12v2.pdf) provided and the title name, I narrowed down to `Table 12: Keyboard/Keypad Page`. </br>

Collecting all the values of `0x1d` starting from frame 1 to 66, I got this list of hex values:

```
09 0f 04 0a 
2f 13 15 20 
22 22 2d 27 
11 1a 04 15 
07 16 2d 25 
22 26 26 22 
20 1f 20 30 06
```
Decoding the hex values corresponding to the table value gives us `flag{pr355_0nwards_85995323}c`

# Potential exercises
1) Looking into automating the process using `Scapy`
2) Using `USBPcap` to understand how to generate a usb pcap file

# Learning Outcome
1) Analysis on usb pcap files
