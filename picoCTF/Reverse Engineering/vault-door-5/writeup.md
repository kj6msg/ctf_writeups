# vault-door-5
## Description
In the last challenge, you mastered octal (base 8), decimal (base 10), and hexadecimal (base 16) numbers, but this vault door uses a different change of base as well as URL encoding! The source code for this vault is here: [VaultDoor5.java](VaultDoor5.java)
## Hints
1. You may find an encoder/decoder tool helpful, such as https://encoding.tools/
2. Read the wikipedia articles on URL encoding and base 64 encoding to understand how they work and what the results look like.
## Solution
1. This is straight forward. The password is URL encoded and then base64 encoded.
```java
public boolean checkPassword(String password) {
    String urlEncoded = urlEncode(password.getBytes());
    String base64Encoded = base64Encode(urlEncoded.getBytes());
    String expected = "JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVm"
                    + "JTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2"
                    + "JTM0JTVmJTY1JTMzJTMxJTM1JTMyJTYyJTY2JTM0";
    return base64Encoded.equals(expected);
}
```
2. Run the script below to decode.
```python
import base64
import urllib.parse

encoded = "JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVmJTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2JTM0JTVmJTY1JTMzJTMxJTM1JTMyJTYyJTY2JTM0"
password = urllib.parse.unquote(base64.b64decode(encoded))

print("picoCTF{" + password + "}")
```
```console
% python decode.py
picoCTF{c0nv3rt1ng_fr0m_ba5e_64_e3152bf4}
```
