# Challenge

--Dot Code--

Find me!

Download file:

http://material.wargame.whitehat.vn/contests/13/Hue.zip

<md5:b825837dcc3f236e0ed5d90f65b8dc36>

Backup:

http://bak.material.wargame.whitehat.vn/contests/13/Hue.zip

<md5:b825837dcc3f236e0ed5d90f65b8dc36>

# Walkthrough/Solution

Extracting `hue.zip`, we are presented with a folder named `my collection` and a zip file named `openme.zip`. Similar to the challenge `Con Dao Islands`, the zip file is encrypted with a password so the clue to the password probably lies in the folder. 

The folder contains images of different country flags and a QR code that is broken up into 16 images. I used this [website](http://qrcode.meetheed.com/question14.php) to help me understand the structure of a QR code and managed to pieced the 16 images together.

I proceeded to use a QR code scanner to scan the [QR code](https://github.com/tanhengyeow/ctf-journal/blob/master/whitehat-contest-13/hue-200/img/QR-code-hue.png), giving me the string "=== Ea5y p4ssw0rd h4h4 ===", which is the password to `openme.zip`.

Extracting `openme.zip` presents us with a text file named `flag.txt` and an image file `here.png`. The text file shows "It's not here ^^", which means the clue lies in the image file. The image file corresponds to the title named "--Dot Code--", which is a clue that we are supposed to decipher the message in braille.

---To be continued---

