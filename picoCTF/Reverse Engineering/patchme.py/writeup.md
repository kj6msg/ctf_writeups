# patchme.py
## Description
Can you get the flag? Run this [Python program](patchme.flag.py) in the same directory as this [encrypted flag](flag.txt.enc).
## Hints
(none)
## Solution
1. Comment out the call to `level_1_pw_check()` at line 31 and print the flag directly.
```python
# level_1_pw_check()
print(str_xor(flag_enc.decode(), "utilitarian"))
```
```console
% python patchme.flag.py
picoCTF{p47ch1ng_l1f3_h4ck_21d62e33}
```
