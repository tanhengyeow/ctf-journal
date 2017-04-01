# Challenge

This program requires some unprintable characters as input... But how do you print unprintable characters? CLI yourself to /problems/b20c0c219ef2c830da927f80fb7e9cd3 and turn that Hex2Raw!

# Walkthrough/Solution

Executing the program hex2raw, it prompted us to change the hex `88a5e3d5caa34e85e5f36cd55d776568` to raw format. Since raw content cannot be printed and intepreted properly, copying and pasting would not do. </br>

Therefore, we can do this. In your root directory, perform this command `echo 88a5e3d5caa34e85e5f36cd55d776568 | xxd -r -p > hex2raw.txt` to convert the hex to raw format and save it to a text file. </br>

`-r convert (or patch) hexdump into binary` and `-p tells the program to use a plain format` </br>

Then we can pipe in the contents of the text file to the program through this command `cat hex2raw.txt | /problems/b20c0c219ef2c830da927f80fb7e9cd3/hex2raw` and we get the flag `2bdd0a8259fcada3c12d732c7f3ca98a
`

# Learning Outcome

1) Converting hex to raw content
2) Piping content into another program
