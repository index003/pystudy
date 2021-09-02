import rocket

'''早盘赔率变更'''

# # 切换环境
rocket.env_no = 1
#
# # 发送单个消息
# 赛事结算消息
rocket.send_message('match_market_bet_settlements', 'match_settlement.json')
#
