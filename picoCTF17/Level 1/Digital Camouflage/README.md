# Challenge

We need to gain access to the school routers to cover our tracks. Let's try and see if we can find the password in the network data we captured earlier: data.pcap

# Walkthrough/Solution

To analyse packet files, we will be using wireshark in this case. Data can be sent with two methods POST or GET. The password authentication process should be using the POST method for data transmission. </br> 

We can perform a filter of the network packets using this `http.request.method == "POST"`. </br> 

After performing the fitler, we noticed a single stream and we can right click > follow  tcp stream to view the details of the packet. </br>

The password is url encoded and we when we url decode it, it  gives us `UjZBS05oV3dvNw==`. This string seems like it is base-64 encoded because of the double `==` pads behind the string. When we perform a base-64 decode, we get the password `R6AKNhWwo7`

# Learning Outcome

1) Using wireshark
2) Packet filters
3) URL & Base64 Encoding/Decoding

# Resources

http://www.hacking-tutorial.com/hacking-tutorial/how-to-sniff-http-post-password-via-network-using-wireshark-network-analyzer/#sthash.Jaa9cZsN.dpbs
