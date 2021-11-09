from config import env_config
from rocket_mq import match_status
from rocket_mq import match_odds_1x2
from rocket_mq import rocket

# 配置环境 fat1，fat2，fat3,fat4,pre,prod
env_config.env = 'fat2'


# 推送mq消息
def sub_mq(topic, message):
    rocket.send_message_str(topic, message)


# mq消息体
def get_message_body(match_id, status):
    return match_status.match_status_msg(match_id, status)


# message_body = get_message_body(2407, 3)
# sub_mq('match_metadata_update', message_body)

message_body = match_odds_1x2.match_odds_1x2_msg(1587)
sub_mq('match_markets_update', message_body)
