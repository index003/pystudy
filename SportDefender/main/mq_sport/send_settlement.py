from common.config import env_config
from task.rocket_mq.mq_requset import send_message
from task.rocket_mq.sport_message_body import options_settlement

# 配置环境 fat1，fat2，fat3,fat4,pre,prod
env_config.env = 'fat1'


# 发送早盘消息
def send_option_settlement(match_id, market_id):
    # mq消息体
    message_body = options_settlement.create_message_body(match_id, market_id)
    # 推送mq消息
    send_message.send_message_str('match_markets_update', message_body)


# mq消息体
print(options_settlement.create_message_body(2748, 1))

'''
 "settlement": 
case -1:
    return PrizeType.CANCEL;
case 1:
    return PrizeType.LOSE;
case 2:
    return PrizeType.AWARD;
case 3:
    return PrizeType.DRAW;
case 4:
    return PrizeType.HALF_LOST;
case 5:
    return PrizeType.HALF_WIN;

topic:match_market_bet_settlements
'''

