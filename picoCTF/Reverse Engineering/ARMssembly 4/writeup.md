# ARMssembly 4
## Description
What integer does this program print with argument `3964545182`?  
File: [chall_4.S](chall_4.S)  
Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})
## Hints
1. Switching things up
## Solution
1. The function `func1` is called with a user entered parameter, passed in `w0`.
```arm
func1:
	stp	x29, x30, [sp, -32]!
	add	x29, sp, 0
	str	w0, [x29, 28]
	ldr	w0, [x29, 28]
	cmp	w0, 100
	bls	.L2
	ldr	w0, [x29, 28]
	add	w0, w0, 100
	bl	func2
	b	.L3
.L2:
	ldr	w0, [x29, 28]
	bl	func3
.L3:
	ldp	x29, x30, [sp], 32
	ret
```
```c
int func1(int w0)
{
	int retval;

	if(w0 <= 100)
	{
		retval = func3(w0);
	}
	else
	{
		w0 += 100;
		retval = func2(w0);
	}

	return retval;
}
```
2. There are a lot of branches in this source code. Let's follow the ones that make sense for us. `func2` will be called with `3964545282`.
```arm
func2:
	stp	x29, x30, [sp, -32]!
	add	x29, sp, 0
	str	w0, [x29, 28]
	ldr	w0, [x29, 28]
	cmp	w0, 499
	bhi	.L5
	ldr	w0, [x29, 28]
	sub	w0, w0, #86
	bl	func4
	b	.L6
.L5:
	ldr	w0, [x29, 28]
	add	w0, w0, 13
	bl	func5
.L6:
	ldp	x29, x30, [sp], 32
	ret
```
```c
int func2(int w0)
{
	int retval;

	if(w0 > 499)
	{
		w0 += 13;
		retval = func5(w0);
	}
	else
	{
		w0 -= 86;
		retval = func4(w0);
	}

	return retval;
}
```
3. Deeper we go... `func5` will be called with `3964545295`. All it does is call `func8`.
```arm
func5:
	stp	x29, x30, [sp, -32]!
	add	x29, sp, 0
	str	w0, [x29, 28]
	ldr	w0, [x29, 28]
	bl	func8
	str	w0, [x29, 28]
	ldr	w0, [x29, 28]
	ldp	x29, x30, [sp], 32
	ret
```
4. Last one! `func8` will be called with `3964545295`.
```arm
func8:
	sub	sp, sp, #16
	str	w0, [sp, 12]
	ldr	w0, [sp, 12]
	add	w0, w0, 2
	add	sp, sp, 16
	ret
```
5. The series of function calls will ultimately return `3964545297` (`3964545182 + 100 + 13 + 2`), making the flag `picoCTF{ec4e2911}`
