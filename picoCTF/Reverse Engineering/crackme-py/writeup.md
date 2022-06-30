# crackme-py
## Description
[crackme.py](crackme.py)
## Hints
(none)
## Solution
1. Open the python program. The string `bezos_cc_secret` is of interest. Modify the program by commenting out line 54 and adding
`decode_secret(bezos_cc_secret)`. Run it.
```python
# choose_greatest()
decode_secret(bezos_cc_secret)
```
```console
% python crackme.py
picoCTF{1|\/|_4_p34|\|ut_dd2c4616}
```
