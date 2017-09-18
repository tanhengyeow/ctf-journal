#!/usr/bin/python

from pwn import *

def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10

def is_luhn_valid(card_number):
    return luhn_checksum(card_number) == 0


r = remote('misc.chal.csaw.io','8308')

americanExpress = [line.rstrip('\n') for line in open('american-express.txt')]
visa = [line.rstrip('\n') for line in open('visa.txt')]
masterCard = [line.rstrip('\n') for line in open('mastercard.txt')]
discover = [line.rstrip('\n') for line in open('discover.txt')]

acount=vcount=mcount=dcount=startIndex=0
while True:
    
    currLine = r.recvline()
    print currLine
    if "flag" in currLine:
        break
 
    if "Discover" in currLine:
        sendLine = r.sendline(discover[dcount])
        print 'Sending discover:', discover[dcount] 
        dcount+=1
    elif "MasterCard" in currLine:
        r.sendline(masterCard[mcount])
        print 'Sending mastercard:', masterCard[mcount] 
        mcount+=1
    elif "American Express" in currLine:
        r.sendline(americanExpress[acount])
        print 'Sending american express:', americanExpress[acount] 
        acount+=1
    elif "Visa" in currLine:
        r.sendline(visa[vcount])
        print 'Sending visa:', visa[vcount] 
        vcount+=1
    elif "starts with" in currLine:
        number = 0
        validccNumber = 0
        for field in currLine.split():
            field = field.rstrip('!')
            if field.isdigit():
                number = field
                break

        ccNumber = int(number) * 100000000
       
        while True:
            result = is_luhn_valid(ccNumber+startIndex)
            if result == True:
                validccNumber = ccNumber + startIndex
                break
            startIndex+=1
 
        r.sendline(str(validccNumber))
        print 'Sending valid cc number:',validccNumber
    
    elif "ends with" in currLine:
        number = 0
        ccNumber = 0
        validccNumber = 0
        for field in currLine.split():
            field = field.rstrip('!')
            if field.isdigit():
                number = field
                break

        if len(str(number)) == 1:
            while True:
                acount+=1
                if int(americanExpress[acount])%10 == int(number):
                    validccNumber = int(americanExpress[acount])
                    break

            r.sendline(str(validccNumber))
            print 'Sending valid cc number:',validccNumber
        else:
            ccNumber = 4001150000000000 + int(number)
            while True:
                result = is_luhn_valid(ccNumber+startIndex*10000)
                if result == True:
                    validccNumber = ccNumber+startIndex*10000   
                    break
                startIndex+=1
            r.sendline(str(validccNumber))
            print 'Sending valid cc number:',validccNumber

    elif "need to know" in currLine: 
        for field in currLine.split():
            field = field.rstrip('!')
            if field.isdigit():
                number = field
                break
        if len(number) == 16:
            length = True
        else:
            length = False
        
        result = is_luhn_valid(int(number))
        if result == True and length == True:
            r.sendline('1')
            print 'Sending 1=Yes'
        else:
            r.sendline('0')
            print 'Sending 0=No'
