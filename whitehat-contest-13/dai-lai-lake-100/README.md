# Challenge  
Can you find my sensitive infomation? </br></br> Dai Lai has acquired a reputation for the land of graceful mountains and debonair water. </br></br>
Download file:
http://material.wargame.whitehat.vn/contests/13/passcode.zip

# Walkthrough/Solution
Upon extracting the contents of the zip file, we are presented with a file name `passcode.apk`. Using apktool with the below command, I managed to unpack the files from the APK:
```
apktool d passcode.apk -o output
```
Looking through the files in the `output` folder, I began to analyze the file `passcode.sqlite`. Using `sqlitebrowser` to open the .sqlite file, there were 3 tables present. The table `zadminz` seemed interesting and I proceeded to execute the following SQL statement under the `Execute SQL` tab:
```
SELECT * from zadminz
```
The result returned an interesting email named `admin_contest_05@spamdecoy.net`. Visiting http://spamdecoy.net with the email, I saw an email subject named `PASSCODE`. The contents of the email presented "Your new PASSCODE is: check_your_db_before_building_app". Converting the string to SHA1 gives us the flag `WhiteHat{254eb81a7b439405a5d006eb7cfdf0cd841c6d28}`
