# ARMssembly 3
## Description
What integer does this program print with argument `3350728462`?  
File: [chall_3.S](chall_3.S)  
Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})
## Hints
1. beep boop beep boop...
## Solution
1. We have two functions of interest now, `func1` and `func2`. Let's start with `func1`. The parameter is passed in `w0`.
```arm
func1:
	stp	x29, x30, [sp, -48]!
	add	x29, sp, 0
	str	w0, [x29, 28]
	str	wzr, [x29, 44]
	b	.L2
.L4:
	ldr	w0, [x29, 28]
	and	w0, w0, 1
	cmp	w0, 0
	beq	.L3
	ldr	w0, [x29, 44]
	bl	func2
	str	w0, [x29, 44]
.L3:
	ldr	w0, [x29, 28]
	lsr	w0, w0, 1
	str	w0, [x29, 28]
.L2:
	ldr	w0, [x29, 28]
	cmp	w0, 0
	bne	.L4
	ldr	w0, [x29, 44]
	ldp	x29, x30, [sp], 48
	ret
```
2. Let's convert it to C.
```c
int func1(int w0)
{
	int sp28 = w0;
	int sp44 = 0;

	while(sp28 > 0)
	{
		if(sp28 & 0x1 == 1)
			sp44 = func2(sp44);
		
		sp28 >>= 1;
	}

	return sp44;
}
```
3. What does `func2` do? The parameter is passed in `w0`.
```arm
func2:
	sub	sp, sp, #16
	str	w0, [sp, 12]
	ldr	w0, [sp, 12]
	add	w0, w0, 3
	add	sp, sp, 16
	ret
```
4. We don't need to convert that to C. It's pretty simple: add 3 to the passed value and return it. Now the flow should be obvious: the program counts the set bits in a number and multiplies that value by three.
```console
% python -c "n = 3 * bin(3350728462).count('1'); print('picoCTF{' + f'{n:08x}' + '}')"
picoCTF{00000030}
```
