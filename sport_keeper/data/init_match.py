import sys
from data import db_utils
from config import env_config

env_config.env = 'fat2'


def query_source_category_by_id(category_id):
    query_sql = "select * from sport_category_info where id = %s"
    query_result = db_utils.get_lottery_db().query_execute(query_sql, category_id)
    if query_result:
        return query_result
    else:
        print("the result is null")
        sys.exit()


def query_category_market_info_by_id(source_category_id):
    query_sql = "select * from sport_market_config where source_category_id = %s"
    query_result = db_utils.get_lottery_db().query_execute(query_sql, source_category_id)
    return query_result


def query_market_option_config_info(market_code_list):
    query_sql = "select * from sport_market_option_config where market_code in %s"
    query_result = db_utils.get_lottery_db().query_execute(query_sql, market_code_list)
    return query_result


def get_source_category_id(category_id):
    source_category = query_source_category_by_id(category_id)
    source_category_id = source_category[0][4]
    return source_category_id


def get_category_market_code(category_id):
    source_category_id = get_source_category_id(category_id)
    category_market_info = query_category_market_info_by_id(source_category_id)
    category_market_code = []
    for item in category_market_info:
        category_market_code.append(item[1])
    return category_market_code


def get_market_option_config_info(category_id):
    market_code_list = get_category_market_code(category_id)
    market_option_config_info = query_market_option_config_info(market_code_list)
    print(market_option_config_info)
    return market_option_config_info


get_market_option_config_info(8)

