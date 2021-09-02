import rocket

'''赛果消息MQ '''
# 切换环境
rocket.env_no = 3

# 发送单个消息

# category = 8 football
# rocket.send_message('match_livescore_update', 'match_result_8_football.json')

# 发送批量消息
message_files = [
    'match_result_8_football.json',
    'match_result_9_basketball.json',
    'match_result_10_tennis.json',
    'match_result_11_AM_football.json',
    'match_result_12_baseball.json'
]
rocket.send_message_list('match_livescore_update', message_files)
