# HashingJobApp
## Description
If you want to hash with the best, beat this test! ```nc saturn.picoctf.net 57689```
## Hints
1. You can use a commandline tool or web app to hash text
2. Press Ctrl and c on your keyboard to close your connection and return to the command prompt.
## Solution
1. Connect to the server.
```
% nc saturn.picoctf.net 57689
Please md5 hash the text between quotes, excluding the quotes: 'Microsoft'
Answer: 
```
2. Hash the text and copy the result. I use the command ```echo -n "Microsoft" | md5 | pbcopy``` in another terminal window.
```
140864078aeca1c7c35b4beb33c53c34
140864078aeca1c7c35b4beb33c53c34
Correct.
Please md5 hash the text between quotes, excluding the quotes: 'computer hackers'
Answer: 
```
3. Continue until you get the flag.
```
1034abc8025edcc22f58c35abc21e36f
1034abc8025edcc22f58c35abc21e36f
Correct.
Please md5 hash the text between quotes, excluding the quotes: 'a cheap motel'
Answer: 
d51908671c7603ec46c7379887509894
d51908671c7603ec46c7379887509894
Correct.
picoCTF{4ppl1c4710n_r3c31v3d_3eb82b73}
```
