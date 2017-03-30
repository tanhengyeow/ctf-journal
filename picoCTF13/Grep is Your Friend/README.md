# Challenge

Score: 40

After plugging the robot into the computer, the robot asks for the name of a file containing the string SECRET AUTH CODE. You can find it using the command-line interface in /problems/grep.tar or by downloading all of the files.

# Walkthrough/Solution

Save the file grep.tar into your linux machine. Run this command to unpack the tar file and save the contents into another directory:  </br></br> `tar -xf grep.tar -C /grep` </br></br>

We are asked to find the name of the file containing the string `SECRET AUTH CODE`. Using the help of grep, we can run this command to find the file name. </br></br>

`strings * | grep -r "SECRET AUTH CODES"` </br></br>

We get the result `fHYYpdrfeOCHyQicfe96xfw==:SECRET AUTH CODES`

# Learning outcome

1) Use of Grep. Grep is a powerful tool for searching specific data admist a chunk of data.

