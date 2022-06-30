# PW Crack 1
## Description
Can you crack the password to get the flag? Download the password checker [here](level1.py) and you'll need the encrypted [flag](level1.flag.txt.enc) in the same directory too.
## Hints
1. To view the file in the webshell, do: `$ nano level1.py`
2. To exit `nano`, press Ctrl and x and follow the on-screen prompts.
3. The `str_xor` function does not need to be reverse engineered for this challenge.
## Solution
1. The password is visible on line 19 of the password checker.
```python
if( user_pw == "1e1a"):
    print("Welcome back... your flag, user:")
```
2. Run the script and enter the password.
```console
% python level1.py
Please enter correct password for flag: 1e1a
Welcome back... your flag, user:
picoCTF{545h_r1ng1ng_fa343060}
```
