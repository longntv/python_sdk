# app/container.py
from dependency_injector import containers, providers
from app.application.application import Application
from app.domain.my_entity import MyEntity
from app.infrastructure.redis.message_subscriber import MessageSubscriber
from app.handler.consumer_handler import ConsumerHandler
from app.handler.worker_handler import WorkerHandler
from app.utils.config import Config
from app.infrastructure.redis.message_publisher import MessagePublisher

class Container(containers.DeclarativeContainer):
    config = providers.Object(Config)
    # my_entity = providers.Singleton(MyEntity)
    message_subscriber = providers.Singleton(MessageSubscriber, config=config)
    message_publisher = providers.Singleton(MessagePublisher, config=config)
    consumer_handler = providers.Factory(ConsumerHandler, config=config)
    worker_handler = providers.Factory(WorkerHandler, config=config)
    application = providers.Factory(Application, 
                                     message_subscriber=message_subscriber,
                                     message_publisher=message_publisher,
                                     consumer_handler=consumer_handler,
                                     worker_handler=worker_handler,
                                    )