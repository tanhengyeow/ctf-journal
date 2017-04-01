# Challenge

A program at /problems/02bd7d8f7e9c13a19940fd1116234469 has access to a flag but refuses to share it. Can you convince it otherwise?

# Walkthrough/Solution

On the shell server, navigate to /problems/02bd7d8f7e9c13a19940fd1116234469 and we are presented with the source code of the program `justno`. </br>

The source code seems to be comparing the string in the file `auth` with the string `no`. If we can compare the string `no` with a different string in the `auth` file, the program would print out the flag. </br>

At the start of the source code, the code seems to be reading the contents of the `auth` file relative to the user's directory. Using this knowledge, we can create a similar directory `/problems/02bd7d8f7e9c13a19940fd1116234469` on our root directory and create our own auth file containing contents with anything but `no` in the newly created directory, `echo yes > auth`. </br>

Executing the program `/problems/02bd7d8f7e9c13a19940fd1116234469/justno` from our directory `/home/<team name>/problems/02bd7d8f7e9c13a19940fd1116234469` gives us the flag :) </br>

`Oh. Well the auth file doesn't say no anymore so... Here's the flag: cad7c91983f6a8ed691c6d7e2dd2264c`

# Learning Outcome

1) Relative path/Absolute path

