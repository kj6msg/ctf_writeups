# Serpentine
## Description
Find the flag in the Python script! [Download Python script](serpentine.py)
## Hints
1. Try running the script and see what happens
2. In the webshell, try examining the script with a text editor like ```nano```
3. To exit ```nano```, press Ctrl and x and follow the on-screen prompts.
4. The ```str_xor``` function does not need to be reverse engineered for this challenge.
## Solution
1. Option ```b``` should print the flag, but it doesn't.
```
    elif choice == 'b':
      print('\nOops! I must have misplaced the print_flag function! Check my source code!\n\n')
```
2. Modify the code as follows.
```
    elif choice == 'b':
      # print('\nOops! I must have misplaced the print_flag function! Check my source code!\n\n')
      print_flag()
```
3. Run the modified script and choose option ```b```.
```
picoCTF{7h3_r04d_l355_7r4v3l3d_ae0b80bd}
```
