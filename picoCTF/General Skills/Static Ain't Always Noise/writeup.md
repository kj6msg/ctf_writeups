# Static ain't always noise...
## Description
Can you look at the data in this binary: [static](static)? This [BASH script](ltdis.sh) might help!
## Hints
(none)
## Solution 1
1. Check the file type of the binary.
```
% file static
static: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically
linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0,
BuildID[sha1]=33934f7b8aea8e359749ed57dca4cd26d6059acf, not stripped
```
2. Dump the strings contained in the binary.
```
% strings static
/lib64/ld-linux-x86-64.so.2
libc.so.6
puts
...
picoCTF{d15a5m_t34s3r_1e6a7731}
...
.data
.bss
.comment
```
## Solution 2
1. Run the BASH script.
```
% chmod +x ltdis.sh
% ./ltdis.sh
Attempting disassembly of  ...
/Library/Developer/CommandLineTools/usr/bin/objdump: error: 'a.out': No such file or directory
Disassembly failed!
Usage: ltdis.sh <program-file>
Bye!
% ./ltdis.sh static
Attempting disassembly of static ...
Disassembly successful! Available at: static.ltdis.x86_64.txt
Ripping strings from binary with file offsets...
Any strings found in static have been written to static.ltdis.strings.txt with file offset
```
2. View ```static.ltdis.strings.txt```.
```
% cat static.ltdis.strings.txt
238 /lib64/ld-linux-x86-64.so.2
361 libc.so.6
36b puts
...
1020 picoCTF{d15a5m_t34s3r_1e6a7731}
...
1963 .data
1969 .bss
196e .comment
```
