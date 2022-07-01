# vault-door-3
## Description
This vault uses for-loops and byte arrays. The source code for this vault is here: [VaultDoor3.java](VaultDoor3.java)
## Hints
1. Make a table that contains each value of the loop variables and the corresponding buffer index that it writes to.
## Solution
1. This is pretty straight forward, we just need to reverse the algorithm.
```java
public boolean checkPassword(String password) {
    if (password.length() != 32) {
        return false;
    }
    char[] buffer = new char[32];
    int i;
    for (i=0; i<8; i++) {
        buffer[i] = password.charAt(i);
    }
    for (; i<16; i++) {
        buffer[i] = password.charAt(23-i);
    }
    for (; i<32; i+=2) {
        buffer[i] = password.charAt(46-i);
    }
    for (i=31; i>=17; i-=2) {
        buffer[i] = password.charAt(i);
    }
    String s = new String(buffer);
    return s.equals("jU5t_a_sna_3lpm18g947_u_4_m9r54f");
}
```
2. Run the following python script for the flag: `picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_79958f}`
```python
#!/usr/bin/env python3

buffer = list("jU5t_a_sna_3lpm18g947_u_4_m9r54f")
password = [None] * len(buffer)

for i in range(0, 8):
    password[i] = buffer[i]

for i in range(8, 16):
    password[23 - i] = buffer[i]

for i in range(16, 32, 2):
    password[46 - i] = buffer[i]

for i in range(17, 32, 2):
    password[i] = buffer[i]

print("picoCTF{" + "".join(password) + "}")
```
