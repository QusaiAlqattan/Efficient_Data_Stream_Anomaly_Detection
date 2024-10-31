# logger.py
import logging

def setup_logger():
    """Set up the logger for the application."""
    logging.basicConfig(
        filename='app.log',
        filemode='a',
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

def log_error(message):
    """Log an error message."""
    logging.error(message)

def log_info(message):
    """Log an informational message."""
    logging.info(message)
