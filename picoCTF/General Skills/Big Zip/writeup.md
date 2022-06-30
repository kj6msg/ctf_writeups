# Big Zip
## Description
Unzip this archive and find the flag.
* [Download zip file](big-zip-files.zip)
## Hints
1. Can grep be instructed to look at every file in a directory and its subdirectories?
## Solution
1. Unzip the file and `grep` for the flag.
```console
% unzip big-zip-files.zip
% grep -hIRo 'picoCTF.*' *
picoCTF{gr3p_15_m4g1c_ef8790dc}
```
