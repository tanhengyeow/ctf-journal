#!/usr/bin/python
from PIL import Image
import random
def expand(s):
	while(len(s) < 8):
		s = ''.join(['0',s])
	return s
message = "************"
key =     '336460560072702347617456615303204617152713067320010076351372505074576134036106626534024762437731571312133465747452003467036033535104133372012112104702656655752602403516725117437326242451146013652105152711113551131073727506327102760600510467334606012231251130155023132116320137622232717524237536136534046404652375162406731540244254105316262171607753120103731703'
im = Image.open("sadfrog.png")
old_pix = im.load()
red, green, blue = im.split()
width, height = im.size
encode_image = Image.new("RGB",(width,height))
pix_values = list(im.getdata())
pix = encode_image.load()
t = 0
kt = 0 
x = 0
y = 0
red1 = 0
green1 = 0
blue1 = 0
for i in range(width):
	if(kt == 1):
		break
	for j in range(height):
		new_red = bin(red.getpixel((i,j)))[2:]
		print "first: " + new_red
		new_red = expand(new_red)
		print "second: " +  new_red
		list_red = list(new_red)
		list_red[7-int(key[t])] = message[t]
		new_red= ''.join(list_red)
		if(t == (len(message) -1)):
			kt = 1
			if(j < height-1):
				y = j+1
				x = i
			else:
				x =i+1
				y = 0
			red1 = int(new_red,2)
			break
		else:
			t = t+1
		new_green = bin(green.getpixel((i,j)))[2:]
		new_green = expand(new_green)
		list_green = list(new_green)
		list_green[7-int(key[t])] = message[t]
		new_green= ''.join(list_green)
		if(t == (len(message) -1)):
			kt = 1
			if(j < height-1):
				y = j+1
				x = i
			else:
				x =i+1
				y = 0
			green1 = int(new_green,2)
			break
		else:
			t = t+1
		new_blue = bin(blue.getpixel((i,j)))[2:]
		new_blue = expand(new_blue)
		list_blue = list(new_blue)
		list_blue[7-int(key[t])] = message[t]
		new_blue= ''.join(list_blue)
		if(t == (len(message) -1)):
			kt = 1
			if(j < height-1):
				y = j+1
				x = i
			else:
				x =i+1
				y = 0
#			blue1 = int(new_blue,2)
			break
		else:
			t = t+1
#		pix[i,j] = (int(new_red,2),int(new_green,2),int(new_blue,2))
pix[x,y-1] = (red1,green1,blue1)
for i in range(x,width,1):
	for j in range(y,height,1):
		pix[i,j] = old_pix[i,j]
encode_image.save("testfrog.png")
#author: Handsome rubick
