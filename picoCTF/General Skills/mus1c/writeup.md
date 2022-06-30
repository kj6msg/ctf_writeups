# mus1c
## Description
I wrote you a [song](lyrics.txt). Put it in the picoCTF{} flag format.
## Hints
1. Do you think you can master rockstar?
## Solution
1. The song lyrics are actually Rockstar code. Enter it in a [decoder](https://codewithrockstar.com/online).
```
114
114
114
111
99
107
110
114
110
48
49
49
51
114
Program completed in 95 ms
```
2. Looks like decimal ASCII. Convert it with [CyberChef](https://gchq.github.io/CyberChef/).
```
rrrocknrn0113r
```
3. The flag is `picoCTF{rrrocknrn0113r}`.
