# reverse_cipher
## Description
We have recovered a [binary](rev) and a [text file](rev_this). Can you reverse the flag.
## Hints
1. objdump and Gihdra are some tools that could assist with this
## Solution
1. Load it in Ghidra. I've renamed some of the variables for clarity.
```c
void main(void)
{
  size_t sVar1;
  char flag_buf [23];
  char local_41;
  int local_2c;
  FILE *rev_file;
  FILE *flag_file;
  uint j;
  int i;
  char local_9;
  
  flag_file = fopen("flag.txt","r");
  rev_file = fopen("rev_this","a");
  if (flag_file == (FILE *)0x0) {
    puts("No flag found, please make sure this is run on the server");
  }
  if (rev_file == (FILE *)0x0) {
    puts("please run this on the server");
  }
  sVar1 = fread(flag_buf,0x18,1,flag_file);
  local_2c = (int)sVar1;
  if ((int)sVar1 < 1) {
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  for (i = 0; i < 8; i = i + 1) {
    local_9 = flag_buf[i];
    fputc((int)local_9,rev_file);
  }
  for (j = 8; (int)j < 23; j = j + 1) {
    if ((j & 1) == 0) {
      local_9 = flag_buf[(int)j] + 5;
    }
    else {
      local_9 = flag_buf[(int)j] + -2;
    }
    fputc((int)local_9,rev_file);
  }
  local_9 = local_41;
  fputc((int)local_41,rev_file);
  fclose(rev_file);
  fclose(flag_file);
  return;
}
```
2. The encoding logic is contained in a couple of `for` loops. It's pretty cut and dry... inside the curly braces, characters at an even index are incremented by 5 and characters at an odd index are decremented by 2. Reverse this with the following script.
```python
encoded = list("w1{1wq84fb<1>49")
decoded = [None] * len(encoded)

for i in range(len(encoded)):
    if i & 1 == 0:
        decoded[i] = chr(ord(encoded[i]) - 5)
    else:
        decoded[i] = chr(ord(encoded[i]) + 2)

print("picoCTF{" + "".join(decoded) + "}")
```
```console
% python decode.py
picoCTF{r3v3rs36ad73964}
```
