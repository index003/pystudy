from task.rocket_mq.sport_message_body import match_status
from task.rocket_mq.mq_requset import send_message
from common.config import env_config

env_config.env = 'fat1'


def send_match_status_message(match_id, status=1):
    # mq消息体
    message_body = match_status.match_status_msg(match_id, status)
    # 推送mq消息
    send_message.send_message_str('match_metadata_update', message_body)
    print(message_body)


print(match_status.match_status_msg(2591, 1))
# send_match_status_message(2591, 3)

'''
status:

NOT_STARTED_YET(1),未开赛
IN_PROGRESS(2),进行中
FINISHED(3),已完赛
CANCELLED(4),已取消
POSTPONED(5),已延期
INTERRUPTED(6),已中断
ABANDONED(7),
COVERAGE_LOST(8),
ABOUT_TO_START(9)
'''
