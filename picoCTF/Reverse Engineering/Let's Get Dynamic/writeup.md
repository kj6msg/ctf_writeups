# Let's Get Dynamic
## Description
Can you tell what this file is reading? [chall.S](chall.S)
## Hints
1. Running this in a debugger would be helpful
## Solution
1. Assemble and run it.
```console
% gcc -o chall chall.S
% ./chall
Hello
Correct! You entered the flag.
```
2. Interesting. It waits for input, but it doesn't make sense. Time for the debugger.
```console
% gdb chall
(gdb) layout asm
(gdb) b *main
```
3. Scrolling through the program, the call to `memcmp` looks interesting.
```
	0x5555555552ef <main+374>       mov    edx,0x31
	0x5555555552f4 <main+379>       mov    rsi,rcx
	0x5555555552f7 <main+382>       mov    rdi,rax
	0x5555555552fa <main+385>       call   0x555555555060 <memcmp@plt>
(gdb) b *(main+385)
(gdb) r
Starting program: /home/ryan/ctf/chall

Breakpoint 1, 0x0000555555555179 in main ()
(gdb) c
Continuing.
Hello
Breakpoint 2, 0x00005555555552fa in main ()
```
4. What are we comparing? Let's look at `rsi` and `rdi`.
```
(gdb) x/8bx $rsi
0x7fffffffde50: 0x70    0x69    0x63    0x6f    0x43    0x54    0x46    0x7b
(gdb) x/s $rsi
0x7fffffffde50: "picoCTF{dyn4m1c_4n4ly1s_1s_5up3r_us3ful_56e35b54}\200"
```
