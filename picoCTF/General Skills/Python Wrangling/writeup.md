# Python Wrangling
## Description
Python scripts are invoked kind of like programs in the Terminal... Can you run [this Python script](ende.py) using [this password](pw.txt) to get [the flag](flag.txt.en)?
## Hints
1. Get the Python script accessible in your shell by entering the following command in the Terminal prompt: ```$ wget https://mercury.picoctf.net/static/8e33ede04d02f3765b8c6a6e24d72733/ende.py```
2. ```$ man python```
## Solution
1. View the files. The python script accepts a few options and the flag is encoded.
2. Run the python script's help option.
```
% python ende.py -h
Usage: ende.py (-e/-d) [file]
Examples:
  To decrypt a file named 'pole.txt', do: '$ python ende.py -d pole.txt'

```
3. Decrypt the flag.
```
% python ende.py -d flag.txt.en < pw.txt 
Please enter the password:picoCTF{4p0110_1n_7h3_h0us3_aa821c16}
```
