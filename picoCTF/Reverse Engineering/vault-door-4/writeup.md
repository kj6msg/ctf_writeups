# vault-door-4
## Description
This vault uses ASCII encoding for the password. The source code for this vault is here: [VaultDoor4.java](VaultDoor4.java)
## Hints
1. Use a search engine to find an "ASCII table".
2. You will also need to know the difference between octal, decimal, and hexadecimal numbers.
## Solution
1. This is straight forward. The password is just stored as different representations of characters.
```java
public boolean checkPassword(String password) {
    byte[] passBytes = password.getBytes();
    byte[] myBytes = {
        106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
        0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
        0142, 0131, 0164, 063 , 0163, 0137, 070 , 0146,
        '4' , 'a' , '6' , 'c' , 'b' , 'f' , '3' , 'b' ,
    };
    for (int i=0; i<32; i++) {
        if (passBytes[i] != myBytes[i]) {
            return false;
        }
    }
    return true;
}
```
2. Run the script below.
```python
password = [106, 85, 53, 116, 95, 52, 95, 98, 0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f, 0o142, 0o131, 0o164, 0o63, 0o163, 0o137, 0o70, 0o146, '4', 'a', '6', 'c', 'b', 'f', '3', 'b']

passw = ""

for i in range(24):
    passw += chr(password[i])

for i in range(24, len(password)):
    passw += password[i]

print("picoCTF{" + passw + "}")
```
```console
% python decode.py
picoCTF{jU5t_4_bUnCh_0f_bYt3s_8f4a6cbf3b}
```
