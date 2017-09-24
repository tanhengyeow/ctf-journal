# Challenge

http://163.172.176.29/OPENCHALLENGE/open-challenge.html

# Walkthrough/Solution

Viewing the source code showed us three interesting stuff:
1. A script containing JSFuck.
2. Author's hint: `<!-- Hey, you looked into the source for comments! As a bonus for doing so, f0xtr0t grants you this link: https://www.youtube.com/watch?v=-tJYN-eG1zk -->` (Will come in handy later)
3. A hidden element of password type

Deobfuscating the JSFuck gives us:
```
$(function() {
    $("#z-form").submit(function(t) {
        t.preventDefault();
        var a = $("#z-password").val(),
            e = "8e15ad6e5f26fe0585707dc97ce967c6ffaac0cacd2037c4c6c63a503ceea1e6U2FsdGVkX1+yNXzSLU+2HUI7GTRvpl9BdTD1OPX5iMZgHlYay52uv5t/UEHRkeKLJyFjgCoV2nxfL17HPAz8e3bQy0tm0VtorCHXuW/IauNEynVQygPQzaob/1eRihkfYf1XW59GQscAf9uDz93Dub7qiIn5WMIH6hzkM1yDbDBXb6U4GdZQWYsqoFStfyBGaQ04DnnrN3qU/kSs3ciVGmWyW3vuPSHw26VwmINr1jF16DKGK8YWBExVgu9zhiNBaxyQIuWs2SX2BVHokVBOKg==",
            r = e.substring(0, 64),
            c = e.substring(64); 
        if (CryptoJS.HmacSHA256(c, CryptoJS.SHA256(a)).toString() === r) {
            var n = CryptoJS.AES.decrypt(c, a).toString(CryptoJS.enc.Utf8);
            document.write("<html><body><h1>Congratulations!</h1><h2>If you've been following along closely, you should have found the flag by now :P</h2></body></html>")
        } else alert("Haha, try again!")
    })
});
```

r evaluates to `8e15ad6e5f26fe0585707dc97ce967c6ffaac0cacd2037c4c6c63a503ceea1e6` </br>
and c evaluates to `U2FsdGVkX1+yNXzSLU+2HUI7GTRvpl9BdTD1OPX5iMZgHlYay52uv5t/UEHRkeKLJyFjgCoV2nxfL17HPAz8e3bQy0tm0VtorCHXuW/IauNEynVQygPQzaob/1eRihkfYf1XW59GQscAf9uDz93Dub7qiIn5WMIH6hzkM1yDbDBXb6U4GdZQWYsqoFStfyBGaQ04DnnrN3qU/kSs3ciVGmWyW3vuPSHw26VwmINr1jF16DKGK8YWBExVgu9zhiNBaxyQIuWs2SX2BVHokVBOKg==`

It seems that we have to find the correct password so that `CryptoJS.HmacSHA256(c, CryptoJS.SHA256(a)).toString()` evaluates to r.

Seems like a pain to bruteforce the password given the number of permutations. But wait, what about the author's hint that we discovered earlier? It is a youtube link to Queen - We Will Rock You's official video.

With that in mind, I wrote a nodejs script to solve this challenge:
```
e = "8e15ad6e5f26fe0585707dc97ce967c6ffaac0cacd2037c4c6c63a503ceea1e6U2FsdGVkX1+yNXzSLU+2HUI7GTRvpl9BdTD1OPX5iMZgHlYay52uv5t/UEHRkeKLJyFjgCoV2nxfL17HPAz8e3bQy0tm0VtorCHXuW/IauNEynVQygPQzaob/1eRihkfYf1XW59GQscAf9uDz93Dub7qiIn5WMIH6hzkM1yDbDBXb6U4GdZQWYsqoFStfyBGaQ04DnnrN3qU/kSs3ciVGmWyW3vuPSHw26VwmINr1jF16DKGK8YWBExVgu9zhiNBaxyQIuWs2SX2BVHokVBOKg==";

r = e.substring(0,64);
c = e.substring(64);
a = "";

function brute(a) {
    var CryptoJS = require("crypto-js");
    if (CryptoJS.HmacSHA256(c, CryptoJS.SHA256(a)).toString() === r) {
        var n = CryptoJS.AES.decrypt(c, a).toString(CryptoJS.enc.Utf8);
        console.log(n);
        process.exit();
    }
}

// Thanks to https://stackoverflow.com/questions/6156501/read-a-file-one-line-at-a-time-in-node-js
var lineReader = require('readline').createInterface({
  input: require('fs').createReadStream('rockyou.txt')
});

lineReader.on('line', function (line) {
    //console.log(line);
    brute(line);
});
```

# Learning outcome
1. JSFuck/Deobfuscating JSFuck
2. Javascript functions/NodeJS scripting
