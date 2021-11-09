import time
from collections import namedtuple
from db_operation import db_crud
from config import env_config

env_config.env = 'fat2'


def query_match_info_by_id(match_id):
    match_info_fields = ["fixtureId", "source"]
    MatchMsg = namedtuple('MatchMsg', match_info_fields)
    sql_query = "select source_match_id,source from sport_match_info where id = %s"
    query_result = db_crud.get_lottery_db().query_execute(sql_query, match_id)
    match_msg = MatchMsg(*query_result[0])
    message_body = str(match_msg._asdict()).replace("'", '"')
    print(message_body)
    return message_body


query_match_info_by_id(1587)


def query_market_info_by_id(fixture_id, market_id):
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
    BetsMsg = namedtuple('MatchMsg', bets_fields)
    current_millis = int(time.time() * 1000)
    sql_query = ("select bet_name, line, base_line, status, "
                 "CAST(start_price as CHAR) as start_price,"
                 "CAST(price as CHAR) as price "
                 "from ds_sport_market_bet_info where provider_id = 8 and fixture_id = %s and market_id = %s")
    query_result = db_crud.get_data_db().query_execute(sql_query, fixture_id, market_id)
    print(query_result[0])
    bets_msg = BetsMsg(0, *query_result[0], current_millis)
    bets_body = str(bets_msg._asdict()).replace("'", '"')
    print(bets_body)


query_market_info_by_id(7740388, 2)

