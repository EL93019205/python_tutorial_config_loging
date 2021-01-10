"""
CRITICAL
ERROR
WARNING
INFO
DEBUG
"""
import logging

# logging.basicConfig(filename='test.log', level=logging.DEBUG)
logging.basicConfig(level=logging.DEBUG)

logging.critical('critical')
logging.error('error')
logging.warning('warning')
logging.info('info')
logging.debug('debug')
