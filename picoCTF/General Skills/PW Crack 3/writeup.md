# PW Crack 3
## Description
Can you crack the password to get the flag? Download the password checker [here](level3.py) and you'll need the encrypted [flag](level3.flag.txt.enc) and the [hash](level3.hash.bin) in the same directory too. There are 7 potential passwords with 1 being correct. You can find these by examining the password checker script.
## Hints
1. To view the level3.hash.bin file in the webshell, do: ```$ bvi level3.hash.bin```
2. To exit ```bvi``` type ```:q``` and press enter.
3. The ```str_xor``` function does not need to be reverse engineered for this challenge.
## Solution
1. The password is hashed prior to comparison.
```
    user_pw_hash = hash_pw(user_pw)
    
    if( user_pw_hash == correct_pw_hash ):
        print("Welcome back... your flag, user:")
```
2. The list of possible passwords is on line 44. Enter the following code on line 37 before the call to ```level_3_pw_check```.
```
for p in ["6997", "3ac8", "f0ac", "4b17", "ec27", "4e66", "865e"]:
    if hash_pw(p) == correct_pw_hash:
        print("Correct password: " + p)
```
3. Run the modified script.
```
% python level3.py
Correct password: 4b17
Please enter correct password for flag: 4b17
Welcome back... your flag, user:
picoCTF{m45h_fl1ng1ng_2b072a90}
```
