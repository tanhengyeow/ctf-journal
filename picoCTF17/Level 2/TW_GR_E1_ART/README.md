# Challenge

Oh, sweet, they made a spinoff game to Toaster Wars! That last room has a lot of flags in it though. I wonder which is the right one...? Check it out here.

# Walkthrough/Solution

First challenge to the Toaster Wars series. It was fun solving this challenge :) </br>

First, we are directed to the game consisting of 4 floors. When we reach the last stage, there are many flags and we are supposed to find the right one to reveal the flag to the challenge. </br>

The hint was that the game was running on a Node.js server. Referring to this [link](https://www.sitepoint.com/beginners-guide-node-package-manager/), we noticed the existence of npm. </br>

All npm packages contain a file, usually in the project root, called package.json - this file holds various metadata relevant to the project (Refer to this [link](https://docs.nodejitsu.com/articles/getting-started/npm/what-is-the-file-package-json/) for more information). </br>

Visiting http://shell2017.picoctf.com:50787/package.json shows us the dependencies and the server's javascript on server/serv.js </br>

Notice that there are many `require` functions being called. The field `require("./game")(app, io)` seemed interesting and I got 
access to /server/game.js, which is the source code of the game. </br>

In game.js, the module exports a function `module.exports = function(app, io){ ... }`, in this case, a reference to the express app and the 
Socket.IO server when the developer import it in serv.js, which explained the field `require("./game")(app, io)`.

Viewing the source code, there's an interesting code snippet:

```
case "revealFlag":
  if (entity.items[action.item].effects[i].check == 64) {
    outcome.flag = process.env["PICO_CTF_FLAG"];
	}
  break;
```

Viewing the source code of the config file in `/server/config.js` tells us that the flag is arranged in order through the code snippet:

```
items: Array.from(new Array(83), (_, idx) => {
	if (idx >= 2) {
		idx++
	}

	if (idx >= 77) {
		idx++;
	}

	var r = Math.floor(idx / 5) + 1;
	var c = (idx % 5) + 1;

	return createFlag(idx, { r: r, c: c });
	}),
```
We can also confirm that the id is the value `64 + 100 = 164` through the previous code snippet `entity.items[action.item].effects[i].check == 64` and the following function: 

```
function createFlag(check, location) {
	return {
		name: "Flag",
		description: "Gives you the flag... maybe.",
		location: location,
		use: 0,
		id: check + 100,
		sprite: "flag",
		effects: [
			{
				type: "revealFlag",
				check: check
			},
			{
				type: "destroyItems"
			}
		]
	};
}
```

Using this information, I picked up the flag at the 64th position and confirmed the value of the id by viewing at the `state` object in developer tools under public/js/client.js.

![](https://github.com/tanhengyeow/ctf-journal/tree/master/picoCTF17/Level%202/TW_GR_E1_ART/img/TW_GR_E1_ART.png)

Revealing the flag with id 164, we get `A soft voice on the wind speaks to you: "The secret you are looking for is at_least_the_world_wasnt_destroyed_by_a_meteor_d53e9d9bc6ded1e7cc1f4f60bdf70404. Use it wisely."`

# Learning Outcome

1) Package managers/Dependencies
2) Source code control flow
3) Don't set up your server in a way that it serves the source code. In this case, the problem came from serv.js `app.use(express.static(path.join(__dirname, "..")));` This is telling the server to serve everything in the server's root directory, when in reality, it should only be serving the `public` directory.



