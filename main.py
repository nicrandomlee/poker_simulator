from src.utils.simulate import simulate
from src.utils.logging import setup_logger
import time
import logging

if __name__ == '__main__':
    n_trials = 1500000
    n_players = 4
    winners_dict_filepath="winner_4_player_results.json"
    losers_dict_filepath="loser_4_player_results.json"

    logger = setup_logger()

    logger.info("Simulation started.")
    start = time.time()
    simulate(n_trials = n_trials, 
             n_players = n_players, 
             winners_dict_filepath=winners_dict_filepath, 
             losers_dict_filepath=losers_dict_filepath)
    end = time.time()

    duration = end - start
    logger.info(f"Simulation for {n_trials} trials with {n_players} players completed in {duration:.4f} seconds.")


    
