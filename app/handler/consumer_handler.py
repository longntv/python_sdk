
from app.infrastructure.redis.message_subscriber import MessageSubscriber

class ConsumerHandler:
    def __init__(self, config):
        self.config = config
        self.subscriber = MessageSubscriber(config)
        self.subscriber.subscribe(config.APP_TAG, self.handle_message)

    def handle_message(self, channel, message):
        # Process the message here
        print(f"Received message from {channel}: {message}")
