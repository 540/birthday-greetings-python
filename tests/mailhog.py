import time
import os
import requests


def start_mailhog():
    os.system("docker-compose stop")
    os.system("docker-compose up -d")


def stop_mailhog():
    os.system("docker-compose stop")
    os.system("docker-compose rm -f")


def messages_sent():
    time.sleep(5)
    return requests.get("http://127.0.0.1:8025/api/v1/messages", timeout=1).json()
