# Challenge
--Faces--

Pass the test to take the flag. Then fly to Con Dao islands, one of Vietnam's star attractions.

Downloadfile:

http://material.wargame.whitehat.vn/contests/13/faces.zip

<md5:7a73971d985701fa86379c6dbfa84722>

Backup:

http://bak.material.wargame.whitehat.vn/contests/13/faces.zip

<md5:7a73971d985701fa86379c6dbfa84722>

# Walkthrough/Solution
Extracting the files `faces.zip`, we are presented with a zip file named `SadFrog.zip` and a text file named `Password.txt`. The zip file is encrypted with a password so it means we have to obtain the password by decoding `Password.txt`.

The text file contains lenny faces and with a bit of research, I managed to narrow down to this [website](https://esolangs.org/wiki/(_%CD%A1%C2%B0_%CD%9C%CA%96_%CD%A1%C2%B0)fuck), stating that the lenny faces are a derivate of an esoteric programming language named Brainfuck. 

Decoding the lenny faces in the text file, this string is obtained `++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>>++++.<------.>++++++++++++++.<-------------.+++++++++++++++++++.>-.-------.<------------.<++++++++++++.`

I used this [website](http://www.dcode.fr/brainfuck-language) to decode the above string and the password to `Sadfrog.zip` is `h@v3Fun:*`. Extracting the files in the zip file gives us a python script `encrypt.py` and an image file named `Sadfrog.png`.

---To be Continued---
