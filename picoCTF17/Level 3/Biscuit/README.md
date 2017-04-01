# Challenge

Your friend has a personal website. Fortunately for you, he is a bit of a noob when it comes to hosting a website. Can you find out what he is hiding? Website.

# Walkthrough/Solution

The name of the challenge and the background of the webpage suggested that this challenge has something to do with cookies. Upon viewing the page source, we noticed that there is comment saying:

```
<!-- Storing stuff in the same directory as your web server doesn't seem like a good idea -->
<!-- Thankfully, we use a hidden one that is super PRIVATE, to protect our cookies.sqlite file -->
```
Also, the background image is stored in the /private folder. With these information, I tried to access private/cookies.sqlite managed to download the file. Opening cookies.sqlite in sqlitebrowser and going to the `Browse Data` tab showed us the localhost entry with filter value `F3MAqpWxIvESiUNLHsflVd`. </br>

Since the client has control over HTTP requests, we can make use of the curl (a tool used to transfer data to or from a user without user interaction) to spoof the value of the cookie to a valid user (possibly the administrator). </br>

`curl -v http://shell2017.picoctf.com:54399/ --cookie ID=F3MAqpWxIvESiUNLHsflVd`

And we are given the flag! `our flag is: 7480ef727bda99d85a218b75c3f3157f`

# Learning Outcome

1) Using sqlitebrowser
2) Understanding HTTP requests
3) Client-side controls using cookies


