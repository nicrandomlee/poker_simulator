import random
from .card import Card

class Deck:
    def __init__(self):
        self.cards_in_deck = []
        self.discard_pile = []
        self.get_new_deck()

    def get_new_deck(self):
        deck = []
        for suit in Card.SUITS:
            for value in Card.VALUES:
                deck.append(Card(suit, value))
        random.shuffle(deck)
        self.cards_in_deck = deck
        return

    def draw(self, num=1):
        """
        Draw num cards from the deck.
        Moves the drawn cards to the discard pile.
        Returns a list of Card objects.
        """
        if num > len(self.cards_in_deck):
            raise ValueError("Not enough cards in the deck to draw.")
        drawn = self.cards_in_deck[:num]
        self.cards_in_deck = self.cards_in_deck[num:]
        return drawn
    
    def burn(self, num=1):
        """
        Remove the top `num` cards from the deck and put them into the discard pile.
        """
        if num > len(self.cards_in_deck):
            raise ValueError("Not enough cards in deck to burn.")

        burned_cards = self.cards_in_deck[:num]
        self.cards_in_deck = self.cards_in_deck[num:]
        self.discard_pile.extend(burned_cards)

    def __repr__(self):
        return f"Deck({len(self.cards_in_deck)} cards left, {len(self.discard_pile)} in discard pile)"
