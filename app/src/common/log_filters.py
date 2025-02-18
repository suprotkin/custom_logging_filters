import logging

from src.common.redis_client import redis_client



class CustomLogFilter(logging.Filter):
    def filter(self, record):
        if record.extra.get('filtered'):
            log_filter = redis_client.get('log_filter')
            if log_filter is not None:
                return log_filter in record.message
            return False
        return True

