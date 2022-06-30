# speeds and feeds
## Description
There is something on my shop network running at `nc mercury.picoctf.net 7032`, but I can't tell what it is. Can you?
## Hints
1. What language does a CNC machine use?
## Solution
1. Run the program.
```console
% nc mercury.picoctf.net 7032
G17 G21 G40 G90 G64 P0.003 F50
G0Z0.1
G0Z0.1
...
G1X199.3103Y-1.6552
G1X198.7586Y-1.9310
G0Z0.1
```
2. CNC machines use G-code. Copy the output and load it in [NC Viewer](https://ncviewer.com).
```
picoCTF{num3r1cal_c0ntr0l_a067637b}
```
