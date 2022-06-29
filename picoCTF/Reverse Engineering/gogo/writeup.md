# gogo
## Description
Hmmm this is a weird file... [enter_password](enter_password). There is a instance of the service running at `mercury.picoctf.net:35862`.
## Hints
1. use go tool objdump or ghidra
## Solution
1. Connect to the server.
```console
% nc mercury.picoctf.net 35862
Enter Password: helloworld
```
2. Ok, let's take a look in Ghidra. The function `main.checkPassword` is a good place to start.
```c
void main.checkPassword(int param_1,uint param_2)
{
  uint *puVar1;
  uint uVar2;
  int iVar3;
  int *in_GS_OFFSET;
  undefined4 local_40;
  undefined4 local_3c;
  undefined4 local_38;
  undefined4 local_34;
  undefined4 local_30;
  undefined4 local_2c;
  undefined4 local_28;
  undefined4 local_24;
  byte local_20 [28];
  undefined4 uStack4;
  
  puVar1 = (uint *)(*(int *)(*in_GS_OFFSET + -4) + 8);
  if (&stack0x00000000 < (undefined *)*puVar1 || &stack0x00000000 == (undefined *)*puVar1) {
    uStack4 = 0x80d4b72;
    runtime.morestack_noctxt();
    main.checkPassword();
    return;
  }
  if ((int)param_2 < 0x20) {
    os.Exit(0);
  }
  FUN_08090b18();
  local_40 = 0x38313638;
  local_3c = 0x31663633;
  local_38 = 0x64336533;
  local_34 = 0x64373236;
  local_30 = 0x37336166;
  local_2c = 0x62646235;
  local_28 = 0x39383338;
  local_24 = 0x65343132;
  FUN_08090fe0();
  uVar2 = 0;
  iVar3 = 0;
  while( true ) {
    if (0x1f < (int)uVar2) {
      if (iVar3 == 0x20) {
        return;
      }
      return;
    }
    if ((param_2 <= uVar2) || (0x1f < uVar2)) break;
    if ((*(byte *)(param_1 + uVar2) ^ *(byte *)((int)&local_40 + uVar2)) == local_20[uVar2]) {
      iVar3 = iVar3 + 1;
    }
    uVar2 = uVar2 + 1;
  }
  runtime.panicindex();
  do {
    invalidInstructionException();
  } while( true );
}
```
3. It appears that `param1` is the user password and `param2` is the length of the password, which must be 32. The `if` statement below checks the user password by XORing it with a key and comparing it to a known value.
```c
if ((*(byte *)(param_1 + uVar2) ^ *(byte *)((int)&local_40 + uVar2)) == local_20[uVar2])
```
4. The 32 byte key (`0x6534313239383338626462353733616664373236643365333166363338313638`) is stored as a series of assignments to `local_40` through `local_24`. The known values are stored at `local_20`. Where is that loaded? Looking at the assembly after loading the key, you see the following instructions.
```
080d4af1 8d 7c 24 24     LEA        EDI=>local_20,[ESP + 0x24]
080d4af5 8d 35 00        LEA        ESI,[main.statictmp_4]
		 fe 10 08
080d4afb e8 e0 c4        CALL       FUN_08090fe0
		 fb ff
```
5. A little more probing reveals that `FUN08090fe0` copies 32 bytes stored at `main.statictmp_4` (`0x014650454b5755410e011054555d00050d4557530a5a025d540345415d47534a`) to `local_20`. These are the expected values. Run the following script to reverse the XOR and decode the password. Note that the hex values are reversed for proper endianness prior to decoding.
```python
import binascii

key = "6534313239383338626462353733616664373236643365333166363338313638"
key = binascii.unhexlify(key)[::-1]
xor = "014650454b5755410e011054555d00050d4557530a5a025d540345415d47534a"
xor = binascii.unhexlify(xor)[::-1]

password = ""
for n in range(32):
    password += chr(key[n] ^ xor[n])

print("Password: " + password)
```
```console
% python decode.py
Password: reverseengineericanbarelyforward
% nc mercury.picoctf.net 35862
Enter Password: reverseengineericanbarelyforward
=========================================
This challenge is interrupted by psociety
What is the unhashed key?
```
6. So, the key is hashed. Poking around in Ghidra a little more reveals another function named `main.ambush`. There are references to `md5` in the function. Entering the key (reversed for proper endianness) into a [MD5 reverse lookup](https://md5.gromweb.com) yields `goldfish`.
```console
% nc mercury.picoctf.net 35862
Enter Password: reverseengineericanbarelyforward
=========================================
This challenge is interrupted by psociety
What is the unhashed key?
goldfish
Flag is:  picoCTF{p1kap1ka_p1c05729981f}
```
