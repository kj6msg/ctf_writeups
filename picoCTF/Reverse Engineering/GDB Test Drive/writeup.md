# GDB Test Drive
## Description
Can you get the flag? Download this [binary](gdbme). Here's the test drive instructions:
* `$ chmod +x gdbme`
* `$ gdb gdbme`
* `(gdb) layout asm`
* `(gdb) break *(main+99)`
* `(gdb) run`
* `(gdb) jump *(main+104)`
## Hints
(none)
## Solution
1. Follow the first three test drive instructions.
```console
% chmod +x gdbme
% gdb gdbme
(gdb) layout asm
```
2. It seems we're bypassing a call to ```sleep``` with the remaining test drive steps.
```
0x55555555532a <main+99>        call   0x555555555110 <sleep@plt>
0x55555555532f <main+104>       lea    rax,[rbp-0x30]
```
3. Execute the remaining test drive instructions.
```
(gdb) break *(main+99)
Breakpoint 1 at 0x132a
(gdb) run
Starting program: /home/ryan/ctf/gdbme

Breakpoint 1, 0x000055555555532a in main ()
(gdb) jump *(main+104)
Continuing at 0x55555555532f.
picoCTF{d3bugg3r_dr1v3_7776d758}
(gdb) ior 1 (process 9046) exited normally]
```
