# Challenge

Prove your knowledge of hashes and claim a flag as your prize! Connect to the service at shell2017.picoctf.com:9661

# Walkthrough/Solution

To connect to the port, use netcat: `nc shell2017.picoctf.com 9661` </br>

Welcome to Hashes 101! There are 4 Levels. Complete all and receive a prize! 

`-------- LEVEL 1: Text = just 1's and 0's --------` </br>

`All text can be represented by numbers. To see how different letters translate to numbers, go to http://www.asciitable.com/`

`TO UNLOCK NEXT LEVEL, give me the ASCII representation of 0111000001100101011000010110001101100101`

Ans: Converting the binary number `0111000001100101011000010110001101100101` to ASCII gives us `peace`.

`------ LEVEL 2: Numbers can be base ANYTHING -----` </br>

`Numbers can be represented many ways. A popular way to represent computer data is in base 16 or 'hex' since it lines up with bytes very well (2 hex characters = 8 binary bits). Other formats include base64, binary, and just regular base10 (decimal)! In a way, that ascii chart represents a system where all text can be seen as "base128" (not including the Extended ASCII codes)`

`TO UNLOCK NEXT LEVEL, give me the text you just decoded, peace, as its hex and decimal equivalent`

Ans: Converting `peace` to hex gives us `7065616365`. Converting `7065616365` to decimal gives us `482737218405`.

`----------- LEVEL 3: Hashing Function ------------` </br>

`A Hashing Function intakes any data of any size and irreversibly transforms it to a fixed length number. For example, a simple Hashing Function could be to add up the sum of all the values of all the bytes in the data and get the remainder after dividing by 16 (modulus 16)`

`TO UNLOCK NEXT LEVEL, give me a string that will result in a 4 after being transformed with the mentioned example hashing function`

Ans:

Let unknown variable be x. </br>

x mod 16 = 4 </br>

4 = x - 16(any positive integer >= 1, e.g. 5) </br>

x = 16*5 + 4 = 84, equivalent to ASCII character T </br>

`--------------- LEVEL 4: Real Hash ---------------` </br>

`A real Hashing Function is used for many things. This can include checking to ensure a file has not been changed (its hash value would change if any part of it is changed). An important use of hashes is for storing passwords because a Hashing Function cannot be reversed to find the initial data. Therefore if someone steals the hashes, they must try many different inputs to see if they can "crack" it to find what password yields the same hash. Normally, this is too much work (if the password is long enough). But many times, people's passwords are easy to guess... Brute forcing this hash yourself is not a good idea, but there is a strong possibility that, if the password is weak, this hash has been cracked by someone before. Try looking for websites that have stored already cracked hashes.` </br>

`TO CLAIM YOUR PRIZE, give me the string password that will result in this MD5 hash (MD5, like most hashes, are represented as hex digits): 05635c2378051c67022b9096e0813aeb` </br>

Ans: Decrypting the hash 05635c2378051c67022b9096e0813aeb gives us `r3v3l`

You completed all 4 levels! Here is your prize: `c3ee093f26ba147ccc451fd13c91ffce`

# Learning Outcome

1) Number base system/ASCII
2) Role of modulus function in security
3) Hashes
