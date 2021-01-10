"""
logtest
"""
import logging

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

# H = logging.FileHandler('logtest.log')
# LOGGER.addHandler(H)


def do_something():
    """
    do_something
    """
    logging.info('from logtest info')
    LOGGER.info('from logtest')
    LOGGER.debug('from logtest debug')
