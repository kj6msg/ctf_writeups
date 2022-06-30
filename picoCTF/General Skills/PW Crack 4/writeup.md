# PW Crack 4
## Description
Can you crack the password to get the flag?  
Download the password checker [here](level4.py) and you'll need the encrypted [flag](level4.flag.txt.enc) and the [hash](level4.hash.bin) in the same directory too. There are 100 potential passwords with only 1 being correct. You can find these by examining the password checker script.
## Hints
1. A for loop can help you do many things very quickly.
2. The `str_xor` function does not need to be reverse engineered for this challenge.
## Solution
1. The password is hashed prior to comparison.
```pythong
user_pw_hash = hash_pw(user_pw)

if( user_pw_hash == correct_pw_hash ):
    print("Welcome back... your flag, user:")
```
2. The list of possible passwords is on line 45. Comment out the call to ```level_4_pw_check``` on line 39 and add the following code to the end of the file.
```python
for p in pos_pw_list:
    if hash_pw(p) == correct_pw_hash:
        print("Correct password: " + p)

level_4_pw_check()
```
3. Run the modified script.
```console
% python level4.py
Correct password: eacc
Please enter correct password for flag: eacc
Welcome back... your flag, user:
picoCTF{fl45h_5pr1ng1ng_cf341ff1}
```
