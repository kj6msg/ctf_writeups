# asm4
## Description
What will asm4("picoCTF_a3112") return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](asm4.asm)
## Hints
1. Treat the Array argument as a pointer
## Solution
1. Sometimes it's easier to just run the code itself... I converted it to NASM syntax.
```assembly
SECTION .data
    param0 db "picoCTF_a3112"
    len equ $-param0

SECTION .text
    global _start
_start:
    push   param0
    call   asm4
    add    esp, 4

    mov    eax, 1
    mov    ebx, 0
    int    0x80

asm4:
    push   ebp
    mov    ebp, esp

    push   ebx
    sub    esp, 0x10

    mov    [ebp-0x10], DWORD 0x246
    mov    [ebp-0xc], DWORD 0x0
    jmp    L27

L23:
    add    [ebp-0xc], DWORD 0x1

L27:
    mov    edx, [ebp-0xc]
    mov    eax, [ebp+0x8]
    add    eax, edx
    movzx  eax, BYTE [eax]
    test   al, al
    jne    L23

    mov    [ebp-0x8], DWORD 0x1
    jmp    L138

L51:
    mov    edx, [ebp-0x8]
    mov    eax, [ebp+0x8]
    add    eax,edx
    movzx  eax, BYTE [eax]
    movsx  edx, al
    mov    eax, [ebp-0x8]
    lea    ecx, [eax-0x1]
    mov    eax, [ebp+0x8]
    add    eax, ecx
    movzx  eax, BYTE [eax]
    movsx  eax, al
    sub    edx, eax
    mov    eax, edx
    mov    edx, eax
    mov    eax, [ebp-0x10]
    lea    ebx, [edx+eax*1]
    mov    eax, [ebp-0x8]
    lea    edx, [eax+0x1]
    mov    eax, [ebp+0x8]
    add    eax, edx
    movzx  eax, BYTE [eax]
    movsx  edx, al
    mov    ecx, [ebp-0x8]
    mov    eax, [ebp+0x8]
    add    eax, ecx
    movzx  eax, BYTE [eax]
    movsx  eax, al
    sub    edx, eax
    mov    eax, edx
    add    eax, ebx
    mov    [ebp-0x10], eax
    add    [ebp-0x8], DWORD 0x1

L138:
    mov    eax, [ebp-0xc]
    sub    eax, 0x1
    cmp    [ebp-0x8],eax
    jl     L51
    
    mov    eax, [ebp-0x10]

    add    esp, 0x10
    pop    ebx

    pop    ebp
    ret
```
```console
% nasm -f elf32 -o asm4.o asm4.asm
% ld -m elf_i386 -o asm4 asm4.o
% gdb asm4
(gdb) layout asm
(gdb) disass _start
(gdb) b *(_start+10)
(gdb) r
(gdb) p/x $eax
Starting program: /home/ryan/ctf/asm4

Breakpoint 1, 0x0804900a in _start ()
(gdb) p/x $eax
$1 = 0x1d0
```
2. The flag is `0x1d0`
