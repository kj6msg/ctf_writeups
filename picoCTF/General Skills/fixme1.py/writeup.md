# fixme1.py
## Description
Fix the syntax error in this Python script to print the flag. [Download Python script](fixme1.py)
## Hints
1. Indentation is very meaningful in Python
2. To view the file in the webshell, do: `$ nano fixme1.py`
3. To exit `nano`, press Ctrl and x and follow the on-screen prompts.
4. The `str_xor` function does not need to be reverse engineered for this challenge.
## Solution
1. You can see the erroneous indentation at line 20 (`print` statement).
```python
flag = str_xor(flag_enc, 'enkidu')
  print('That is correct! Here\'s your flag: ' + flag)
```
2. Fix the indendation and run the script.
```console
% python fixme1.py
That is correct! Here's your flag: picoCTF{1nd3nt1ty_cr1515_182342f7}
```
