# Challenge 

Given the relative success of the first release, it was no surprise that a second installment in the TW:GR series was released. I can't beat this one either, though... those darn spatulas put an induction cooktop in the floor so I can't get to the flag! Can you get it for me? You can play the game here.

# Walkthrough/Solution

Playing the previous challenge is important because that way you would have read through most of the source code made available. In this challenge, we can't get past the induction cooktop but the spatula can. This hinted us to look at the behavior of spatula, so I looked into server/ai.js </br>

Observing the movement of spatula and looking at the code snippet, spatula always tries to be in the row or column as toaster, no matter how far apart we are. 

```
function measureDist(a, b) {
	var r = Math.abs(a.r - b.r);
	var c = Math.abs(a.c - b.c);

	var m = Math.min(r, c);
	var d = Math.max(r, c);

	return d + m / 20;
```
This was why spatula moved onto of the cooktop when I moved diagonally up/left which is the empty space 5 spots above the cooktop. 

Also, this snippet proved to be interesting:

```

	// If the player is nearby (at most 3 steps) or is in the same room, move toward them
	if (curDist <= 3 || (playerRoom > 0 && playerRoom == entityRoom)) {
		var bestDist = curDist;
		var bestDir = 0;

		for (var i = 0; i < 8; i++) {
			if (validMove(state, entity, { type: "move", direction: i })) {
				var dir = utils.decodeDirection(i);
				var newDist = measureDist(state.player.location, { r: entity.location.r + dir[0], c: entity.location.c + dir[1] });
				if (newDist < bestDist) {
					bestDist = newDist;
					bestDir = i;
				}
			}
		}

		entity.lastMoveDir = bestDir;
		return { type: "move", direction: bestDir };
	}
  ```
Since spatula is on the stove now, I want to force it to move towards the flag, but how do I do that? Although it kept following me and replicated towards the direction where I go, I can't seem to force it to move right such that it can enter the top right portion of the maze. </br>

When we look at the beginning of the code snippet, `bestDist` is set to `curDist`, `bestDir` is set to 0. What if there are no positions where spatula could move to is closer? The values of these two variables would not change, causing spatula to move in direction 0. </br>

In server/util.js, notice the function:

```
function decodeDirection(dir){
	switch(dir){
		case 0:
			return [0, 1];
			break;
		case 1:
			return [-1, 1];
			break;
		case 2:
			return [-1, 0];
			break;
		case 3:
			return [-1, -1];
			break;
		case 4:
			return [0, -1];
			break;
		case 5:
			return [1, -1];
			break;
		case 6:
			return [1, 0];
			break;
		case 7:
			return [1, 1];
			break;
		default:
			return null;
			break;
	}
}
```
Case 0 seemed to cause spatula to move right, case 1 bottom right, case 2 bottom and so on. Spatula moving in direction 0 is what we want. Therefore, luring spatula to the spot where you want it to move right and then using a skill like `calm mind`, you can force spatula to move right. After that, if you move up or down, you will be at a distance of greater than 3 from the spatula, so it will continue following the corridor and grab the flag. From there, you can lure it out and kill it to get the flag.

![](https://github.com/tanhengyeow/ctf-journal/blob/master/picoCTF17/Level%202/TW_GR_E2_EoTDS/img/TW_GR_E2_EoTDS.png)

# Learning Outcome
1) Pay extra attention to edge cases!
 
