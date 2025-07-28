import sys
import os
import pytest


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.utils.utils import compare_hands
from src.card import Card

# Test 1
hand1 = [Card('♣', '2'), Card('♦', '2'), Card('♦', '4'), Card('♥', '4'), Card('♣', 'K')]
hand2 = [Card('♣', '2'), Card('♦', '2'), Card('♣', '4'), Card('♥', '4'), Card('♣', 'K')]
test1 = compare_hands(hand1, hand2)
assert test1 == 0


# Test 2
hand3 = [Card('♣', '2'), Card('♣', '3'), Card('♣', '4'), Card('♣', '5'), Card('♣', '6')]
hand4 = [Card('♦', '3'), Card('♦', '4'), Card('♦', '5'), Card('♦', '6'), Card('♣', '7')]
test2 = compare_hands(hand3, hand4)
print(test2)
assert test2 == 1

hand5 = [Card('♣', '2'), Card('♣', '5'), Card('♣', '7'), Card('♣', '10'), Card('♣', 'K')]
hand6 = [Card('♦', '3'), Card('♦', '4'), Card('♦', '5'), Card('♦', '9'), Card('♣', 'Q')]
test3 = compare_hands(hand5, hand6)
assert test3 == 1

hand7 = [Card('♣', '2'), Card('♣', '3'), Card('♦', '4'), Card('♣', '5'), Card('♣', '6')]
hand8 = [Card('♦', '3'), Card('♦', '4'), Card('♦', '5'), Card('♦', '6'), Card('♣', '7')]
test4 = compare_hands(hand7, hand8)
assert test4 == -1

