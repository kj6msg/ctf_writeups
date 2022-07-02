# Bbbbloat
## Description
Can you get the flag?  
Reverse engineer this [binary](bbbbloat).
## Hints
(None)
## Solution
1. Load it in Ghidra. The entry point calls the main function located at `0x1307`.
```c
undefined8 main(void)
{
  char *__s;
  long in_FS_OFFSET;
  int local_48;
  undefined8 local_38;
  undefined8 local_30;
  undefined8 local_28;
  undefined8 local_20;
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  local_38 = 0x4c75257240343a41;
  local_30 = 0x3062396630664634;
  local_28 = 0x63633066635f3d33;
  local_20 = 0x4e5f6532636637;
  printf("What\'s my favorite number? ");
  __isoc99_scanf();
  if (local_48 == 549255) {
    __s = (char *)FUN_00101249(0,&local_38);
    fputs(__s,stdout);
    putchar(10);
    free(__s);
  }
  else {
    puts("Sorry, that\'s not it!");
  }
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}
```
2. That was easy. Run the program and enter the favorite number `549255`.
```console
% ./bbbbloat
What's my favorite number? 549255
picoCTF{cu7_7h3_bl047_44f74a60}
```
