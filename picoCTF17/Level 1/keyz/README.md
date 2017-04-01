# Challenge

While webshells are nice, it'd be nice to be able to login directly. To do so, please add your own public key to ~/.ssh/authorized_keys, using the webshell. Make sure to copy it correctly! The key is in the ssh banner, displayed when you login remotely with ssh, to shell2017.picoctf.com

# Walkthrough/Solution

To summarize how the RSA authentication works:

Description | Steps
--- | --- 
Shell Server (which you are connecting to) | <ul>1. The public key placed in ~/.ssh on the shell server.</ul><ul>2. The public key contents copied into ~/.ssh/authorized keys on the shell server.</ul>
Personal Computer (I'm using linux) | <ul>1. Generate a pair of public and private keys by using `ssh-keygen -t rsa` </ul> <ul>2. Store the public and private keys in your ~/.ssh folder</ul>

If you did it correctly, `ssh <team name>@shell2017.picoctf.com` and you get the flag `who_needs_pwords_anyways`. Refer to this [link](https://www.linode.com/docs/security/use-public-key-authentication-with-ssh) if you are using Windows or need more help.

# Learning Outcome

1) RSA Authentication
2) How to generate keys and configure them
