# Challenge

I was told to use the linux strings command on yarn, but it doesn't work. Can you help? I lost the flag in the binary somewhere, and would like it back.

# Walkthrough/Solution

Running `strings yarn` doesn't give us much information. Knowing that the `strings` command searches for a default of 4 characters, we can actually customize the length of the string we want to search. </br>

Executing `strings -n 3 yarn` shows us the flag `Submit_me_for_I_am_the_flag` broken up in chunks of 3.

# Learning Outcome
1) Customized usage of the `strings` command
