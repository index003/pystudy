from db_operation import db_crud





def query_market_option_odds(match_id, market_id, currency):
    sql_query = ("select final_odds from sport_market_option_launch "
                 f"where match_id = {match_id} and "
                 f"market_id = {market_id} and "
                 f"currency = '{currency}'")
    query_result = db_crud.get_lottery_db().query_execute(sql_query)
    return query_result


def get_odds_list(match_id, market_id, currency):
    query_reult = query_market_option_odds(match_id, market_id, currency)
    odds_list = []
    for item in query_reult:
        odds_list.append(float(item[0]))
    return odds_list
