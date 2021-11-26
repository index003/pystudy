from config import env_config
from rocket import message_body_external
from rocket import send_message

# 配置环境 fat1，fat2，fat3,fat4,pre,prod
env_config.env = 'fat2'


def send_result_request(match_id):
    message_body = message_body_external.create_message_body_request(match_id)
    send_message.send_message_str('external_match_result_request', message_body)


def send_results(match_id, source_id, add_score):
    message_body = message_body_external.create_message_body_results(match_id, source_id, add_score)
    send_message.send_message_str('external_match_results', message_body)


def send_result_respons(match_id, source_id, add_score):
    message_body = message_body_external.create_message_body_results(match_id, source_id, add_score)
    send_message.send_message_str('external_match_result_respons', message_body)


def send_external_message(function_id, source_id, add_score, match_id):
    if function_id == 1:
        send_result_request(match_id)
    elif function_id == 2:
        send_results(match_id, source_id, add_score)
    elif function_id == 3:
        send_result_respons(match_id, source_id, add_score)
    else:
        print("function is not exist!")


# function_id: 1 rquest 2 results 3 respons
# source_id: 1 espn 2 hupu 3 sky
# add_score: 0 无加时比分 1 一个加时 2 两个加时 3 三个加时

send_external_message(2, 1, 0, 1558)

