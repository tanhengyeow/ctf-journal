# Challenge

https://brave.dctf-quals-17.def.camp/

# Walkthrough/Solution

Visiting the website shows us a plain `NOP`. Turns out that the website stores a backup file of `index.php` and the source can be viewed by visiting `https://brave.dctf-quals-17.def.camp/index.php~`:

```
<?php

$db  = mysqli_connect('localhost','web_brave','','web_brave');

$id  = @$_GET['id'];
$key = $db->real_escape_string(@$_GET['key']);

if(preg_match('/\s|[\(\)\'"\/\\=&\|1-9]|#|\/\*|into|file|case|group|order|having|limit|and|or|not|null|union|select|from|where|--/i', $id))
    die('Attack Detected. Try harder: '. $_SERVER['REMOTE_ADDR']); // attack detected

$query = "SELECT `id`,`name`,`key` FROM `users` WHERE `id` = $id AND `key` = '".$key."'";
$q = $db->query($query);

if($q->num_rows) {
    echo '<h3>Users:</h3><ul>';
    while($row = $q->fetch_array()) {
        echo '<li>'.$row['name'].'</li>';
    }

    echo '</ul>';
} else {    
    die('<h3>Nop.</h3>');
}
```
On first look, I tried to bypass `real_escape_string` by trying multibyte injection but nothing seemed to be working.  

What's left is to deconstruct what `preg_match` is filtering and finding a way to bypass the filters so that a successful SQL query can be constructed to read the database.

The if statement filtered almost everything that a SQL statement would use except `;`.

Since that is the case, let us use stacked queries to construct our own customized SQL query.

This payload can be used to read the database contents: `https://brave.dctf-quals-17.def.camp/?id=users.id;%00`

1. `users.id` refers to all the values of the id column in the users table, thus it is valid field.
2. `;` would end the first query.
3. `%00` would mark the termination of the second string which would allow us to execute the first query successfully.

This was what the website returned:
```
Users:

Try Harder
DCTF{602dcfeedd3aae23f05cf93d121907ec925bd70c50d78ac839ad48c0a93cfc54}
```
# Learning outcome
1. Stacked queries
