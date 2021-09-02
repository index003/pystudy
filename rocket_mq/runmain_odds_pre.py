import rocket

#
# '''早盘赔率变更'''
#
# # 切换环境
rocket.env_no = 1
#
# # 发送单个消息
#
# # 足球胜平负赔率变更MQ
# rocket.send_message('match_markets_update', 'odds_prematch_football_1_1x2.json')
# # 足球大小盘赔率变更MQ
# rocket.send_message('match_markets_update', 'odds_prematch_football_2_under_over.json')
# # 足球大小盘赔率变更MQ
# rocket.send_message('match_markets_update', 'odds_prematch_football_3_asian_handicap.json')
#
# # 发送批量消息
# message_files = [
#     'odds_prematch_football_1_1x2.json',
#     'odds_prematch_football_2_under_over.json',
#     'odds_prematch_football_3_asian_handicap.json'
# ]
# rocket.send_message_list('match_markets_update', message_files)

rocket.send_message('match_markets_update', 'odds_prematch_football_21_under_over_hf.json')
