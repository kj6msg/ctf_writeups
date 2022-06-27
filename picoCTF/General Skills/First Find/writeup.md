# First Find
## Description
Unzip this archive and find the file named 'uber-secret.txt'
* [Download zip file](files.zip)
## Hints
(none)
## Solution
1. Unzip the zip file, find the file, and print its contents.
```
% unzip files.zip
% find files -name uber-secret.txt | xargs cat
picoCTF{f1nd_15_f457_ab443fd1}
```
