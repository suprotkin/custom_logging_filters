import logging

from src.common.redis_client import redis_client


class CustomLogFilter(logging.Filter):
    def filter(self, record):
        if hasattr(record, 'filtered') and record.filtered:
            log_filter = redis_client.db.get('log_filter')
            if log_filter:
                return log_filter in record.getMessage()
            return False
        return True
