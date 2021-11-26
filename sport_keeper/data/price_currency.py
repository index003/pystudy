from data import db_utils


# 获取币种价格信息
def query_price_currency_info():
    query_sql = "select currency, dollar, usdt from price_currency"
    query_result = db_utils.get_platform_db().query_execute(query_sql)
    return query_result


# 将某种币的指定金额转换成等价的美元价值
def exchange_to_dollar(amount, currency):
    dollar_value = 0
    all_currency_price_info = query_price_currency_info()
    for item in all_currency_price_info:
        if item[0] == currency:
            dollar_value = float(item[1])*amount
    return dollar_value

