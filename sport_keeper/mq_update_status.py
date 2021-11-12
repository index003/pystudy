from rocket_mq import message_body_status
from rocket_mq import send_message
from config import env_config

env_config.env = 'fat2'


def send_match_status_message(match_id, status=2):
    # mq消息体
    message_body = message_body_status.match_status_msg(match_id, status)
    # 推送mq消息
    send_message.send_message_str('match_metadata_update', message_body)


send_match_status_message(1621)

'''
status:

NOT_STARTED_YET(1,"Not started yet","The event has not started yet"),未开赛
IN_PROGRESS(2,"In progress","The event is live"),进行中
FINISHED(3,"Finished","The event is finished"),已完赛
CANCELLED(4,"Cancelled"    ,"The event has been cancelled"),已取消
POSTPONED(5,"Postponed"    ,"The event has been postponed"),已延期
INTERRUPTED(6,"Interrupted"    ,"The event has been interrupted"),已中断
ABANDONED(7,"Abandoned"    ,"The event has been abandoned"),
COVERAGE_LOST(8,"Coverage lost","The coverage for this event has been lost"),
ABOUT_TO_START(9,"About to start","The event has not started but is about to. ")
'''
