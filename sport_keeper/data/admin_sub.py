from itertools import chain
from data import db_utils


def get_subscription_league(category_id):
    sql = f"select id from sport_league_info where category_id={category_id} and available=0"
    league_ids = db_utils.get_lottery_db().query_execute(sql)
    league_id_list = list(chain.from_iterable(league_ids))
    return league_id_list


