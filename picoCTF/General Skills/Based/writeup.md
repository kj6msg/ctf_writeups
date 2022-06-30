# Based
## Description
To get truly 1337, you must understand different data encodings, such as hexadecimal or binary. Can you get the flag from this program to prove you are on the way to becoming 1337? Connect with `nc jupiter.challenges.picoctf.org 15130`.
## Hints
1. I hear python can convert things.
2. It might help to have multiple windows open.
## Solution
1. Connect to the server and use [CyberChef](https://gchq.github.io/CyberChef/) to convert the values (binary, octal, and hex).
```console
% nc jupiter.challenges.picoctf.org 15130
Let us see how data is stored
table
Please give the 01110100 01100001 01100010 01101100 01100101 as a word.
...
you have 45 seconds.....

Input:
table
Please give me the  157 166 145 156 as a word.
Input:
oven
Please give me the 70656172 as a word.
Input:
pear
You've beaten the challenge
Flag: picoCTF{learning_about_converting_values_02167de8}
```
