from common.data import sport_data_sql
from common.utils import std_out


def get_subscription_league(category_id):
    leagues = sport_data_sql.query_league_info_by_category_id(category_id)
    return std_out(leagues, [0])
