# Challenge

Someone got hacked! Check out some service's password hashes that were leaked at hashdump.txt! Do you think they chose strong passwords? We should check... The service is running at shell2017.picoctf.com:44804!

# Walkthrough/Solution

There are lots of resources available online that contain cracked hashes. In this case, I used this [service](https://crackstation.net/). However, they only accept a specific hash format and accepts at most 20 hashes at one go. Doing this in your vim editor containing the data of hashdumps.txt helps to clear off the excess format that is not required, `:%s/.\{-}:`. </br>

Thankfully the first 20 hashes contain some hashes that were already cracked. Using the credentials to login after connecting to the port, we can access the access the cat ascii art database.

```

     /\_/\ 
    ( o o )
  G-==_Y_==-M
      `-'
      
  /\ /\ 
  (O o)
=(: ^ :)=  
  '*v*'
  
 |\_/|     
 (. .)
  =w= (\   
 / ^ \//   
(|| ||)
,""_""_ .

     /\_/\ 
    ( o o )
   -==_Y_==- 
      `-'
    /\**/\ 
   ( o_o  )_)
   ,(u  u  ,),
  {}{}{}{}{}{}
  
  /\_/\ 
 ( o.o )
  > ^ <
  
       /\_/\ 
  /\  / o o \ 
 //\ \~(*)~/
 `  \/   ^ /
    | \|| ||  
    \ '|| ||  
     \)()-())
     
   A_A
  (-.-)
   |-|   
  /   \  
 |     |  __
 |  || | |  \___
 \_||_/_/
 
     /\__/\ 
    /`    '\ 
  === 0  0 ===
    \  --  /    - flag is 3977df525282eaf0e99f86efd2b645ed

   /        \ 
  /          \ 
 |            |
  \  ||  ||  /
   \_oo__oo_/#######o
   
  /\___/\ 
 ( o   o )
 (  =^=  ) 
 (        )
 (         )
 (          )))))))))))
 
 /\ /\ 
 (O o)
=(:^:)=  
   U
   
    _,,/|
    \o o' 
    =_~_=
    /   \ (\ 
   (////_)//
   ~~~
   
   /\     /\ 
  {  `---'  }
  {  O   O  }  
~~|~   V   ~|~~  
   \  \|/  /   
    `-----'__
    /     \  `^\_
   {       }\ |\_\_   W
   |  \_/  |/ /  \_\_( )
    \__/  /(_E     \__/
      (  /
       MM
       
              ("`-''-/").___..--''"`-._
               `6_ 6  )   `-.  (     ).`-.__.`)
               (_Y_.)'  ._   )  `._ `. ``-..-'
             _..`--'_..-_/  /--'_.' ,'
           (il),-''  (li),'  ((!.-'
           
from http://user.xmission.com/~emailbox/ascii_cats.htm

```

# Learning Outcome

1) Password hashes



 
