# vault-door-8
## Description
Apparently Dr. Evil's minions knew that our agency was making copies of their source code, because they intentionally sabotaged this source code in order to make it harder for our agents to analyze and crack into! The result is a quite mess, but I trust that my best special agent will find a way to solve it. The source code for this vault is here: [VaultDoor8.java](VaultDoor8.java)
## Hints
1. Clean up the source code so that you can read it and understand what is going on.
2. Draw a diagram to illustrate which bits are being switched in the scramble() method, then figure out a sequence of bit switches to undo it. You should be able to reuse the switchBits() method as is.
## Solution
1. This is straight forward. There are three functions of interest: `scramble`, `switchBits`, and `checkPassword`.
```java
public char[] scramble(String password) {
    /* Scramble a password by transposing pairs of bits. */
    char[] a = password.toCharArray();
    
    for (int b=0; b<a.length; b++) {
        char c = a[b];
        
        c = switchBits(c,1,2);
        c = switchBits(c,0,3);
        /*
        c = switchBits(c,14,3);
        c = switchBits(c, 2, 0);
        */
        c = switchBits(c,5,6);
        c = switchBits(c,4,7);
        c = switchBits(c,0,1);
        /*
        d = switchBits(d, 4, 5);
        e = switchBits(e, 5, 6);
        */
        c = switchBits(c,3,4);
        c = switchBits(c,2,5);
        c = switchBits(c,6,7);
        
        a[b] = c;
    }
    return a;
}

public char switchBits(char c, int p1, int p2) {
    /*
    Move the bit in position p1 to position p2, and move the bit
    that was in position p2 to position p1. Precondition: p1 < p2
    */
    char mask1 = (char)(1 << p1);
    char mask2 = (char)(1 << p2);
    /*
    char mask3 = (char)(1<<p1<<p2);
    mask1++;
    mask1--;
    */
    char bit1 = (char)(c & mask1);
    char bit2 = (char)(c & mask2);
    /*
    System.out.println("bit1 " + Integer.toBinaryString(bit1));
    System.out.println("bit2 " + Integer.toBinaryString(bit2));
    */
    char rest = (char)(c & ~(mask1 | mask2));
    char shift = (char)(p2 - p1);
    char result = (char)((bit1<<shift) | (bit2>>shift) | rest);
    return result;
}

public boolean checkPassword(String password) {
    char[] scrambled = scramble(password);
    char[] expected = {0xF4, 0xC0, 0x97, 0xF0, 0x77, 0x97, 0xC0, 0xE4, 0xF0, 0x77, 0xA4, 0xD0, 0xC5, 0x77, 0xF4, 0x86, 0xD0, 0xA5, 0x45, 0x96, 0x27, 0xB5, 0x77, 0xE0, 0x95, 0xF1, 0xE1, 0xE0, 0xA4, 0xC0, 0x94, 0xA4 };
    return Arrays.equals(scrambled, expected);
}
```
2. We can reuse `switchBits`. To descramble, just run the scramble sequence in reverse.
```python
def switch_bits(c, p1, p2):
    mask1 = 1 << p1
    mask2 = 1 << p2

    bit1 = c & mask1
    bit2 = c & mask2

    rest = c & ~(mask1 | mask2)
    shift = p2 - p1
    result = (bit1 << shift) | (bit2 >> shift) | rest
    
    return result

scrambled = [0xF4, 0xC0, 0x97, 0xF0, 0x77, 0x97, 0xC0, 0xE4, 0xF0, 0x77, 0xA4, 0xD0, 0xC5, 0x77, 0xF4, 0x86, 0xD0, 0xA5, 0x45, 0x96, 0x27, 0xB5, 0x77, 0xE0, 0x95, 0xF1, 0xE1, 0xE0, 0xA4, 0xC0, 0x94, 0xA4]
password = ""

for i in range(len(scrambled)):
    c = scrambled[i]

    c = switch_bits(c, 6, 7)
    c = switch_bits(c, 2, 5)
    c = switch_bits(c, 3, 4)

    c = switch_bits(c, 0, 1)
    c = switch_bits(c, 4, 7)
    c = switch_bits(c, 5, 6)

    c = switch_bits(c, 0, 3)
    c = switch_bits(c, 1, 2)

    password += chr(c)

print("picoCTF{" + password + "}")
```
```console
% python decode.py
picoCTF{s0m3_m0r3_b1t_sh1fTiNg_2e762b0ab}
```
