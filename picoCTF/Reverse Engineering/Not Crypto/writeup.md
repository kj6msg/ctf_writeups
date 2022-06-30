# not crypto
## Description
there's crypto in here but the challenge is not crypto... 🤔  
Download [not-crypto](not-crypto)
## Hints
(none)
## Solution
1. The program is a position independent executable (PIE) with symbols stripped, making this challenge a little trickier.
```console
% file not-crypto
not-crypto: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=1f838db474ea41305b3181bc0acdc8231273189d, for GNU/Linux 4.4.0, stripped
```
2. Load it in GDB to find the base address and entry point.
```console
% gdb not-crypto
(gdb) starti
Starting program: not-crypto

Program stopped.
(gdb) info proc mappings
process 35325
Mapped address spaces:

          Start Addr           End Addr       Size     Offset objfile
      0x555555554000     0x555555555000     0x1000        0x0 /home/ryan/ctf/not-crypto
      0x555555555000     0x555555556000     0x1000     0x1000 /home/ryan/ctf/not-crypto
      0x555555556000     0x555555557000     0x1000     0x2000 /home/ryan/ctf/not-crypto
      0x555555557000     0x555555559000     0x2000     0x2000 /home/ryan/ctf/not-crypto
      0x7ffff7fc6000     0x7ffff7fca000     0x4000        0x0 [vvar]
      0x7ffff7fca000     0x7ffff7fcc000     0x2000        0x0 [vdso]
      0x7ffff7fcc000     0x7ffff7fcd000     0x1000        0x0 /usr/lib/x86_64-linux-gnu/ld-2.33.so
      0x7ffff7fcd000     0x7ffff7ff1000    0x24000     0x1000 /usr/lib/x86_64-linux-gnu/ld-2.33.so
      0x7ffff7ff1000     0x7ffff7ffb000     0xa000    0x25000 /usr/lib/x86_64-linux-gnu/ld-2.33.so
      0x7ffff7ffb000     0x7ffff7fff000     0x4000    0x2e000 /usr/lib/x86_64-linux-gnu/ld-2.33.so
      0x7ffffffde000     0x7ffffffff000    0x21000        0x0 [stack]
(gdb) info files
Symbols from "/home/ryan/ctf/not-crypto".
Native process:
        Using the running image of child process 35325.
        While running this, GDB does not access memory from...
Local exec file:
        `/home/ryan/ctf/not-crypto', file type elf64-x86-64.
        Entry point: 0x555555555c70
        0x0000555555554318 - 0x0000555555554334 is .interp
        0x0000555555554338 - 0x0000555555554378 is .note.gnu.property
        0x0000555555554378 - 0x000055555555439c is .note.gnu.build-id
        0x000055555555439c - 0x00005555555543bc is .note.ABI-tag
        0x00005555555543c0 - 0x00005555555543dc is .gnu.hash
        0x00005555555543e0 - 0x00005555555544e8 is .dynsym
        0x00005555555544e8 - 0x0000555555554598 is .dynstr
        0x0000555555554598 - 0x00005555555545ae is .gnu.version
        0x00005555555545b0 - 0x00005555555545e0 is .gnu.version_r
        0x00005555555545e0 - 0x00005555555546b8 is .rela.dyn
        0x00005555555546b8 - 0x0000555555554718 is .rela.plt
        0x0000555555555000 - 0x000055555555501b is .init
        0x0000555555555020 - 0x0000555555555070 is .plt
        0x0000555555555070 - 0x0000555555555de5 is .text
        0x0000555555555de8 - 0x0000555555555df5 is .fini
        0x0000555555556000 - 0x0000555555556200 is .rodata
        0x0000555555556200 - 0x0000555555556234 is .eh_frame_hdr
        0x0000555555556238 - 0x0000555555556340 is .eh_frame
        0x0000555555557de0 - 0x0000555555557de8 is .init_array
        0x0000555555557de8 - 0x0000555555557df0 is .fini_array
        0x0000555555557df0 - 0x0000555555557fd0 is .dynamic
        0x0000555555557fd0 - 0x0000555555558000 is .got
        0x0000555555558000 - 0x0000555555558038 is .got.plt
        0x0000555555558038 - 0x0000555555558048 is .data
        0x0000555555558048 - 0x0000555555558050 is .bss
        0x00007ffff7fcc238 - 0x00007ffff7fcc25c is .note.gnu.build-id in /lib64/ld-linux-x86-64.so.2
        0x00007ffff7fcc260 - 0x00007ffff7fcc32c is .hash in /lib64/ld-linux-x86-64.so.2
        0x00007ffff7fcc330 - 0x00007ffff7fcc420 is .gnu.hash in /lib64/ld-linux-x86-64.so.2
        0x00007ffff7fcc420 - 0x00007ffff7fcc720 is .dynsym in /lib64/ld-linux-x86-64.so.2
        0x00007ffff7fcc720 - 0x00007ffff7fcc959 is .dynstr in /lib64/ld-linux-x86-64.so.2
        0x00007ffff7fcc95a - 0x00007ffff7fcc99a is .gnu.version in /lib64/ld-linux-x86-64.so.2
        0x00007ffff7fcc9a0 - 0x00007ffff7fcca44 is .gnu.version_d in /lib64/ld-linux-x86-64.so.2
        0x00007ffff7fcca48 - 0x00007ffff7fccb38 is .rela.dyn in /lib64/ld-linux-x86-64.so.2
--Type <RET> for more, q to quit, c to continue without paging--q
Quit
```
3. Load it in Ghidra and set the base address to `0x555555554000`. Ghidra labeled the entry point `0x555555555c70` as `entry`. The call to `__libc_start_main` shows the `main` function at `0x555555555070`.
```c
void entry(undefined8 param_1,undefined8 param_2,undefined8 param_3)
{
  undefined8 in_stack_00000000;
  undefined auStack8 [8];

  __libc_start_main(FUN_555555555070,in_stack_00000000,&stack0x00000008,FUN_555555555d70,
                    FUN_555555555de0,param_3,auStack8);
  do {
                    /* WARNING: Do nothing block with infinite loop */
  } while( true );
}
```
4. There is a lot going on in `main`, but one part in particular stands out: a memory compare resulting in printing one of two messages.
```c
if (local_48 == local_1e8) {
    iVar24 = memcmp(local_88,local_198,0x40);
    if (iVar24 == 0) {
        puts("Yep, that\'s it!");
    }
    else {
        iVar24 = 1;
        puts("Nope, come back later");
    }
    if (local_40 == *(long *)(in_FS_OFFSET + 0x28)) {
        return iVar24;
    }
              /* WARNING: Subroutine does not return */
    __stack_chk_fail();
}
```
```
5555555553aa 48 8b 74        MOV        RSI,qword ptr [RSP + local_1c8]
             24 40
5555555553af ba 40 00        MOV        EDX,0x40
             00 00
5555555553b4 48 8b 7c        MOV        RDI,qword ptr [RSP + local_1c0]
             24 48
5555555553b9 e8 a2 fc        CALL       <EXTERNAL>::memcmp
             ff ff
```
5. Set a breakpoint at the `memcmp` (`0x5555555553b9`), run the program, and input a 64 byte string. Take a look at `rsi` and `rdi`, since that's what `memcmp` uses.
```console
(gdb) b *0x5555555553b9
Breakpoint 1 at 0x5555555553b9
(gdb) r
The program being debugged has been started already.
Start it from the beginning? (y or n) y
Starting program: /home/ryan/ctf/not-crypto 
I heard you wanted to bargain for a flag... whatcha got?
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

Breakpoint 1, 0x00005555555553b9 in ?? ()
(gdb) x/s $rsi
0x7fffffffddc0: 'a' <repeats 64 times>, "\367l\214\377\\\207/\216\236C\236Ԙ2l\034\325<\020\271\211\273?7\027\370\241\343\217\312\315\377\243\201\006\312*:9\375=\302\230\036\262\bU\341\227}\376\375\275", <incomplete sequence \307>
(gdb) x/s $rdi
0x7fffffffded0: "picoCTF{c0mp1l3r_0pt1m1z4t10n_15_pur3_w1z4rdry_but_n0_pr0bl3m?}\n"
```
