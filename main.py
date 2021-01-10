"""
CRITICAL
ERROR
WARNING
INFO
DEBUG
"""
import logging

FORMATTER = '%(levelname)s:%(message)s'
# FORMATTER = '%(asctime)s:%(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMATTER)

logging.critical('critical')
logging.error('error')
logging.warning('warning')
logging.info('info')
logging.debug('debug')
