# Challenge

This program just prints a flag in raw form. All we need to do is convert the output to hex and we have it! CLI yourself to /problems/7ed72aec10a93d978ec3542055975d36 and turn that Raw2Hex!

# Walkthrough/Solution

This challenge is basically an opposite of what we did in Hex2Raw. We can redirect the output produced by the program raw2hex into a text file by doing this `/problems/7ed72aec10a93d978ec3542055975d36/raw2hex > raw2hex.txt` </br>

Next, we pass the content of the text file and pipe it xxd, which performs a hexdump of the content, `cat raw2hex.txt | xxd -p > raw2hexfinal.txt` </br>

`cat raw2hexfinal.txt` and we get the flag `54686520666c61672069733a233a338f3052fec75f009f2485ac5352`

# Learning outcome

1) Converting raw content to hex
2) Piping content into another program
3) The xxd tool
