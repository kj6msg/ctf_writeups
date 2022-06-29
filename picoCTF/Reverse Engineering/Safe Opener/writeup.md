# Safe Opener
## Description
Can you open this safe? I forgot the key to my safe but this [program](SafeOpener.java) is supposed to help me with retrieving the lost key. Can you help me unlock my safe? Put the password you recover into the picoCTF flag format like: ```picoCTF{password}```
## Hints
(None)
## Solution
1. Looks like the string is stored encoded in ```openSafe``` as ```encodedkey```.
```
public static boolean openSafe(String password) {
	String encodedkey = "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz";
	
	if (password.equals(encodedkey)) {
		System.out.println("Sesame open");
		return true;
	}
	else {
		System.out.println("Password is incorrect\n");
		return false;
	}
}
```
2. Looks like base64. Decode it.
```
% echo -n cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz | base64 -d | xargs printf "picoCTF{%s}\n"
picoCTF{pl3as3_l3t_m3_1nt0_th3_saf3}
```
