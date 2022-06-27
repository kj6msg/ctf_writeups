# ARMssembly 1
## Description
For what argument does this program print 'win' with variables ```85```, ```6``` and ```3```?\
File: [chall_1.S](chall_1.S)\
Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})
## Hints
1. Shifts
## Solution
1. The function to look at is ```func```.
```
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
2. Breaking it down to pseudo-code makes the logic clearer.
```
int func(int param0)
    int a = 85
	int b = 6
	int c = 3

	return (a << b) / c) - param0
```
3. The return value of ```func``` is compared with ```0```.
```
	bl	func
	cmp	w0, 0
```
4. Following the code, we 'win' if the user input is equal to the math in ```func```, which is 1813 (rounded). Convert to hex for the flag.
```
picoCTF{00000715}
```
