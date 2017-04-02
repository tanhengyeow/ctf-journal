# Challenge

I really need access to website, but I forgot my password and there is no reset. Can you help? I like lite sql :)

# Walkthrough/Solution

The challenge suggested that it has something to do with Union-Based SQL Injection. Trying to input `'` or `"` in the login page doesn't reveal much information. Are there any other ways you can break the SQL query by not entering single quotes in the username field in the login box? </br>

The most common form of SQL injection is error based, in that you get an error letting you know what's failing and maybe even disclosing parts of the SQL query. Having done so, you would have broken the sql query and find a way to inject into it. </br>

Could it be possible that the sql injection is tied to another part of the system? When we try to register for an account with the username `'` and tried to login afterwards, we broke a SQL query which looks like this: 
```
select id, user, post from posts where user = '';
```
The login system tried to handle a username with a query breaking character in it. With this information, it tells us that the username you register is where you can insert your own malicious SQL. </br>

From the query which selects the id , user, posts from the posts table, it tells us that it is fetching the posts' data when someone logs in. </br>

I tried meddling with SQL injections like this, which showed that I can output data onto the posts page correctly:

```
' OR 1=0 UNION ALL SELECT 1, 1, 1 --
```
Let us think of a way to SQL Inject so that that query selects not only our user's posts, but another user's as well. You can display all other user's post through this SQL injection:
```
' OR user LIKE '%
```
We see that the admin user is the only user with posts in the forum, which is possibly the user that forgotten his/her password. The main purpose of `UNION SELECT` is to select statements from other tables. </br>

Having that in mind, how would you go about to get information about the admin user itself? The challenged hinted `lite sql`. Googling for SQLite Injection Cheatsheets gave us 2 resources, refer to [here](https://github.com/unicornsasfuel/sqlite_sqli_cheat_sheet) and [here](https://www.netsparker.com/blog/web-security/sql-injection-cheat-sheet/). </br>

I viewed the table names in the database by executing this SQL Injection:
```
' OR 1=0 UNION SELECT '1', '2', name FROM sqlite_master WHERE type='table' --
```
Note that when you execute an `UNION SELECT`, the corresponding columns must be the same as the original query statement, in this case, which is 3. </br>

We can see that there are three tables present, posts, sqlite_sequence and users. The users table usually holds account credentials. With this in mind, executing this SQL Injection shows us the credentials for admin:
```
' OR 1=0 UNION SELECT user, * FROM users where user = 'admin' --
```
And the flag is `flag{union?_why_not_onion_a69464d4869c743e26c08df8686e4003}`

# Learning Outcome

1) Identifying fields that are prone to SQL Injection/error messages
2) Introduction to Union-Based SQL Injection
3) Enumerating techniques using SQL injection
