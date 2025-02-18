
from structlog import DropEvent

from src.common.redis_client import redis_client


class ConditionalDropper:
    def __call__(self, logger, method_name, event_dict):
        if event_dict.get('filtered'):
            log_filter = redis_client.db.get('log_filter')
            event_dict['log_filter'] = log_filter
            if log_filter is None or log_filter not in event_dict["event"]:
                event_dict["raised"] = "DropEvent"
                raise DropEvent


        return event_dict

conditional_dropper = ConditionalDropper()
