import hashlib
import json

from config import env_config
from rocket import message_body_external
from rocket import send_message

# 配置环境 fat1，fat2，fat3,fat4,pre,prod
env_config.env = 'fat2'


def md5_value(match_id, source):
    source = source.lower()
    string = f"matchId={match_id}&source={source}VkryuBktdSvnglZd"
    input_name = hashlib.md5()
    input_name.update(string.encode("utf-8"))
    md5_32_lower = input_name.hexdigest().lower()  # 小写32位
    md5_32_upper = input_name.hexdigest().upper()  # 大写32位
    md5_16_lower = input_name.hexdigest()[8:-8].lower()  # 小写16位
    md5_16_upper = input_name.hexdigest()[8:-8].upper()  # 大写16位
    return md5_32_lower


def send_result_request(match_id):
    message_body = message_body_external.create_message_body_request(match_id)
    send_message.send_message_str('EXTERNAL_MATCH_RESULT_REQUEST', message_body)


def send_results(match_id, source_id, add_score):
    message_body = message_body_external.create_message_body_results(match_id, source_id, add_score)
    print(message_body)
    temp_message = message_body
    # temp_message = json.loads(message_body)
    source = temp_message['sourceName']
    temp_message['hash'] = md5_value(match_id, source)
    message_body = json.dumps(temp_message)
    send_message.send_message_str('EXTERNAL_MATCH_RESULT', message_body)


def send_result_respons(match_id, source_id, add_score):
    message_body = message_body_external.create_message_body_results(match_id, source_id, add_score)
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

send_external_message(2, 3, 3, 1652)
