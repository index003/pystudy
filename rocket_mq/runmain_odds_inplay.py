import rocket

#
# '''滚盘赔率变更'''
#
# # 切换环境
rocket.env_no = 1
#
# # 发送单个消息
#
rocket.send_message('inplay_market_odds_update', 'odds_inplay_football_207_minutes_result.json')

# # 发送批量消息
# message_files = [
#     'odds_prematch_football_1_1x2.json',
#     'odds_prematch_football_2_under_over.json',
#     'odds_prematch_football_3_asian_handicap.json'
# ]
# rocket.send_message_list('inplay_market_odds_update', message_files)

