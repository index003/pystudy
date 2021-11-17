from dynamic import dynamic_formula
from db_operation import dynamic_basic_data
from config import env_config

env_config.env = "fat2"


def check_dynamic_run(odds, bet_amount, k, match_id, market_id, currency):
    odds_list = dynamic_basic_data.get_odds_list(match_id, market_id, currency)
    dynamic_formula.get_dynamic_odds(odds, bet_amount, k, odds_list)


check_dynamic_run(3.48, 200, 10000, 1626, 18902, 'USD')
