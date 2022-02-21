import requests
from common.config import api_config


def send_message_str(topic, message):
    url = api_config.get_mq_domain()
    header = {
        'Content-Type': 'application/json;charset=UTF-8'
    }
    data = {
        "topic": topic,
        "key": "key",
        "tag": "tag",
        "messageBody": message
    }
    res = requests.post(url, json=data, headers=header)
    print(f"Send result :{res.text}")

