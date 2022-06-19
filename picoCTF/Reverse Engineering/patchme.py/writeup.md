# patchme.py
## Description
Can you get the flag? Run this [Python program](patchme.flag.py) in the same directory as this [encrypted flag](flag.txt.enc).
## Hints
(none)
## Solution
1. Upon inspect of the Python program, comment out the call to ```level_1_pw_check()``` at line 31 and print the flag directly.
```
# level_1_pw_check()
print(str_xor(flag_enc.decode(), "utilitarian"))
```
2. Run the program.
```
% python patchme.flag.py
picoCTF{p47ch1ng_l1f3_h4ck_21d62e33}
```
