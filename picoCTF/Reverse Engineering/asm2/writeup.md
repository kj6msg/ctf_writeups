# asm2
## Description
What does asm2(0x4,0x2d) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](test.S)
## Hints
1. assembly [conditions](https://www.tutorialspoint.com/assembly_programming/assembly_conditions.htm)
## Solution
1. Let's convert this to C for readability.
```
asm2:
	<+0>:	push   ebp
	<+1>:	mov    ebp,esp
	<+3>:	sub    esp,0x10
	<+6>:	mov    eax,DWORD PTR [ebp+0xc]
	<+9>:	mov    DWORD PTR [ebp-0x4],eax
	<+12>:	mov    eax,DWORD PTR [ebp+0x8]
	<+15>:	mov    DWORD PTR [ebp-0x8],eax
	<+18>:	jmp    0x50c <asm2+31>
	<+20>:	add    DWORD PTR [ebp-0x4],0x1
	<+24>:	add    DWORD PTR [ebp-0x8],0xd1
	<+31>:	cmp    DWORD PTR [ebp-0x8],0x5fa1
	<+38>:	jle    0x501 <asm2+20>
	<+40>:	mov    eax,DWORD PTR [ebp-0x4]
	<+43>:	leave  
	<+44>:	ret    
```
```c
int asm2(int param0, int param1)
{
    int ebp4 = param1;
    int ebp8 = param0;

    while(ebp8 <= 0x5fa1)
    {
        ++ebp4;
        ebp8 += 0xd1;
    }

    return ebp4;
}
```
2. Pretty simple. Let's compute the loop iterations.
```
(0x5fa1 - 0x4) / 0xd1 = 0x75
0x75 * 0xd1 = 0x5f85
````
3. Room for one more. The flag is `0x75 + 0x1 + 0x2d = 0xa3`
