
import json
from utils.logger import Logger
import threading
import time
from app.infrastructure.redis.message_publisher import MessagePublisher

# from app.application.service import ServiceA

class WorkerHandler:
    def __init__(self, config):
        self.running = False
        self.config = config
        self.interval = int(config.WORKER_INTERVAL)
        self.message_publisher = MessagePublisher(config=config)

    def handle(self):
        Logger.GetLogger().info("WorkerHandler doing task....")
        # TODO: add processing here

        Logger.GetLogger().info("WorkerHandler send message to IOGATE")
        # TODO: send message to IOGATE if have any
        # publish a message to the Redis channel
        self.message_publisher.publish(self.config.IOGATE_CHANNEL, json.dumps({
            'type': 'result',
            'data': 'example',
        }))

    def run(self):
        self.running = True
        Logger.GetLogger().info("WorkerHandler running!")
        while self.running:
            # Sleep for interval seconds
            time.sleep(self.interval)
            self.handle()

    def run_in_background(self):
        thread = threading.Thread(target=self.run)
        thread.daemon = True
        thread.start()