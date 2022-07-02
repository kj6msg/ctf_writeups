# asm3
## Description
What does asm3(0xd73346ed,0xd48672ae,0xd3c8b139) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](test.S)
## Hints
1. more(?) [registers](https://wiki.skullsecurity.org/index.php?title=Registers)
## Solution
1. Let's take a look.
```
asm3:
	<+0>:	push   ebp
	<+1>:	mov    ebp,esp
	<+3>:	xor    eax,eax
	<+5>:	mov    ah,BYTE PTR [ebp+0xa]
	<+8>:	shl    ax,0x10
	<+12>:	sub    al,BYTE PTR [ebp+0xc]
	<+15>:	add    ah,BYTE PTR [ebp+0xd]
	<+18>:	xor    ax,WORD PTR [ebp+0x10]
	<+22>:	nop
	<+23>:	pop    ebp
	<+24>:	ret 
```
2. This is 32 bit code, so the first parameter is at `[ebp+0x8]`, the second at `[ebp+0xc]`, and the third at `[ebp+0x10]`. We are extracting bytes (8 bits) and words (16 bits) from the parameters for 8 and 16 bit operations. The instructions up to and including the `shl` at `<asm3+8>` can be ignored. It effectively leaves `eax` as `0`.
```
<+3>:	xor    eax,eax
<+5>:	mov    ah,BYTE PTR [ebp+0xa]
<+8>:	shl    ax,0x10
```
3. The next two instructors load `al` with `-0xae` and `ah` with `0x72`. Since `0xae` is already a negative number (2's compliment... MSb is set), we reverse that and that makes `ax` equal to `0x7252`.
```
<+12>:	sub    al,BYTE PTR [ebp+0xc]
<+15>:	add    ah,BYTE PTR [ebp+0xd]
```
4. Now we just XOR `ax` (`0x7252`) with the least significant word of parameter 3 (`0xb139`), and the flag is `0xc36b`
```
<+18>:	xor    ax,WORD PTR [ebp+0x10]
```
