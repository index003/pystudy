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




