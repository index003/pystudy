from itertools import chain
from config import env_config
from rocket import send_message
from rocket import message_body_odds
from data import mq_basic

# 配置环境 fat1，fat2，fat3,fat4,pre,prod
env_config.env = 'fat2'


# 发送早盘消息
def send_prematch_odds(match_id, market_id):
    # mq消息体
    message_body = message_body_odds.create_message_body(match_id, market_id)
    # 推送mq消息
    send_message.send_message_str('match_markets_update', message_body)


# 发送滚盘消息
def send_inplay_odds(match_id, market_id):
    # mq消息体
    message_body = message_body_odds.create_message_body(match_id, market_id)
    # 推送mq消息
    send_message.send_message_str('inplay_market_odds_update', message_body)


# 获取某场赛事所有的玩法id
def get_match_whole_markets(match_id):
    market_query_result = mq_basic.query_whole_markets_by_id(match_id)
    market_ids = list(chain.from_iterable(market_query_result))
    return market_ids


# 推送某场赛事所有玩法的消息
def send_match_whole_markets_message(match_id, betting_phase):
    market_ids = get_match_whole_markets(match_id)
    print(market_ids)
    if betting_phase == 'pre':
        for market_id in market_ids:
            send_prematch_odds(match_id, market_id)
    elif betting_phase == 'inplay':
        for market_id in market_ids:
            send_inplay_odds(match_id, market_id)
    else:
        print("Please check params!")


send_match_whole_markets_message(1773, 'inplay')


# 推送单个玩法的消息
def send_match_market_message(match_id, market_id, betting_phase):
    market_ids = get_match_whole_markets(match_id)
    if market_id not in market_ids:
        print("market id is wrong")
        return
    if betting_phase == 'pre':
        send_prematch_odds(match_id, market_id)
    elif betting_phase == 'inplay':
        send_inplay_odds(match_id, market_id)
    else:
        print("Please check params!")


# send_match_market_message(2055, 1, 'dka')

