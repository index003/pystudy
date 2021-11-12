import json
import time
from collections import namedtuple
from rocket_mq.mq_basic_data import query_match_info_by_id, query_match_market_option_by_id


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
    fixture_id = query_match_info_by_id(match_id)
    query_result = query_match_market_option_by_id(fixture_id, market_id)
    bets_body = []
    for item in query_result:
        bet_msg = BetsMsg(0, *item, current_millis)
        bet_body = str(bet_msg._asdict()).replace("'", '"')
        bets_body.append(eval(bet_body))

    return bets_body


def create_message_body(match_id, market_id):
    bets = create_messages_markets_bets(match_id, market_id)
    source_match_id = query_match_info_by_id(match_id)
    fixtureId = source_match_id[0][0]
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
    return json.dumps(message_body)


'''
status: 1,//open=1,suspended=2,settled=3，其他的都报错
'''