from collections import namedtuple
from pprint import pprint
from random import choice

# creates a subclass of named tuple
Card = namedtuple("Card", ["rank", "suit"])
# print(Card)

p = Card(10, 11)
# print(p, type(p))


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = "spades diamonds clubs hearts".split()

    def __init__(self) -> None:
        # self._cards = [Card(rank, suit) for rank, suit in zip(self.ranks, self.suits)]
        self._cards = [Card(rank, suit)for rank in self.ranks ## Used list Comprehension here
                       for suit in self.suits]
        # pprint(list(zip(range(1, 100), self._cards))) ## adds the indexes to another iterable

    def __len__(self):  ## Special method 1
        return len(self._cards)

    def __getitem__(self, position):  ## Special method 2
        return self._cards[position]

## to call these special methods, create an instance and call them as a regular function with instance as the argument
my_deck = FrenchDeck()
# print(my_deck)
# print(len(my_deck))
# print(my_deck[0])
# print(my_deck[10])
print(choice(my_deck))  ## Picking a random card


## Printing all cards in the deck
index = 1
for card in my_deck:
    print(f"{index}: {card}")
    index += 1




