# Bases
## Description
What does this ```bDNhcm5fdGgzX3IwcDM1``` mean? I think it has something to do with bases.
## Hints
1. Submit your answer in our flag format. For example, if your answer was 'hello', you would submit 'picoCTF{hello}' as the flag.
## Solution
1. Looks like base64.
```
% echo -n "bDNhcm5fdGgzX3IwcDM1" | base64 -d
l3arn_th3_r0p35
```
2. The flag is ```picoCTF{l3arn_th3_r0p35}```.
