from src.deck import Deck
from src.card import Card
from src.utils.utils import best_hand, compare_hands
from src.utils.save import load_simulation_results, save_simulation_results

import copy


def simulate(n_trials = 10000, n_players = 4, winners_dict_filepath="winner_4_player_results.json", losers_dict_filepath="loser_4_player_results.json"):
    results_dict = load_simulation_results(winners_dict_filepath)
    losers_dict = load_simulation_results(losers_dict_filepath)

    for _ in range(n_trials):
        deck = Deck()
        player_hands = []
        for i in range(n_players):
            player_hands.append(sorted(deck.draw(2)))
        board = deck.draw(5)
        
        best_player_idx = 0
        for curr_challenger_idx in range(1, n_players):
            best_player_hand = copy.deepcopy(player_hands[best_player_idx])
            best_player_hand.extend(board)
            curr_challenger_hand = copy.deepcopy(player_hands[curr_challenger_idx])
            curr_challenger_hand.extend(board)
            duel_winner = compare_hands(best_player_hand, curr_challenger_hand)
            if duel_winner == -1:
                best_player_idx = curr_challenger_idx
        
        winning_hand = player_hands[best_player_idx]
        player_hands.pop(best_player_idx)

        winning_hand_str = tuple([str(card) for card in winning_hand])
        if winning_hand_str not in results_dict:
            results_dict[winning_hand_str] = 0
        results_dict[winning_hand_str] += 1

        for losing_hand in player_hands:
            losing_hand_str = tuple([str(card) for card in losing_hand])
            if losing_hand_str not in losers_dict:
                losers_dict[losing_hand_str] = 0
            losers_dict[losing_hand_str] += 1

    save_simulation_results(results_dict, winners_dict_filepath)
    save_simulation_results(losers_dict, losers_dict_filepath)


