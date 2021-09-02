import rocket

#
# '''滚盘实时比分'''
#
# # 切换环境
rocket.env_no = 1
#
# # 发送单个消息
#
rocket.send_message('match_livesocre_update', 'match_livescore_update.json')

# # 发送批量消息
# message_files = [
#     'odds_prematch_football_1_1x2.json',
#     'odds_prematch_football_2_under_over.json',
#     'odds_prematch_football_3_asian_handicap.json'
# ]
# rocket.send_message_list('inplay_market_odds_update', message_files)

