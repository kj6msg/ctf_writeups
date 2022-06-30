# ARMssembly 2
## Description
What integer does this program print with argument `3848786505`?  
File: [chall_2.S](chall_2.S)  
Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})
## Hints
1. Loops
## Solution
1. Look take a look at the function `func1`. The parameter is passed in `w0`.
```arm
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
2. Converting it to C makes the logic clearer: it's a loop that multiplies the input parameter by three through addition.
```c
int func1(int w0)
{
	int sp12 = w0;
	int sp24 = 0;
	int sp28 = 0;

	while(sp28 < sp12)
	{
		sp24 += 3;
		++sp28;
	}
}
```
3. Let's simplify the above C code.
```c
int func1(int w0)
{
	int retval = 0;

	for(int i = 0; i < w0; ++i)
		retval += 3;

	return retval;
}
```
4. Calling `func1(3848786505)` returns `11546359515` (`0x2B03776DB`), however that's larger than a 32-bit register can hold (`0xFFFFFFFF`). Mask the result with 0xFFFFFFFF and we have the flag: `picoCTF{0xb03776db}`
