import itertools
from src.card import Card

def best_hand(seven_cards):
    """
    Given a list of 7 Card objects, return a tuple:
    (best 5-card hand as a list of Card objects, hand ranking string)
    """
    best = None
    best_rank = None
    best_hand_ranking = None

    for combo in itertools.combinations(seven_cards, 5):
        rank, hand_ranking = evaluate_hand(combo)
        if best_rank is None or rank > best_rank:
            best = combo
            best_rank = rank
            best_hand_ranking = hand_ranking

    return list(best), best_hand_ranking

def evaluate_hand(hand):
    """
    Assigns a sortable value to a hand according to poker hand strength.
    Higher value = stronger hand. Adapt this for your Card implementation.
    """
    # Check for flush
    suits = [card.suit for card in hand]
    is_flush = any(suits.count(suit) == 5 for suit in set(suits))

    # Get sorted values, treating A as both high and low for straight
    value_str_to_int = {'A':14, 'K':13, 'Q':12, 'J':11, '10':10, '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2}
    values = sorted([value_str_to_int[card.value] for card in hand], reverse=True)
    unique_values = sorted(set(values), reverse=True)

    # Check for straight (including 5-4-3-2-A)
    is_straight = False
    for i in range(len(unique_values)-4):
        if unique_values[i] - unique_values[i+4] == 4:
            is_straight = True
            break
    # Special case for Ace-low straight
    if set([14, 2, 3, 4, 5]).issubset(set(values)):
        is_straight = True

    # Count occurrences for pairs, trips, quads
    counts = {v: values.count(v) for v in set(values)}
    counts_sorted = sorted(counts.items(), key=lambda x: (-x[1], -x[0]))

    # Assign ranking tuple (bigger first element = stronger)
    if is_flush and is_straight:
        rank = (8, max(values))  # Straight flush
        hand_ranking = "Straight Flush"
    elif counts_sorted[0][1] == 4:
        rank = (7, counts_sorted[0][0], counts_sorted[1][0])  # Four of a kind
        hand_ranking = "Four of a kind"
    elif counts_sorted[0][1] == 3 and counts_sorted[1][1] == 2:
        rank = (6, counts_sorted[0][0], counts_sorted[1][0])  # Full house
        hand_ranking = "Full House"
    elif is_flush:
        rank = (5, values)  # Flush
        hand_ranking = "Flush"
    elif is_straight:
        rank = (4, max(values))  # Straight
        hand_ranking = "Straight"
    elif counts_sorted[0][1] == 3:
        rank = (3, counts_sorted[0][0], values)  # Three of a kind
        hand_ranking = "Three of a kind"
    elif counts_sorted[0][1] == 2 and counts_sorted[1][1] == 2:
        rank = (2, counts_sorted[0][0], counts_sorted[1][0], values)  # Two pair
        hand_ranking = "Two Pair"
    elif counts_sorted[0][1] == 2:
        rank = (1, counts_sorted[0][0], values)  # One pair
        hand_ranking = "One Pair"
    else:
        rank = (0, values)  # High card
        hand_ranking = "High Card"
    return rank, hand_ranking

def compare_hands(hand1, hand2):
    """
    Compare two 5-card hands and determine which one is stronger.

    Args:
        hand1 (list of Card): First 5-card hand.
        hand2 (list of Card): Second 5-card hand.

    Returns:
        int: 1 if hand1 is stronger,
             -1 if hand2 is stronger,
             0 if hands are of equal strength (tie).
    """
    rank1, _ = evaluate_hand(hand1)
    rank2, _ = evaluate_hand(hand2)

    if rank1 > rank2:
        return 1
    elif rank2 > rank1:
        return -1
    else:
        return 0