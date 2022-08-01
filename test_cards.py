import random


class Card:
    suits = ['\u2666', '\u2665', '\u2663', '\u2660']
    rank = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{Card.rank[self.rank]}{Card.suits[self.suit]}'

    def __lt__(self, other):
        if self.rank == other.rank:
            return self.suit < other.suit
        else:
            return self.rank < other.rank


# card1 = Card(1,1)
# print(card1)


class Deck:
    def __init__(self):
        self.deck = []
        for suit in range(4):
            for rank in range(13):
                self.deck.append(Card(suit, rank))
        self.shuffle()

    def __len__(self):
        return len(self.deck)

    def add_card(self, card):
        self.deck.append(card)

    def pop_card(self):
        return self.deck.pop()

    def shuffle(self):
        random.shuffle(self.deck)


deck1 = Deck()


class Hand(Deck):
    def __init__(self, label):
        self.deck = []
        self.label = label
        self.win_count = 0

    def __str__(self):
        return self.label + ': ' + ' '.join(str(card) for card in self.deck)

    def get_label(self, label):
        return self.label

    def win_count(self):
        return self.win_count

    def winner_of_round(self):
        self.win_count += 1


hands = []
deck = Deck()

for i in range(1, 5):
    hands.append(Hand(f'P{i}'))

while len(deck) > 0:
    for hand in hands:
        hand.add_card(deck.pop_card())
for i in range(13):
    input()
    played_cards = []
    for hand in hands:
        played_cards.append(hand.pop_card())
    for card in played_cards:
        print(card)
    print(max(played_cards))
