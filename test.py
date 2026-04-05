from src.mcqgenerator.logger import logging
def test_logging():
    logging.info("This is an info message for testing.")
    logging.error("This is an error message for testing.")
    logging.warning("This is a warning message for testing.")
    logging.debug("This is a debug message for testing.")