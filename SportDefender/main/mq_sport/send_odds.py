from common.config import env_config
from common.data.sport_data_interface import get_whole_match_markets
from task.rocket_mq.mq_requset import send_message
from task.rocket_mq.sport_message_body import market_odds

# 配置环境 fat1，fat2，fat3,fat4,pre,prod
env_config.env = 'fat1'


# 发送早盘消息
def send_prematch_odds(match_id, market_id):
    # mq消息体
    message_body = market_odds.create_message_body(match_id, market_id)
    # 推送mq消息
    send_message.send_message_str('match_markets_update', message_body)


# 发送滚盘消息
def send_inplay_odds(match_id, market_id):
    # mq消息体
    message_body = market_odds.create_message_body(match_id, market_id)
    # 推送mq消息
    send_message.send_message_str('inplay_market_odds_update', message_body)


# 推送某场赛事所有玩法的消息
def send_match_whole_markets_message(match_id, betting_phase):
    market_ids = get_whole_match_markets(match_id)
    print(market_ids)
    if betting_phase == 'pre':
        for market_id in market_ids:
            send_prematch_odds(match_id, market_id)
    elif betting_phase == 'inplay':
        for market_id in market_ids:
            send_inplay_odds(match_id, market_id)
    else:
        print("Please check params!")


# 推送单个玩法的消息
def send_match_market_message(match_id, market_id, betting_phase):
    market_ids = get_whole_match_markets(match_id)
    if market_id not in market_ids:
        print("market id is wrong")
        return
    if betting_phase == 'pre':
        send_prematch_odds(match_id, market_id)
    elif betting_phase == 'inplay':
        send_inplay_odds(match_id, market_id)
    else:
        print("Please check params!")


# mq消息体
# odds.create_message_body(2748, 1)

# 推送单个玩法的消息
# send_match_market_message(2207, 5, 'pre')

# 推送某场赛事所有玩法的消息
# send_match_whole_markets_message(2539, 'pre')
