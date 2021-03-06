from common.config import env_config
from task.rocket_mq.mq_requset import send_message
from task.rocket_mq.sport_message_body import match_score

# 配置环境 fat1，fat2，fat3,fat4,pre,prod

env_config.env = 'fat1'


# 发送赛果比分消息
def send_match_result_socre(match_id):
    # mq消息体
    message_body = match_score.create_score_message_body(match_id)
    # 推送mq消息
    send_message.send_message_str('match_livescore_update', message_body)


def send_match_live_score(match_id, *score):
    # mq消息体
    message_body = match_score.create_live_score_message_body(match_id, *score)
    # 推送mq消息
    send_message.send_message_str('match_livescore_update', message_body)


def send_score_message(match_id, score_type, *score):
    if score_type == 'result':
        send_match_result_socre(match_id)
    elif score_type == 'live':
        send_match_live_score(match_id, *score)
    else:
        print("Please check params!")


print(match_score.create_score_message_body(3039))
send_score_message(3039, 'live')
