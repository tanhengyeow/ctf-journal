# Challenge

I really need to login to this website, but the developer hasn't implemented login yet. Can you help?

# Walkthrough/Solution

Upon viewing the webpage and viewing the page source, we noticed that there is a javascript processing the password input. Looking at the javascript functions closely, the validate function is called after storing the user input into a variable pword. </br>

The validate function always returns false, which is a value what is anything but `1`. Using the value returned by the validate function, an ajax request is made to the server with a `false` input. Since javascripts can be controlled at the client side, we can manipulate the results. </br>

Right click > Inspect > Sources and you can see the contents of the javascript and a console being presented to you. We can call the function and input a true value to it `make_ajax_req(1)` and this returns us the flag `client_side_is_the_dark_side0c97381c155aae62b9ce3c59845d6941`

# Learning Outcome

1) Client-side controls with javascript

