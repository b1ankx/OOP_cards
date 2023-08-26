import random

class Suit: 
    name: str
    symbol: str

    def to_text(self) -> str:
        return self.name + self.symbol
        
class Suits:
    def diamonds(self):
        s = Suit()
        s.name = ''
        s.symbol = '\u2666'
        return s
    
    def cluds(self):
        s = Suit()
        s.name = ''
        s.symbol = '\u2663'
        return s
    
    def hearts(self):
        s = Suit()
        s.symbol = '\u2665'
        s.name = ''
        return s

    def spades(self):
        s = Suit()
        s.name = ''
        s.symbol = '\u2660'
        return s


class Card():
    name: str
    suit: Suit

    def __init__(self, name, suit: Suit):
        self.suit = suit
        self.name = name
    
    def to_text(self) -> str:
        return self.suit.to_text() + self.name

class Deck:
    cards: list[Card]

    def __init__(self) -> list:
        self.cards = list()

    def shuffle(self):
       random.shuffle(self.cards)

    def give_one_card(self):
        return self.cards.pop()

    def to_text(self):
        len_of_cards = str(len(self.cards))
        text = 'колода из : ' + len_of_cards + '\n'
        for card in self.cards:
            text += card.to_text() + ' '
        return text

class DeckBuilder():
    cards = list[Card]

    def __init__(self):
        self.cards = list()

    def create_cards_names(self):
        numbers = ['10','9','8','7','6','5','4','3','2']
        pictures = ['A', 'Q', 'K', 'J']
        names = numbers +  pictures     
        return names

    def create_suits(self):
        suits = Suits()
        diamonds_suit = suits.diamonds()
        hearts_suit = suits.hearts()
        spades_suit = suits.spades()
        cluds_suit = suits.cluds()
        return [diamonds_suit, hearts_suit, spades_suit, cluds_suit]

    def create_deck(self):
        for n in self.create_cards_names():
            for s in self.create_suits():
                c = Card(n,s)
                self.cards.append(c)
        d = Deck()
        d.cards = self.cards
        return d

class SmallDeckBuilder(DeckBuilder):
    def create_card_names(self):
        return ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6']

class FullDeckBuilder(DeckBuilder):
    def create_card_names(self):
        return ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']

deck1: Deck = SmallDeckBuilder().create_deck()
deck2: Deck = FullDeckBuilder().create_deck()
print(deck1.to_text())
print('*****'*3)
print(deck2.to_text())
