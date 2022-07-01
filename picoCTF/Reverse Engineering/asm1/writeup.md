# asm1
## Description
What does `asm1(0x2e0)` return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](test.S)
## Hints
1. assembly [conditions](https://www.tutorialspoint.com/assembly_programming/assembly_conditions.htm)
## Solution
1. Step through the function. The first comparison starts at `<asm1+3>` and `0x280` is stored in `[ebp+0x8]`. Is `0x2e0` greater than `0x3fb`? Nope, continue.
```
<+3>:	cmp    DWORD PTR [ebp+0x8],0x3fb
<+10>:	jg     0x512 <asm1+37>
```
2. Is `0x2e0` equal to `0x280`? Nope, jump.
```
<+12>:	cmp    DWORD PTR [ebp+0x8],0x280
<+19>:	jne    0x50a <asm1+29>
```
3. Compute `0x2e0 - 0xa` and jump.
```
<+29>:	mov    eax,DWORD PTR [ebp+0x8]
<+32>:	sub    eax,0xa
<+35>:	jmp    0x529 <asm1+60>
```
4. Done. The function returns `0x2d6`.
```
<+60>:	pop    ebp
<+61>:	ret
```
