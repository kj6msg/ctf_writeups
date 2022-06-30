# ARMssembly 0
## Description
What integer does this program print with arguments `1765227561` and `1830628817`?  
File: [chall.S](chall.S)  
Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})
## Hints
1. Simple compare
## Solution
1. Let's take a look at the function `func1`. The first parameter is passed in `w0` and the second in `w1`.
```arm
func1:
	sub	sp, sp, #16
	str	w0, [sp, 12]
	str	w1, [sp, 8]
	ldr	w1, [sp, 12]
	ldr	w0, [sp, 8]
	cmp	w1, w0
	bls	.L2
	ldr	w0, [sp, 12]
	b	.L3
.L2:
	ldr	w0, [sp, 8]
.L3:
	add	sp, sp, 16
	ret
```
2. Let's rewrite the code in C.
```c
int func1(int w0, int w1)
{
	int sp12 = w0;
	int sp8 = w1;
	w1 = sp12;
	w0 = sp8;

	if(w1 <= w0)
		return sp8;
	else
		return sp12;
}
```
3. There's some unnecessary swapping of variables, let's simplify it.
```c
int func1(int w0, int w1)
{
	if(w0 <= w1)
        return w1;
    else
        return w0;
}
```
4. Calling the function as `func1(1765227561, 1830628817)` returns `1830628817`. Convert it to hex for the flag: `picoCTF{6d1d2dd1}`
