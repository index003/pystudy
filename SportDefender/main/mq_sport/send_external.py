import json

from common.config import env_config
from common.utils import encrypt_md5
from task.rocket_mq.sport_message_body import nba_external
from task.rocket_mq.mq_requset import send_message

# 配置环境 fat1，fat2，fat3,fat4,pre,prod
env_config.env = 'fat2'


def send_result_request(match_id):
    message_body = nba_external.create_message_body_request(match_id)
    send_message.send_message_str('EXTERNAL_MATCH_RESULT_REQUEST', message_body)


def send_results(match_id, source_id, add_score):
    message_body = nba_external.create_message_body_results(match_id, source_id, add_score)
    print(message_body)
    temp_message = message_body
    # temp_message = json.loads(message_body)
    source = temp_message['sourceName']
    temp_message['hash'] = encrypt_md5.md5_value(match_id, source)
    message_body = json.dumps(temp_message)
    send_message.send_message_str('EXTERNAL_MATCH_RESULT', message_body)


def send_result_respons(match_id, source_id, add_score):
    message_body = nba_external.create_message_body_results(match_id, source_id, add_score)
    send_message.send_message_str('EXTERNAL_MATCH_RESULT_RESPONSE', message_body)


def send_external_message(function_id, source_id, add_score, match_id):
    if function_id == 1:
        send_result_request(match_id)
    elif function_id == 2:
        send_results(match_id, source_id, add_score)
    elif function_id == 3:
        send_result_respons(match_id, source_id, add_score)
    else:
        print("function is not exist!")


# function_id: 1 rquest 2 result 3 response
# source_id: 1 espn 2 hupu 3 skysports
# add_score: 0 无加时比分 1 一个加时 2 两个加时 3 三个加时

# send_external_message(2, 3, 3, 1652)
