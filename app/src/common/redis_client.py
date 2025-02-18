import redis
import structlog
from src.redis_config import REDIS_CONFIG

logger = structlog.get_logger(__name__)

class RedisClient:
    def __init__(self):
        self.db = redis.Redis(**REDIS_CONFIG)

    def get(self, key):
        logger.info(f'Redis get: {key}', filtered=True)
        return self.db.get(key)

    def set(self, key, value):
        logger.info(f'Redis set: {key}={value}', filtered=True)
        self.db.set(key, value)

    def delete(self, key):
        logger.info(f'Redis del: {key}', filtered=True)
        self.db.delete(key)

redis_client = RedisClient()
