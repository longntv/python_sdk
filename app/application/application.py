from app.infrastructure.redis.message_publisher import MessagePublisher
from app.infrastructure.redis.message_subscriber import MessageSubscriber
from app.handler.consumer_handler import ConsumerHandler
from app.handler.worker_handler import WorkerHandler


class Application:
    def __init__(self, 
                 message_publisher: MessagePublisher,
                 message_subscriber: MessageSubscriber,
                 consumer_handler: ConsumerHandler,
                 worker_handler: WorkerHandler,
                ):
        self.redis_message_publisher = message_publisher
        self.redis_message_subscriber = message_subscriber
        self.consumer_handler = consumer_handler
        self.worker_handler = worker_handler

    def start(self):
        self.worker_handler.run_in_background()