from src.utils.simulate import simulate
from src.utils.logging import setup_logger
import time
import logging

if __name__ == '__main__':
    n_trials = 500000
    n_players = 4

    logger = setup_logger()

    logger.info("Simulation started.")
    start = time.time()
    simulate(n_trials, n_players)
    end = time.time()

    duration = end - start
    logger.info(f"Simulation for {n_trials} trials with {n_players} players completed in {duration:.4f} seconds.")


    
