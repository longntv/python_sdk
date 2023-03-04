# app/utils/config.py

import os
from dotenv import load_dotenv
import json

load_dotenv()

class Config:
    ENV = "debug"
    IOGATE_CHANNEL = "IOG_SUPERVISOR"
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    # Consumer queue from IOGATE to App
    APP_UUID = os.getenv('UUID')
    # Tag queue from App to IOGATE
    APP_TAG = os.getenv('IPC_TAG')
    # Worker interval
    WORKER_INTERVAL = os.getenv('INTERVAL')
    # Redis config
    REDIS_HOST = os.getenv('REDIS_HOST')
    REDIS_PASSWORD = os.getenv('REDIS_PASSWORD')
    REDIS_PORT = os.getenv('REDIS_PORT', 6379)
    # Log file
    IS_LOG_FILE = os.getenv('LOG_FILE', 'disable')
    # Set PathFile
    LOG_FILE_PATH = ""
    if IS_LOG_FILE == "enable" and ENV != "debug":
        LOG_FILE_PATH = "../host_data/iogate-docker-{AppTag}.log" 

    def __str__(self):
        return str({k: v for k, v in self.__dict__.items() if not k.startswith('__')})

