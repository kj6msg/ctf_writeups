# Lazy Game Challenge
## Description
I found an interesting game made by some guy named "John_123". It is some betting game. I made some small fixes to the game; see if you can still pwn this and steal $1000000 from me!

To get flag, pwn the server at: `nc thekidofarcrania.com 10001`
## Hints
(None)
## Solution
1. The game doesn't do proper bounds checking. Bet `-10000000` and keep entering `0` for your guesses.
```console
% printf "y\n-1000000\n0\n0\n0\n0\n0\n0\n0\n0\n0\n0\n" | nc thekidofarcrania.com 10001
Sorry you didn't made it !
Play Again !...
Better Luck next Time !.
Sorry you lost some money !..
Your balance has been updated !.
Current balance :  : 
1000500$
What the... how did you get that money (even when I tried to stop you)!? I guess you beat me!

The flag is CTFlearn{d9029a08c55b936cbc9a30_i_wish_real_betting_games_were_like_this!}

Thank you for playing ! 
Made by John_123
Small mods by theKidOfArcrania
Give it a (+1) if you like !..
```
