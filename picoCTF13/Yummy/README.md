# Challenge

Score: 60

You want to find out the docking bay numbers for space ships that are ready to launch. Luckily for you, the website for the docking bay ship status page doesn't seem so secure....

Enter the docking bay for any of the ships that are awaiting launch.

# Walkthrough/Solution

Upon visiting the webpage, it shows us that we are not authorized to view the webpage. When we view the page source, there is a comment indicating that an expected Cookie: "authorization=administrator is needed for us to authorize as an admin. </br></br> Since users have controls over the fields of the HTTP header, we can modify the cookie value to login as the administrator. An easy way to do this through the command line would be using curl. a tool used to transfer data to or from a user without user interaction. On your linux machine, install curl if you haven't already done so:

`sudo apt-get install curl` </br></br>

You can explore the curl command by typing `man curl` but a straightforward way to change the cookie value of the http request would be by doing so: </br></br>

`curl -v https://2013.picoctf.com/problems/yummy/ --cookie authorization=administrator`

We are logged in as admin and the docking bay for ships that are awaiting launch is `DX4-9`

# Learning Outcome

1) HTTP Request Headers
2) Curl

