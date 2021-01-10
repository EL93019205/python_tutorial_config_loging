"""
CRITICAL
ERROR
WARNING
INFO
DEBUG
"""
import logging

# pylint: disable=R0903
logging.basicConfig(level=logging.INFO)


class NoPassFilter(logging.Filter):
    """
    NoPassFilter
    """
    def filter(self, record):
        """
        filter
        """
        log_message = record.getMessage()
        return 'password' not in log_message


LOGGER = logging.getLogger(__name__)
LOGGER.addFilter(NoPassFilter())
LOGGER.info('from main')
LOGGER.info('from main password = "test"')
