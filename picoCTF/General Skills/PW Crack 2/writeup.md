# PW Crack 2
## Description
Can you crack the password to get the flag? Download the password checker [here](level2.py) and you'll need the encrypted [flag](level2.flag.txt.enc) in the same directory too.
## Hints
1. Does that encoding look familiar?
2. The ```str_xor``` function does not need to be reverse engineered for this challenge.
## Solution
1. The password is visible on line 18 of the password checker.
```
    if( user_pw == chr(0x33) + chr(0x39) + chr(0x63) + chr(0x65) ):
        print("Welcome back... your flag, user:")
```
2. Print the valid password and run the script.
```
% python -c "print(chr(0x33) + chr(0x39) + chr(0x63) + chr(0x65))"
39ce
% python level2.py
Please enter correct password for flag: 39ce
Welcome back... your flag, user:
picoCTF{tr45h_51ng1ng_502ec42e}
```
