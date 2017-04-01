# Challenge

I really need access to website, but I forgot my password and there is no reset. Can you help?

# Walkthrough/Solution

As the name of the challenge suggests, the website is prone to sql injection. Typing a single quote `'` on either fields shows us the format that the sql query of the database is using: </br>

`select * from users where user = '' and pass = '';`

How do we manipulate the fields such that the query will always return true? There are many methods but in this case, I used this method: </br>

`select * from users where user = 'test' and pass = '' OR 1=1 --';`

What I did here was to enter a random username and close the pass field with a single quote `'` and then execute a OR with a statement that is always true `1=1`. Then I comment then the rest of the line with `--`.

This would be what it looks like when you are typing in the fields. </br>

```
username:test
password:' OR 1=1 --

```

And you get the flag! `be_careful_what_you_let_people_ask_1b3db77df6b116a38db8ceb7c81cb14c`

# Learning Outcome

1) Introduction to SQL Injections
