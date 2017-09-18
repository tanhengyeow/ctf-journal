# Challenge 

nc misc.chal.csaw.io 4239

# Walkthrough/Solution

Connecting to the port displays the following prompt I got at that point of time:

```
8-1-1 even parity. Respond with '1' if you got the byte, '0' to retransmit.
01110011001
```
To solve this challenge, you need to understand the [8-N-1 notation](https://en.wikipedia.org/wiki/8-N-1). 

Adapting from the 8-N-1 notation, the approach to this challenge would be to check the following:
1. If the number of 1s in the data chunk is EVEN and the parity bit is 0, you would receive the byte.
2. If the number of 1s in the data chunk is ODD and the parity bit is 1, you would receive the byte.
3. Any other combinations would result in you not receiving the byte.

With that in mind, a hackish python script is used to solve this challenge:
```
#!/usr/bin/python

from pwn import *
import binascii

r = remote('misc.chal.csaw.io','4239')
flag = ""

while True:

    currLine = r.recvline()
    print currLine
    
    if "}" in flag:
        print flag
        break
   
    count = 0
    parity = 0
    store = 0
    power = 7
    for field in currLine.split():
        field = field.rstrip("\n")
        if field.isdigit():   
            # 8-N-1 notation
            for i in range(1,9):
                store += 2**(power) * int(field[i])      
                power-=1
                if int(field[i]) == 1:
                    count += 1

            parity = int(field[9])
 
            if count %2!=0 and parity == 1:
                print 'Number of 1s in data chunk is',count,', this is ODD and parity bit is 1, so responding with \'1\''
                r.sendline('1') 
                flag += chr(store)
                print 'Current flag:',flag
            elif count %2==0 and parity == 0:
                print 'Number of 1s in data chunk is',count,', this is EVEN and parity bit is 0, so responding with \'1\''
                r.sendline('1')
                flag += chr(store)
                print 'Current flag:',flag
            else:
                print 'Didn\'t match any of the requirements, so responding with \'0\''
                r.sendline('0')
```
And the flag is `flag{@n_int3rface_betw33n_data_term1nal_3quipment_and_d@t@_circuit-term1nating_3quipment}`.

# Learning outcome
1. 8-N-1 notation
2. Serial communication
3. Python scripting
