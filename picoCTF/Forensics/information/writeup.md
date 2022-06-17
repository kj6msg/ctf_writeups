# information
## Description
Files can always be changed in a secret way. Can you find the flag? [cat.jpg](cat.jpg)
## Hints
1. Look at the details of the file
2. Make sure to submit the flag as picoCTF{XXXXX}
## Solution
1. Confirm the file is a JPEG.
```
% file cat.jpg
cat.jpg: JPEG image data, JFIF standard 1.02, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 2560x1598, components 3
```
2. View the JPEG file. Looks like a cute cat sitting on a computer, trying to be a 1337 h@x0r.
3. Examine the metadata with ```exiftool```. The ```License``` string looks like base64 encoding.
4. Decode the string.
```
% echo -n "cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9" | base64 -d
picoCTF{the_m3tadata_1s_modified}
```
