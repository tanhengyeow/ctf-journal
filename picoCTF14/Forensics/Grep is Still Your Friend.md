# Challenge

The police need help decrypting one of your father's files. Fortunately you know where he wrote down all his backup decryption keys as a backup (probably not the best security practice). You are looking for the key corresponding to `daedaluscorp.txt.enc`. The file is stored on the shell server at `/problems/grepfriend/keys`.

# Walkthrough/Solution

Change directory by running this command `cd /problems/grepfriend/` in the shell. Type man for grep for help on how to use the command. Run the command `cat keys | grep daedaluscorp.txt.enc` and you will find the decryption key displayed in plaintext.

# Learning Outcome

Grep is a useful tool to search data admist a chunk of data

