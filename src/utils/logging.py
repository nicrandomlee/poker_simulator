import time
import logging
import os

def setup_logger():
    # Get current time string like "28072025 21-00-00"
    current_time = time.strftime("%d%m%Y %H-%M-%S")  # Replace ':' by '-'

    # Create logs folder path
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)  # Just ensure 'logs' folder exists

    # Log file path with timestamp + " simulation.py"
    log_file = os.path.join(log_dir, f"{current_time} simulation.log")

    # Configure logging
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)  # Log all levels DEBUG and above

    # Formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # File handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Also log to console (optional)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger