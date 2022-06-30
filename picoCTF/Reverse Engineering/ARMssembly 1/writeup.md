# ARMssembly 1
## Description
For what argument does this program print 'win' with variables `85`, `6` and `3`?  
File: [chall_1.S](chall_1.S)  
Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})
## Hints
1. Shifts
## Solution
1. Let's take a look at function `func`. The parameter is passed in `w0`.
```arm
func:
	sub	sp, sp, #32
	str	w0, [sp, 12]
	mov	w0, 85
	str	w0, [sp, 16]
	mov	w0, 6
	str	w0, [sp, 20]
	mov	w0, 3
	str	w0, [sp, 24]
	ldr	w0, [sp, 20]
	ldr	w1, [sp, 16]
	lsl	w0, w1, w0
	str	w0, [sp, 28]
	ldr	w1, [sp, 28]
	ldr	w0, [sp, 24]
	sdiv	w0, w1, w0
	str	w0, [sp, 28]
	ldr	w1, [sp, 28]
	ldr	w0, [sp, 12]
	sub	w0, w1, w0
	str	w0, [sp, 28]
	ldr	w0, [sp, 28]
	add	sp, sp, 32
	ret
```
2. Let's rewrite it in C.
```c
int func(int w0)
{
	int sp12 = w0;
	int sp16 = 85;
	int sp20 = 6;
	int sp24 = 3;

	int sp28 = sp16 << sp20;
	sp28 /= sp24;
	sp28 -= sp12;
	
	return sp28;
}
```
3. The code breaks down easily into a simple math expression. Let's rewrite it.
```c
int func(int w0)
{
	return (85 << 6) / 3) - w0;
}
```
4. Calling the function as `func(1813)` returns 0, which will print `You win!`. Convert to hex for the flag: `picoCTF{00000715}`
