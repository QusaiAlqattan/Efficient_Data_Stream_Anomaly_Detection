# logger.py
import logging

def setup_logger():
    """
    Configures and initializes the logger for the application, writing logs to 'app.log'.
    Logs will include timestamps, log levels, and the log messages.

    - Log file: 'app.log' (appends to existing log file if it exists).
    - Log format: '[timestamp] - [log level] - [message]'
    - Log level: INFO (includes INFO, WARNING, ERROR, and CRITICAL messages).
    """

    logging.basicConfig(
        filename='app.log',
        filemode='a',
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

def log_error(message):
    """
    Logs an error message.

    Parameters:
    -----------
    message : str
        The error message to be logged.
    """
    logging.error(message)

def log_info(message):
    """
    Logs an informational message.

    Parameters:
    -----------
    message : str
        The informational message to be logged.
    """
    logging.info(message)
