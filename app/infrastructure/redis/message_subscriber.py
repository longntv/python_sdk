# app/infrastructure/redis/message_subscriber.py

import threading
from abc import ABC, abstractmethod
import redis

class MessageSubscriberInterface(ABC):
    @abstractmethod
    def subscribe(self, channel: str, handler):
        pass

class MessageSubscriber(MessageSubscriberInterface):
    def __init__(self, config):
        self.redis = redis.Redis(
            host=config.REDIS_HOST,
            port=config.REDIS_PORT,
            password=config.REDIS_PASSWORD
        )
        self.config = config
        self.thread = None

    def subscribe(self, channel:str, handler):
        self.thread = threading.Thread(target=self.listen, args=(handler,channel))
        self.thread.start()

    def listen(self, handler, channel):
        print("MessageSubscriber listening channel ", channel)
        while True:
            # block until a message is received
            message = self.redis.brpop(channel)
            handler(channel, message)
