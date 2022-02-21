from common.data import sport_data_sql
from common.utils import std_out
from common.utils import upper_lower


# 将某种币的指定金额转换成等价的美元价值
def exchange_to_dollar(amount, currency):
    currency = upper_lower.switch_to_upper(currency)
    dollar_value = 0
    currency_price_info = sport_data_sql.query_price_currency_info()
    currency_info = std_out.format_sql_result(currency_price_info, [1, 2])
    for item in currency_info:
        if item[0] == currency:
            dollar_value = float(item[1])*amount
    return dollar_value


# 将某种币的指定金额转换成等价的usdt价值
def exchange_to_usdt(amount, currency):
    currency = upper_lower.switch_to_upper(currency)
    usdt_value = 0
    currency_price_info = sport_data_sql.query_price_currency_info()
    currency_info = std_out.format_sql_result(currency_price_info, [1, 6])
    for item in currency_info:
        if item[0] == currency:
            usdt_value = float(item[1])*amount
    return usdt_value
