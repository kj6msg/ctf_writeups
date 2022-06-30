# keygenme-py
## Description
[keygenme-trial.py](keygenme-trial.py)
## Hints
(none)
## Solution
1. Open the python program. The license key is `picoCTF{1n_7h3_|<3y_of_xxxxxxxx}`. We need to figure out the `xxxxxxxx` part.
2. Inspect the `check_key` function. The `xxxxxxxx` portion of the flag is compared to an encoded version of `username_trial` (`"PRITCHARD"`).
```python
if key[i] != hashlib.sha256(username_trial).hexdigest()[4]:
    return False
else:
    i += 1

if key[i] != hashlib.sha256(username_trial).hexdigest()[5]:
    return False
else:
    i += 1

if key[i] != hashlib.sha256(username_trial).hexdigest()[3]:
    return False
else:
    i += 1

if key[i] != hashlib.sha256(username_trial).hexdigest()[6]:
    return False
else:
    i += 1

if key[i] != hashlib.sha256(username_trial).hexdigest()[2]:
    return False
else:
    i += 1

if key[i] != hashlib.sha256(username_trial).hexdigest()[7]:
    return False
else:
    i += 1

if key[i] != hashlib.sha256(username_trial).hexdigest()[1]:
    return False
else:
    i += 1

if key[i] != hashlib.sha256(username_trial).hexdigest()[8]:
    return False

return True
```
3. Decoding is easily performed with a simple script.
```python
import hashlib

username_trial = b"PRITCHARD"
indices = [4, 5, 3, 6, 2, 7, 1, 8]

enc = "".join(hashlib.sha256(username_trial).hexdigest()[i] for i in indices)

print("picoCTF{1n_7h3_|<3y_of_" + enc + "}")
```
```console
% python flag.py
picoCTF{1n_7h3_|<3y_of_54ef6292}
```
