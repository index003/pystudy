from dynamic import dynamic_odds
from data import dynamic_basic
from data import price_currency
from config import env_config

env_config.env = "fat1"


# 格式化输出
def format_output(some_list):
    for i in range(len(some_list)):
        print(some_list[i], end=' | ')
        if(i+1) % 10 == 0:
            print("\n")
    print("\n")
    print("=====================================")


# 显示赛事所有market_id
def show_match_market_info(match_id):
    market_info = dynamic_basic.get_market_info_by_id(match_id)
    format_output(market_info)


# 计算不同币种的美元价值
def ex_to_dollar(amount, currency):
    currency = currency.upper()
    amount_usd_value = price_currency.exchange_to_dollar(amount, currency)
    print(amount_usd_value)
    return amount_usd_value


# 计算某个玩法的动态赔付的结果
def check_dynamic_run(odds, bet_amount, k, match_id, market_id, currency):
    currency = currency.upper()
    odds_list = dynamic_basic.get_odds_list(match_id, market_id, currency)
    if odds_list:
        format_output(odds_list)
    new_odds = dynamic_odds.get_dynamic_odds(odds, bet_amount, k, odds_list)
    format_output(new_odds)


# 计算2项盘的动态赔付结果
def check_dynamic_two_handicap_run(home_odds, bet_amount, k, away_odds):
    odds_list = [home_odds, away_odds]
    format_output(odds_list)
    new_odds = dynamic_odds.get_dynamic_odds(home_odds, bet_amount, k, odds_list)
    format_output(new_odds)


# 计算有限的动态赔付结果，即将赔率放进来
def check_dynamic_other_handicap_run(home_odds, bet_amount, k, other_odds_list):
    odds_list = [home_odds]
    for item in other_odds_list:
        odds_list.append(item)
    # odds_list = [home_odds, away_odds_a, away_odds_b]
    format_output(odds_list)
    new_odds = dynamic_odds.get_dynamic_odds(home_odds, bet_amount, k, odds_list)
    format_output(new_odds)


# show_match_market_info(1628)
# check_dynamic_run(1.65, ex_to_dollar(100, 'usdt'), 27000, 1628, 18939, 'USD')
# check_dynamic_two_handicap_run(1.77, ex_to_dollar(100, 'usdt'), 3500, 1.75)
# check_dynamic_two_handicap_run(1.77, 100, 3500, 1.75)
# check_dynamic_other_handicap_run(1.65, ex_to_dollar(100, 'usdt'), 22000, [1.18, 1.16])
ex_to_dollar(600, 'doge')
