"""
CRITICAL
ERROR
WARNING
INFO
DEBUG
"""
import logging.config

LOGGER = logging.getLogger(__name__)

LOGGER.error('api call is failed')

LOGGER.error({
    'action': 'create',
    'status': 'fail',
    'message': 'Api call is failed'
})
