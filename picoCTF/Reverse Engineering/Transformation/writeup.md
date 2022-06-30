# Transformation
## Description
I wonder what this really is... [enc](enc) `''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])`
## Hints
1. You may find some decoders online
## Solution
1. View the file.
```console
% cat enc
灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弰㑣〷㘰摽
```
2. Copy the unicode string to CyberChef and run through the Magic tool (intensive mode). Scrolling through the results, looks like a UTF-16BE encoded string: `picoCTF{16_bits_inst34d_of_8_04c0760d}`
