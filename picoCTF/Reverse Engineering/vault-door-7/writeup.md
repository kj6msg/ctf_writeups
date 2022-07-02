# vault-door-7
## Description
This vault uses bit shifts to convert a password string into an array of integers. Hurry, agent, we are running out of time to stop Dr. Evil's nefarious plans! The source code for this vault is here: [VaultDoor7.java](VaultDoor7.java)
## Hints
1. Use a decimal/hexadecimal converter such as this one: https://www.mathsisfun.com/binary-decimal-hexadecimal-converter.html
2. You will also need to consult an ASCII table such as this one: https://www.asciitable.com/
## Solution
1. This is straight forward. The `passwordToIntArray` function converts the password bytes into a hex array from the ASCII representation.
```java
public int[] passwordToIntArray(String hex) {
    int[] x = new int[8];
    byte[] hexBytes = hex.getBytes();
    for (int i=0; i<8; i++) {
        x[i] = hexBytes[i*4]   << 24
                | hexBytes[i*4+1] << 16
                | hexBytes[i*4+2] << 8
                | hexBytes[i*4+3];
    }
    return x;
}

public boolean checkPassword(String password) {
    if (password.length() != 32) {
        return false;
    }
    int[] x = passwordToIntArray(password);
    return x[0] == 1096770097
        && x[1] == 1952395366
        && x[2] == 1600270708
        && x[3] == 1601398833
        && x[4] == 1716808014
        && x[5] == 1734304867
        && x[6] == 942695730
        && x[7] == 942748212;
}
```
2. Run the script below to decode.
```python
import binascii

encoded = [1096770097, 1952395366, 1600270708, 1601398833, 1716808014, 1734304867, 942695730, 942748212]
password = ""

for i in range(len(encoded)):
    password += binascii.unhexlify(f'{encoded[i]:08x}').decode()

print("picoCTF{" + password + "}")
```
```console
% python decode.py
picoCTF{A_b1t_0f_b1t_sh1fTiNg_dc80e28124}
```
