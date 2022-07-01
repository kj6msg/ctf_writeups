# breadth
## Description
Surely this is what people mean when they say "horizontal scaling," right?  
**TOP SECRET INFO:**  
Our operatives managed to exfiltrate an in-development version of this challenge, where the function with the real flag had a mistake in it. Can you help us get the flag?  
Download [breadth.v2](breadth.v2)  
Download [breadth.v1](breadth.v1)
## Hints
(None)
## Solution
1. Examine the difference between the files. There are two areas of interest, `725` (`0x2D5`) and `610380` (`0x9504C`).
```console
% cmp -bl breadth.v1 breadth.v2
    725 315 ?    103 C
    726 120 P    122 R
    727 141 a    345 ?
    728  57 /    327 ?
    729  61 1    117 O
    730 350 ?    165 u
    731 223 M-^S 237 M-^_
    732 150 h    371 ?
    733  31 ^Y   234 M-^\
    734 163 s    127 W
    735 271 ?      6 ^F
    736 220 M-^P  14 ^L
    737 377 ?     53 +
    738 313 ?    302 ?
    739 307 ?    337 ?
    740 327 ?     47 '
    741 270 ?    121 Q
    742 250 ?    247 ?
    743 361 ?    335 ?
    744 264 ?    251 ?
 610380 124 T    104 D
 610383 270 ?    110 H
 610384  72 :     75 =
 610385 200 M-^@  76 >
 610386  67 7    307 ?
 610387 320 ?     33 ^[
 610388 110 H      4 ^D
 610389  71 9    164 t
 610390 302 ?     12 ^J
 610391 164 t    303 ?
 610392  10 ^H   146 f
 610393 303 ?     17 ^O
 610394  17 ^O    37 ^_
 610395  37 ^_   204 M-^D
 610396 200 M-^@   0 ^@
2438996  61 1     62 2
```
2. Let's take a look in Ghidra. The first address (`0x2D5`) lies in the section `.note.gnu.build-id` and the second address (`0x9504C`) lies in the section `.text`. That second address correlates to function `fcnkKTQpF` at `0x95040`. There's our flag.
```c
void fcnkKTQpF(void)
{
  puts("picoCTF{VnDB2LUf1VFJkdfDJtdYtFlMexPxXS6X}");
  return;
}
```
