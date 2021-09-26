import time
from itertools import chain
from db_operation import db_crud
from config import env_config

env_config.env = 'fat2'


def match_odds_1x2_msg(match_id, status):
    message_body = {
        "fixtureId": 7139139,
        "source": "LSPORTS",
        "markets": [
            {
                "id": 1,
                "names": {},
                "bets": [
                    {
                        "id": 0,
                        "name": "1",
                        "line": "",
                        "baseLine": "",
                        "status": 1,
                        "startPrice": "",
                        "price": "1.12",
                        "lastUpdateTime": "1628066034000"
                    },
                    {
                        "id": 0,
                        "name": "X",
                        "line": "",
                        "baseLine": "",
                        "status": 1,
                        "startPrice": "",
                        "price": "10.3",
                        "lastUpdateTime": "1628066034000"
                    },
                    {
                        "id": 0,
                        "name": "2",
                        "line": "",
                        "baseLine": "",
                        "status": 1,
                        "startPrice": "",
                        "price": "15.6",
                        "lastUpdateTime": "1628066034000"
                    }
                ]
            }
        ],
        "updateType": "ODDS"
    }

    sql = f"select source_match_id from sport_match_info where id = %s"
    query_result = db_crud.query_execute(sql, match_id)
    query_result_value = list(chain.from_iterable(query_result))
    fixture_id = query_result_value[0]
    current_millis = int(time.time() * 1000)

    message_body['fixtureId'] = fixture_id
    for bet in range(3):
        message_body['markets'][0]['bets'][bet]['status'] = status
        message_body['markets'][0]['bets'][bet]['lastUpdateTime'] = current_millis
    print(message_body)


match_odds_1x2_msg(1399, 2)

