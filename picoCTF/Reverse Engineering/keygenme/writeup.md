# keygenme
## Description
Can you get the flag?  
Reverse engineer this [binary](keygenme).
## Hints
(None)
## Solution
1. Open the binary in Ghidra. The binary was stripped, so use the `entry` function to find the `main` function.
```c
void entry(undefined8 param_1,undefined8 param_2,undefined8 param_3)
{
  undefined8 in_stack_00000000;
  undefined auStack8 [8];
  
  __libc_start_main(FUN_0010148b,in_stack_00000000,&stack0x00000008,FUN_00101520,FUN_00101590,
                    param_3,auStack8);
  do {
                    /* WARNING: Do nothing block with infinite loop */
  } while( true );
}
```
```c
undefined8 FUN_0010148b(void)
{
  char cVar1;
  long in_FS_OFFSET;
  char local_38 [40];
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  printf("Enter your license key: ");
  fgets(local_38,0x25,stdin);
  cVar1 = FUN_00101209(local_38);
  if (cVar1 == '\0') {
    puts("That key is invalid.");
  }
  else {
    puts("That key is valid.");
  }
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}
```
2. It seems the function at `0x1209` checks the license key. There are two interesting parts of this function: verifying `param_1` is 36 bytes long and the comparison between `param_1` and `acStack56`. Note the address of the comparison.
```c
undefined8 FUN_00101209(char *param_1)
{
  size_t sVar1;
  undefined8 uVar2;
  long in_FS_OFFSET;
  int local_d0;
  int local_cc;
  int local_c8;
  int local_c4;
  int local_c0;
  undefined2 local_ba;
  byte local_b8 [16];
  byte local_a8 [16];
  undefined8 local_98;
  undefined8 local_90;
  undefined8 local_88;
  undefined4 local_80;
  char local_78 [12];
  undefined local_6c;
  undefined local_66;
  undefined local_5f;
  undefined local_5e;
  char local_58 [32];
  char acStack56 [40];
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  local_98 = 0x7b4654436f636970;
  local_90 = 0x30795f676e317262;
  local_88 = 0x6b5f6e77305f7275;
  local_80 = 0x5f7933;
  local_ba = 0x7d;
  sVar1 = strlen((char *)&local_98);
  MD5((uchar *)&local_98,sVar1,local_b8);
  sVar1 = strlen((char *)&local_ba);
  MD5((uchar *)&local_ba,sVar1,local_a8);
  local_d0 = 0;
  for (local_cc = 0; local_cc < 0x10; local_cc = local_cc + 1) {
    sprintf(local_78 + local_d0,"%02x",(ulong)local_b8[local_cc]);
    local_d0 = local_d0 + 2;
  }
  local_d0 = 0;
  for (local_c8 = 0; local_c8 < 0x10; local_c8 = local_c8 + 1) {
    sprintf(local_58 + local_d0,"%02x",(ulong)local_a8[local_c8]);
    local_d0 = local_d0 + 2;
  }
  for (local_c4 = 0; local_c4 < 0x1b; local_c4 = local_c4 + 1) {
    acStack56[local_c4] = *(char *)((long)&local_98 + (long)local_c4);
  }
  acStack56[27] = local_66;
  acStack56[28] = local_5e;
  acStack56[29] = local_5f;
  acStack56[30] = local_78[0];
  acStack56[31] = local_5e;
  acStack56[32] = local_66;
  acStack56[33] = local_6c;
  acStack56[34] = local_5e;
  acStack56[35] = (undefined)local_ba;
  sVar1 = strlen(param_1);
  if (sVar1 == 0x24) {
    for (local_c0 = 0; local_c0 < 0x24; local_c0 = local_c0 + 1) {
      if (param_1[local_c0] != acStack56[local_c0]) {
        uVar2 = 0;
        goto LAB_00101475;
      }
    }
    uVar2 = 1;
  }
  else {
    uVar2 = 0;
  }
LAB_00101475:
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return uVar2;
}
```
3. Let's take a look in GDB, setting a breakpoint at the comparison (`0x1455`).
```console
% gdb keygenme
(gdb) starti
Starting program: /home/ryan/ctf/keygenme 

Program stopped.
0x00007ffff7fcd050 in _start () from /lib64/ld-linux-x86-64.so.2
(gdb) b *0x555555555455
Breakpoint 1 at 0x555555555455
(gdb) r
The program being debugged has been started already.
Start it from the beginning? (y or n) y
Starting program: /home/ryan/ctf/keygenme 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
Enter your license key: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

Breakpoint 1, 0x0000555555555455 in ?? ()
(gdb) layout asm
```
```assembly
   0x555555555432      mov    eax,DWORD PTR [rbp-0xb8]
   0x555555555438      movsxd rdx,eax
   0x55555555543b      mov    rax,QWORD PTR [rbp-0xd8]
   0x555555555442      add    rax,rdx
   0x555555555445      movzx  edx,BYTE PTR [rax]
   0x555555555448      mov    eax,DWORD PTR [rbp-0xb8]
   0x55555555544e      cdqe
   0x555555555450      movzx  eax,BYTE PTR [rbp+rax*1-0x30]
B+>0x555555555455      cmp    dl,al        
```
4. The comparison is between `[rbp-0xd8]` and `[rbp-0x30]`.
```console
(gdb) x/s $rbp-0xd8
0x7fffffffde28: " \337\377\377\377\177"
(gdb) x/s *(char**)($rbp-0xd8)
0x7fffffffdf20: 'a' <repeats 36 times>
(gdb) x/s $rbp-0x30
0x7fffffffded0: "picoCTF{br1ng_y0ur_0wn_k3y_9d74d90d}\377\177"
```
