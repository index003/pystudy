import requests

# 环境序号，默认1
env_no = 1


def send_message_list(topic, message_files):
    for message_file in message_files:
        send_message(topic, message_file)


def send_message(topic, message_file):
    """
   发送MQ消息
   :param topic:MQ 主题
   :param message_file:MQ消息主体
   """

    url = f'http://fat{env_no}.console.testbitgame.com/topic/sendTopicMessage.do'
    header = {
        'Content-Type': 'application/json;charset=UTF-8'
    }
    with open('message_collect/' + message_file) as f:
        message_body = f.read()
        data = {
            "topic": topic,
            "key": "key",
            "tag": "tag",
            "messageBody": message_body
        }
        res = requests.post(url, json=data, headers=header)
        print(f"Send result :{res.text}")
        print(res.text)
