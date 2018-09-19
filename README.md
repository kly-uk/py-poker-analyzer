# Poker hand analyser

This program will analyze whether the player's hand is higher than the opponents', as well as displaying the winner of the Poker round.


## 1. Guidelines

A poker hand has a constructor that accepts a string containing 5 cards:

```python
hand = PokerHand("KS 2H 5C JD TD");
```

and a method to compare itself to another hand

```python
def compare_with(self, opponent):
    # Your code here
    return 0
```

The characteristics of the string of cards are:
*   A space is used as card seperator
*   Each card consists of two characters
*   The first character is the value of the card, valid characters are: `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `T`(en), `J`(ack), `Q`(ueen), `K`(ing), `A`(ce)
*   The second character represents the suit, valid characters are: `S`(pades), `H`(earts), `D`(iamonds), `C`(lubs)

The result of the poker hand compare can be one of the 3 options:
*   0 for a TIE
*   1 for a WIN
*   2 for a LOSS

The ranking of the hands follows the [Texas Hold'em rules](https://www.partypoker.com/how-to-play/hand-rankings.html)


## 2. Tests

Sample unit tests have been included in the code skeleton. You can run them as a script: `python tests.py`. Writing more tests is welcome :)
