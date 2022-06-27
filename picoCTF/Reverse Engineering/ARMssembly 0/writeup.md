# ARMssembly 0
## Description
What integer does this program print with arguments ```1765227561``` and ```1830628817```?\
File: [chall.S](chall.S)\
Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})
## Hints
1. Simple compare
## Solution
1. The function to look at is ```func1```.
```
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
2. Breaking it down to pseudo-code makes the logic clearer.
```
int func1(int a, int b)
    if(a <= b)
        return b
    else
        return a
```
3. The function is called as ```func1(1765227561, 1830628817)``` which will return ```1830628817```. Convert it to hex for the flag format.
```
picoCTF{6d1d2dd1}
```
