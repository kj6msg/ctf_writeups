# Glitch Cat
## Description
Our flag printing service has started glitching! ```$ nc saturn.picoctf.net 51109```
## Hints
1. ASCII is one of the most common encodings used in programming
2. We know that the glitch output is valid Python, somehow!
3. Press Ctrl and c on your keyboard to close your connection and return to the command prompt.
## Solution
1. Connect to the server.
```
% nc saturn.picoctf.net 51109
'picoCTF{gl17ch_m3_n07_' + chr(0x62) + chr(0x64) + chr(0x61) + chr(0x36) + chr(0x38) + chr(0x66) + chr(0x37) + chr(0x35) + '}'
```
2. Definitely a python string. Print it.
```
% python -c "print('picoCTF{gl17ch_m3_n07_' + chr(0x62) + chr(0x64) + chr(0x61) + chr(0x36) + chr(0x38) + chr(0x66) + chr(0x37) + chr(0x35) + '}')"
picoCTF{gl17ch_m3_n07_bda68f75}
```
