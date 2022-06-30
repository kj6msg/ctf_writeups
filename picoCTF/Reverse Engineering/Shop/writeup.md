# Shop
## Description
Best Stuff - Cheap Stuff, Buy Buy Buy... Store Instance: [source](source). The shop is open for business at `nc mercury.picoctf.net 34938`.
## Hints
1. Always check edge cases when programming
## Solution
1. Run the program.
```console
% nc mercury.picoctf.net 34938
Welcome to the market!
=====================
You have 40 coins
	Item		Price	Count
(0) Quiet Quiches	10	12
(1) Average Apple	15	8
(2) Fruitful Flag	100	1
(3) Sell an Item
(4) Exit
Choose an option: 
```
2. Try option 2.
```console
2
How many do you want to buy?
1
Not enough money.
You have 40 coins
	Item		Price	Count
(0) Quiet Quiches	10	12
(1) Average Apple	15	8
(2) Fruitful Flag	100	1
(3) Sell an Item
(4) Exit
Choose an option: 
```
3. Buy an item.
```console
0
How many do you want to buy?
1
You have 30 coins
	Item		Price	Count
(0) Quiet Quiches	10	11
(1) Average Apple	15	8
(2) Fruitful Flag	100	1
(3) Sell an Item
(4) Exit
Choose an option: 
```
4. Can we buy a negative number of items?
```console
0
How many do you want to buy?
-1
You have 40 coins
	Item		Price	Count
(0) Quiet Quiches	10	12
(1) Average Apple	15	8
(2) Fruitful Flag	100	1
(3) Sell an Item
(4) Exit
Choose an option: 
```
5. Bingo. Buy `-6` Quiet Quiches and then buy the Fruitful Flag.
```console
0
How many do you want to buy?
-6
You have 100 coins
	Item		Price	Count
(0) Quiet Quiches	10	18
(1) Average Apple	15	8
(2) Fruitful Flag	100	1
(3) Sell an Item
(4) Exit
Choose an option: 
2
How many do you want to buy?
1
Flag is:  [112 105 99 111 67 84 70 123 98 52 100 95 98 114 111 103 114 97 109 109 101 114 95 98 97 54 98 56 99 100 102 125]
```
6. Looks like ASCII. Use [CyberChef](https://gchq.github.io/CyberChef/) to decode it: `picoCTF{b4d_brogrammer_ba6b8cdf}`
