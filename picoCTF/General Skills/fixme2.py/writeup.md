# fixme2.py
## Description
Fix the syntax error in the Python script to print the flag. [Download Python script](fixme2.py)
## Hints
1. Are equality and assignment the same symbol?
2. To view the file in the webshell, do: `$ nano fixme2.py`
3. To exit `nano`, press Ctrl and x and follow the on-screen prompts.
4. The `str_xor` function does not need to be reverse engineered for this challenge.
## Solution
1. The erroneous assignment operator (`=`) is at line 22 (`if` statement).
```python
if flag = "":
  print('String XOR encountered a problem, quitting.')
```
2. Change it to an equality operator (`==`) and run the script.
```console
% python fixme2.py
That is correct! Here's your flag: picoCTF{3qu4l1ty_n0t_4551gnm3nt_e8814d03}
```
