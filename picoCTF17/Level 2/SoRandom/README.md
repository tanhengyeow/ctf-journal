# Challenge

We found sorandom.py running at shell2017.picoctf.com:16768. It seems to be outputting the flag but randomizing all the characters first. Is there anyway to get back the original flag?
Update (text only) 16:16 EST 1 Apr Running python 2 (same version as on the server).

# Walkthrough/Solution

Looking at the `sorandom.py`, it is using a fixed seed through `random.seed("random")`. Thus it is generating a fixed sequence of random numbers generated. Reversing the order of the operation gives us the original flag. </br>

This is the script I used:

```
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
```

And we get the flag `FLAG:107bd559693aef6692e1ed55ebe29514`

# Learning Outcome
1) Pseudorandom numbers
2) Python scripting
