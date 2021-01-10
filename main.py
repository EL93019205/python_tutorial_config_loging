"""
CRITICAL
ERROR
WARNING
INFO
DEBUG
"""
import logging
import logtest

logging.basicConfig(level=logging.INFO)

logging.info('info')

LOGGER = logging.getLogger(__name__)
LOGGER.info('from main')

logtest.do_something()
