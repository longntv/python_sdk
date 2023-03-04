import redis
from app.utils.config import Config


class MessagePublisher:
    def __init__(self, config: Config):
        self.redis = redis.Redis(
            host=config.REDIS_HOST,
            port=config.REDIS_PORT,
            password=config.REDIS_PASSWORD
        )

    def publish(self, channel: str, message: str):
        self.redis.rpush(channel, message)