# keygenme-py
## Description
[keygenme-trial.py](keygenme-trial.py)
## Hints
(none)
## Solution
1. Open the python program. The license key is the flag
```picoCTF{1n_7h3_|<3y_of_xxxxxxxx}```.
2. Inspect the ```check_key``` function. The ```xxxxxxxx``` portion of the flag
is compared to an encoded version of the ```username_trial``` string
```"PRITCHARD"```.
```
if key[i] != hashlib.sha256(username_trial).hexdigest()[4]:
    return False
else:
    i += 1
```
3. Decoding is easily performed with a simple [script](flag.py).
```
import hashlib

username_trial = b"PRITCHARD"
indices = [4, 5, 3, 6, 2, 7, 1, 8]

enc = "".join(hashlib.sha256(username_trial).hexdigest()[i] for i in indices)

print("picoCTF{1n_7h3_|<3y_of_" + enc + "}")
```
4. Run the script and get the flag.
```
% python flag.py
picoCTF{1n_7h3_|<3y_of_54ef6292}
```
