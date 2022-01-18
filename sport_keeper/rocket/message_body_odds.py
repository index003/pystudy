import json
import time
from collections import namedtuple
from data.mq_basic import query_match_market_option_by_id, get_fixture_id_by_id
# from config import env_config
# env_config.env = 'fat1'


# 拼接赛事赔率变更的消息体
# 拼接odds的bets域的消息
def create_messages_markets_bets(match_id, market_id):
    bets_fields = [
        "id",
        "name",
        "line",
        "baseLine",
        "status",
        "startPrice",
        "price",
        "lastUpdateTime"
    ]
    BetsMsg = namedtuple('BetsMsg', bets_fields)
    current_millis = int(time.time() * 1000)
    fixture_id = get_fixture_id_by_id(match_id)
    query_result = query_match_market_option_by_id(fixture_id, market_id)
    bets_body = []
    for item in query_result:
        bet_msg = BetsMsg(0, *item, current_millis)
        bet_body = str(bet_msg._asdict()).replace("'", '"')
        bets_body.append(eval(bet_body))

    return bets_body


# 拼接完整的消息体
def create_message_body(match_id, market_id):
    bets = create_messages_markets_bets(match_id, market_id)
    fixtureId = get_fixture_id_by_id(match_id)
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
        "updateType": "ODDS"
    }
    print(json.dumps(message_body));
    return json.dumps(message_body)

# create_message_body(2136, 5)
'''
status: 1,//open=1,suspended=2,settled=3，其他的都报错
'''