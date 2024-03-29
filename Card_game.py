import random

class Card:
    suits = ['\u2666', '\u2665', '\u2663', '\u2660']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{Card.ranks[self.rank]}{Card.suits[self.suit]}'

    def __lt__(self, other):
        if self.rank == other.rank:
            return self.suit < other.suit
        else:
            return self.rank < other.rank



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
        return random.shuffle(self.deck)



class Hand(Deck):

    def __init__(self, label):
        self.deck = []
        self.label = label
        self.win_count = 0

    def __str__(self):
        return self.label + ': ' + ' '.join(str(card) for card in self.deck)

    def get_label(self):
        return self.label
    def round_winner(self):
        return self.win_count
    def get_win_count(self):
        self.win_count += 1


if __name__ == "__main__":
    hands = []
    deck = Deck()

    for i in range(1,5):
        hands.append(Hand(f'Player {i}'))

    while len(deck) > 0:
        for i in range(4):
            hands[i].add_card(deck.pop_card())

    for hand in hands:
        print(hand)

    for i in range(13):
        input()
        played_cards = []
        for hand in hands:
            played_cards.append(hand.pop_card())
        winner_card = max(played_cards)
        winner_hand = hands[played_cards.index(winner_card)]
        z = " ".join(str(x) for x in played_cards)
        winner_hand.get_win_count()
        print(f'Round{i}: {z}, Winner: {winner_hand.get_label()} ({winner_hand.round_winner()} win rounds) with card: {winner_card}')
    input()

    final_results = {}
    for hand in hands:
        print(f'{hand.get_label()}: {hand.round_winner()} win rounds')
        final_results[str(hand.get_label())] = int(hand.round_winner())
    fin_max = max(final_results, key=final_results.get)
    print(f'\nThe winner of this game is: {fin_max}')





