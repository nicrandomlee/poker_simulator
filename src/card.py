class Card:
    SUITS = ['♣', '♦', '♥', '♠']
    VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    VALUE_RANK = {v: i for i, v in enumerate(VALUES)}

    def __init__(self, suit, value):
        if suit not in Card.SUITS:
            raise ValueError(f"Invalid suit: {suit}. Choose from {Card.SUITS}")
        if value not in Card.VALUES:
            raise ValueError(f"Invalid value: {value}. Choose from {Card.VALUES}")
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value}{self.suit}"
    
    def __str__(self):
        return f"{self.value}{self.suit}"
    
    def __lt__(self, other):
        return Card.VALUE_RANK[self.value] < Card.VALUE_RANK[other.value]

    def __eq__(self, other):
        return self.suit == other.suit and self.value == other.value