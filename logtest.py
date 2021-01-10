"""
logtest
"""
import logging

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)


def do_something():
    """
    do_something
    """
    LOGGER.info('from logtest')
    LOGGER.debug('from logtest debug')
