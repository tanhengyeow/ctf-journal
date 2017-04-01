# Challenge

We found a program that is hiding a flag but requires you to guess the number it is thinking of. Chances are Linux has an easy way to try all the numbers... Go to /problems/e3f1970eb419b3aa32788a43ec91ef08 and try it out!

# Walkthrough/Solution

Create a bash script on your root directory (since you have have permissions to do so anywhere else). You can use the vim editor to write your script, `vim bashloop_script`. </br>

Here is a simple bash script that I use for this challenge: 

```
#!/bin/bash

for i in {0..4096}
do
	/problems/e3f1970eb419b3aa32788a43ec91ef08/bashloop $i
done
```

Make your script executable by doing this, `chmod u+x bashloop_script` and run it by typing `./bashloop_script`. </br>

You noticed that all negative results start with the word "Nope". Thus, we can filter the negative results and show only the positive one by doing this `./bashloop_script | grep -v ^Nope`

And you get the flag `9960332950d7db392f97f29dee04f4ee`!

# Learning Outcome

1) Introduction to bash scripting/passing command line arguments
2) Usage of the grep command
