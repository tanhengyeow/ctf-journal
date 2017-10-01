# Challenge

Oscar is more of an offline type of guy. Can you hack in his platform?

# Walkthrough/Solution

Upon visiting the website, a login prompt was presented. Viewing the source of the page shows that there is script which is validating the form being submitted. 

I overwrote the function in console using:
```
function validateForm() {return true;}
```

Viewing the source on the next page shows the following script:
```
<script>
Offline.options = {	
	// Should we check the connection status immediatly on page load.
	checkOnLoad: false,
	// Should we monitor AJAX requests to help decide if we have a connection.
	interceptRequests: true,
	// Should we automatically retest periodically when the connection is down (set to false to disable).
	reconnect: {
	// How many seconds should we wait before rechecking.
	initialDelay: 3,
	// How long should we wait between retries.
	delay: (1.5 * last delay, capped at 1 hour)
	},
	// Should we store and attempt to remake requests which fail while the connection is down.
	requests: true
	// Should we show a snake game while the connection is down to keep the user entertained?
	// It's not included in the normal build, you should bring in js/snake.js in addition to
	// offline.min.js.
	game: false
	}
</script>
```

This shows that the page is using functionalities of the imported offline-js library. I changed some settings in `Offline.options` and experimented around. Upon disconnection from internet access, this prompt was shown:

![](https://github.com/tanhengyeow/ctf-journal/blob/master/dctf-quals-2017/super-secure/src/super-secure.jpg)

This is a sign that the message lies somewhere where the user can see it (probably the css files).

You can find the flag `DCTF{76c77d557198ff760ab9866ad1261a01a7298c349617cc4557462f80500d56a7}` when you view `slide2.css`.

# Learning outcome
1. Overridding functions
