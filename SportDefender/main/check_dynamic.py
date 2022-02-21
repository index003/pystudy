from task.odds import dynamic
from common.data import sport_data_interface
from common.utils import price_currency
from common.utils import std_out
from common.config import env_config

env_config.env = "fat2"


# 显示赛事所有market_id
def show_match_market_info(match_id):
    match_market_info = sport_data_interface.get_market_info_by_id(match_id)
    std_out.format_output(match_market_info)


# 计算不同币种的美元价值
def ex_to_dollar(amount, currency):
    return price_currency.exchange_to_dollar(amount, currency)


# 计算某个玩法的动态赔付的结果
def check_dynamic_run(odds, bet_amount, k, match_id, market_id, currency):
    currency = currency.upper()
    odds_list = sport_data_interface.get_odds_list(match_id, market_id, currency)
    if odds_list:
        std_out.format_output(odds_list)
    new_odds = dynamic.get_dynamic_odds(odds, bet_amount, k, odds_list)
    std_out.format_output(new_odds)


# 计算2项盘的动态赔付结果
def check_dynamic_two_handicap_run(home_odds, bet_amount, k, away_odds):
    odds_list = [home_odds, away_odds]
    std_out.format_output(odds_list)
    new_odds = dynamic.get_dynamic_odds(home_odds, bet_amount, k, odds_list)
    std_out.format_output(new_odds)


# 计算有限的动态赔付结果，即将赔率放进来
def check_dynamic_other_handicap_run(home_odds, bet_amount, k, other_odds_list):
    odds_list = [home_odds]
    for item in other_odds_list:
        odds_list.append(item)
    # odds_list = [home_odds, away_odds_a, away_odds_b]
    std_out.format_output(odds_list)
    new_odds = dynamic.get_dynamic_odds(home_odds, bet_amount, k, odds_list)
    std_out.format_output(new_odds)


show_match_market_info(1958)
# check_dynamic_run(1.98, ex_to_dollar(100, 'usdt'), 27000, 1958, 22046, 'USD')
# check_dynamic_two_handicap_run(3.33, ex_to_dollar(100, 'usdt'), 27000, 1.2)
# check_dynamic_other_handicap_run(1.65, ex_to_dollar(100, 'usdt'), 22000, [1.18, 1.16])
ex_to_dollar(0.53, 'bnb')
