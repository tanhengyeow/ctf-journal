#!/usr/bin/python

import random, string
import math 

random.seed("random")

store_rand = []

flag = "BNZQ:449xg472190mwx6869b8pt10rwo92624"
decflag = ""

i = 0

for c in flag:
  if c.islower():
    #rotate number around alphabet a random amount
    #chr( (ord(c)-ord('a')+random.randrange(0,26))%26 + ord('a') )
    store_rand.append(random.randrange(0,26))
    letter = ord(c)-ord('a') + abs(-ord('a')+store_rand[i])
    if (letter < ord('a')):
	decflag += chr(letter+26)
    else:
	decflag += chr(letter)
    i += 1
  elif c.isupper():
    store_rand.append(random.randrange(0,26))
    letter = (ord(c)-ord('A') + abs(-ord('A')+store_rand[i]))
    if (letter < ord('A')):
	decflag += chr(letter+26)
    else:
	decflag += chr(letter)
    i += 1
  elif c.isdigit():
    store_rand.append(random.randrange(0,10))
    digit = (ord(c)-ord('0') + abs(-ord('0')+store_rand[i]))
    if ( digit < ord('0')):
	decflag += chr(digit+10)
    else:
	decflag += chr(digit) 
    i += 1
  else:
        decflag += c
print "Guessably Randomized Flag: " + decflag

