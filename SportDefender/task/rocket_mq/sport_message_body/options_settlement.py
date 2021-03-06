import json
import time
from collections import namedtuple
from common.data import sport_data_interface


# 拼接赛事结算的消息体
# 拼接赛事结算的bets域的消息
def create_messages_markets_bets(match_id, market_id):
    bets_fields = [
        "id",
        "name",
        "line",
        "baseLine",
        "status",
        "startPrice",
        "price",
        "settlement",
        "lastUpdate",
        "lastUpdateTime"
    ]
    BetsMsg = namedtuple('BetsMsg', bets_fields)
    current_millis = int(time.time() * 1000)
    fixture_id = sport_data_interface.get_match_info_by_id(match_id, 'fixture_id')
    query_result = sport_data_interface.get_match_market_option_by_id(fixture_id, market_id)
    bets_body = []
    for item in query_result:
        bet_msg = BetsMsg(0, *item, '1', current_millis,current_millis)
        bet_body = str(bet_msg._asdict()).replace("'", '"')
        bets_body.append(eval(bet_body))

    return bets_body


# 拼接完整的消息体
def create_message_body(match_id, market_id):
    bets = create_messages_markets_bets(match_id, market_id)
    fixtureId = sport_data_interface.get_match_info_by_id(match_id, 'fixture_id')
    message_body = {
        "fixtureId": fixtureId,
        "source": "LSPORTS",
        "markets": [
            {
                "id": market_id,
                "names": {},
                "bets": bets
            }
        ],
        "updateType": "SETTLEMENT"
    }
    return json.dumps(message_body)


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

