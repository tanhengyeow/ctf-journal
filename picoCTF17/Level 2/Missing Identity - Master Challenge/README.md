# Challenge

Turns out, some of the files back from Master Challenge 1 were corrupted. Restore this one file and find the flag.

# Walkthrough/Solution

We are given a file and running the command `file file` tells us that it is a data file. When we view the contents of the data file in hexeditor, we see that the file signature is corrupted. </br>

Performing `strings -a` on `file` shows the file signature for zip file, which is PK. Googling the file signature for PK tells us that the magic number is `50 4B 03 04`. Use any hex editor of your choice, and change the first byte of the file to the magic number `50 4B 03 04`. </br>

Change the extension of `file` by using `mv file file.zip` and `unzip file.zip`. </br>

The flag is `ZIPPIDYDOoda44282245` as shown in the image of flag.png

# Learning outcome

1) File signatures/Magic Number
