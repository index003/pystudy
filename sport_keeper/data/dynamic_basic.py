import json
from data import db_utils


def query_market_option_odds(match_id, market_id, currency):
    sql_query = ("select final_odds from sport_market_option_launch "
                 f"where match_id = {match_id} and "
                 f"market_id = {market_id} and "
                 f"currency = '{currency}' and "
                 f"available = 1")
    query_result = db_utils.get_lottery_db().query_execute(sql_query)
    return query_result


def get_odds_list(match_id, market_id, currency):
    query_reult = query_market_option_odds(match_id, market_id, currency)
    odds_list = []
    for item in query_reult:
        odds_list.append(float(item[0]))
    return odds_list


def query_market_id_by_id(match_id):
    sql_query = ("select id,names from sport_betting_market "
                 f"where match_id = {match_id}")
    query_result = db_utils.get_lottery_db().query_execute(sql_query)
    return query_result


def get_market_info_by_id(match_id):
    query_result = query_market_id_by_id(match_id)
    market_info = []
    for item in query_result:
        market_info.append(item[0])
        market_info.append(json.loads(item[1])['zh-Hans'])
    return market_info
