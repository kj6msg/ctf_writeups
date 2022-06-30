# PW Crack 5
## Description
Can you crack the password to get the flag? Download the password checker [here](level5.py) and you'll need the encrypted [flag](level5.flag.txt.enc) and the [hash](level5.hash.bin) in the same directory too. Here's a [dictionary](dictionary.txt) with all possible passwords based on the password conventions we've seen so far.
## Hints
1. Opening a file in Python is crucial to using the provided dictionary.
2. You may need to trim the whitespace from the dictionary word before hashing. Look up the Python string function, `strip`
3. The `str_xor` function does not need to be reverse engineered for this challenge.
## Solution
1. The dictionary is a list of newline separated hexadecimal passwords.
```
% cat dictionary.txt
0000
0001
0002
...
fffd
fffe
ffff
```
2. Read the file and test each password. Enter the following code before the call to `level_5_pw_check`.
```python
def crack_pw():
    with open("dictionary.txt", "r") as file:
        pos_pw = file.read().splitlines()

        for p in pos_pw:
            if hash_pw(p) == correct_pw_hash:
                print("Correct password: " + p)
                return

crack_pw()
```
3. Run the modified script.
```console
% python level5.py
Correct password: 7e5f
Please enter correct password for flag: 7e5f
Welcome back... your flag, user:
picoCTF{h45h_sl1ng1ng_40f26f81}
```
