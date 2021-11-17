

def format_float(float_num):
    format_num = str(float_num).split('.')[0] + '.' + str(float_num).split('.')[1][:12]
    return float(format_num)


# 初盘返还率
def initial_return_rate(odds_list):
    odds_reciprocals = 0
    for odds in odds_list:
        odds_reciprocal = 1 / odds
        odds_reciprocals = odds_reciprocals + odds_reciprocal
    r_rate = 1 / odds_reciprocals
    return format_float(r_rate)


# 初盘胜率
def initial_win_rate(odds_list):
    r_rate = initial_return_rate(odds_list)
    w_rate = []
    for odds in odds_list:
        w_rate_item = (odds, format_float(r_rate / odds))
        w_rate.append(w_rate_item)
    return w_rate


# 设定注量AK，BK……
def get_k_values(odds_list, k):
    k_values = []
    w_rates = initial_win_rate(odds_list)
    for w_rate in w_rates:
        k_value = (w_rate[0], format_float(w_rate[1] * k))
        k_values.append(k_value)
    return k_values


# 目标选项进注量 AK + T
def get_target_odds_total_amount(odds, bet_amount, k, odds_list):
    k_values = get_k_values(odds_list, k)
    for k_value in k_values:
        if k_value[0] == odds:
            target_odds_k_value = k_value[1]
            target_odds_total_amount = target_odds_k_value + bet_amount * (odds - 1)
    return format_float(target_odds_total_amount)


# 其他选项进注量 BK
def get_other_odds_total_amount(k, odds_list):
    other_odds_total_amounts = []
    k_values = get_k_values(odds_list, k)
    for k_value in k_values:
        # if k_value[0] != odds:
        #     other_odds_total_amount = k_value[1]
        #     other_odds_total_amounts.append(format_float(other_odds_total_amount))
        other_odds_total_amount = k_value[1]
        other_odds_total_amounts.append(format_float(other_odds_total_amount))
    return other_odds_total_amounts


# 所有选项进注量的和 AK + T + BK
def get_dynamic_all_amount(odds, k, bet_amount):
    dynamic_denominator = k + bet_amount * (odds - 1)
    return dynamic_denominator


def get_dynamic_odds(odds, bet_amount, k, odds_list):
    new_odds = []

    all_amount = get_dynamic_all_amount(odds, k, bet_amount)
    r_rate = initial_return_rate(odds_list)

    target_odds_total_amount = get_target_odds_total_amount(odds, bet_amount, k, odds_list)

    aat = format_float(target_odds_total_amount / all_amount)
    aat_odds = format_float(r_rate / aat)
    new_odds.append(aat_odds)

    other_odds_total_amounts = get_other_odds_total_amount(k, odds_list)
    for other_odds_total_amount in other_odds_total_amounts:
        bbt = format_float(other_odds_total_amount / all_amount)
        bbt_odds = format_float(r_rate / bbt)
        new_odds.append(bbt_odds)
    print(new_odds)



