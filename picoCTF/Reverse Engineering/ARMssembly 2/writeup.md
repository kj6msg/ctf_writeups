# ARMssembly 2
## Description
What integer does this program print with argument ```3848786505```?\
File: [chall_2.S](chall_2.S)\
Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})
## Hints
1. Loops
## Solution
1. Look at ```func1```.
```
func1:
	sub	sp, sp, #32
	str	w0, [sp, 12]
	str	wzr, [sp, 24]
	str	wzr, [sp, 28]
	b	.L2
.L3:
	ldr	w0, [sp, 24]
	add	w0, w0, 3
	str	w0, [sp, 24]
	ldr	w0, [sp, 28]
	add	w0, w0, 1
	str	w0, [sp, 28]
.L2:
	ldr	w1, [sp, 28]
	ldr	w0, [sp, 12]
	cmp	w1, w0
	bcc	.L3
	ldr	w0, [sp, 24]
	add	sp, sp, 32
	ret
```
2. Breaking it down to pseudo-code makes the logic clearer.
```
int func(int param0)
	int retval = 0

	for(int i = 0; i < param0; ++i)
		retval += 3;

	return retval
```
3. The function arithmetically multiplies the input by three. Calling it with ```3848786505``` yields ```11546359515```, which is larger than a 32-bit register can hold. Mask the result with 0xFFFFFFFF and we have the flag. Python interpreter code is below.
```
>>> print("picoCTF{" + hex((3 * 3848786505) & 0xffffffff) + "}")
picoCTF{0xb03776db}
```
