# Challenge

Can you help me find the data in this littleschoolbus.bmp?

# Walkthrough/Solution

The name of the title and the hint suggested that the data is encoded in the least significant bit. A good resource on LSB Encoding can be found [here](https://cyfor.engineering.nyu.edu/topic/02-lsb-steganography/). </br>

I used stegsolve for this task. Follow this [guide](https://github.com/zardus/ctf-tools/blob/master/stegsolve/install) on how to install and execute the tool. </br>

Exploring the tool provides us with the `Data Extract` function. Since the image is opaque, I figured that it should be only ordered by R, G, and B fields only. Read more about RGB color specification [here](https://stat.ethz.ch/R-manual/R-devel/library/grDevices/html/rgb.html). </br>

Selecting the LSB, `0` of the R,G and B fields and setting the order settings to  `Extract by row` and bit order to be `MSB First`, I proceeded to preview the data extract. Nothing seemed interesting and I meddled with the bit plane order. </br>

Finally, choosing the `BGR` bit plane order gives us `flag{remember_kids_protect_your_headers_b1bb}`

# Learning Outcome

1) LSB encoding
2) Using stegsolve
