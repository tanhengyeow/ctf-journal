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

