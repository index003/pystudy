import rocket

'''赛事状态变化'''

# 切换环境
rocket.env_no = 4

# 发送单个消息

# 赛事状态变更MQ
'''
    NOT_STARTED_YET(1,"Not started yet","The event has not started yet"),未开赛
    IN_PROGRESS(2,"In progress","The event is live"),进行中
    FINISHED(3,"Finished","The event is finished"),已完赛
    CANCELLED(4,"Cancelled"    ,"The event has been cancelled"),已取消
    POSTPONED(5,"Postponed"    ,"The event has been postponed"),已延期
    INTERRUPTED(6,"Interrupted"    ,"The event has been interrupted"),已中断
    ABANDONED(7,"Abandoned"    ,"The event has been abandoned"),
    COVERAGE_LOST(8,"Coverage lost","The coverage for this event has been lost"),
    ABOUT_TO_START(9,"About to start","The event has not started but is about to. ");
'''
# rocket.send_message('match_metadata_update', 'match_status.json')

# 发送批量消息
message_files = [
    'match_status.json'
]
rocket.send_message_list('match_metadata_update', message_files)