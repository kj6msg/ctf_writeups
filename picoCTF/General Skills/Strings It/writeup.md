# Strings It
## Description
Can you find the flag in [file](strings) without running it?
## Hints
1. [strings](https://linux.die.net/man/1/strings)
## Solution
1. Run ```strings``` on the file.
```
% strings strings | grep picoCTF
picoCTF{5tRIng5_1T_d66c7bb7}
```
