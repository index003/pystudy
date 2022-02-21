from common.data.query_core import db_base


# 根据match_id查询指定赛事的信息
def query_match_info_by_id(match_id):
    sql_query = "select * from sport_match_info where id = %s"
    query_result = db_base.get_lottery_db().query_execute(sql_query, match_id)
    return query_result


# 根据category_id获取类别信息
def query_category_info_by_id(category_id):
    sql_query = "select * from sport_category_info where id = %s"
    query_result = db_base.get_lottery_db().query_execute(sql_query, category_id)
    return query_result


# 根据league_id获取联赛基础信息
def query_league_info_by_league_id(league_id):
    sql_query = "select * from sport_league_info where id = %s"
    query_result = db_base.get_lottery_db().query_execute(sql_query, league_id)
    return query_result


# 某个类别下的联赛数据
def query_league_info_by_category_id(category_id):
    sql = ("select * from sport_league_info "
           "where category_id = %s and available=0")
    league_ids = db_base.get_lottery_db().query_execute(sql, category_id)
    return league_ids


# 根据league_id获取联赛名称信息
def query_league_en_names_by_id(league_id):
    sql_query = ("select * from sport_i18n_info "
                 "where buss_id = %s and type = 2 and lang = 'en'")
    query_result = db_base.get_lottery_db().query_execute(sql_query, league_id)
    return query_result


# 根据team_id获得球队英文名称
def query_team_info_by_id(team_id):
    sql_query = ("select * from sport_i18n_info "
                 "where buss_id =%s and type = 3 and lang = 'en'")
    query_result = db_base.get_lottery_db().query_execute(sql_query, team_id)
    return query_result


# 根据team_id获得source_team_id
def query_team_source_info_by_id(team_id):
    sql_query = "select * from sport_team_info where id = %s"
    query_result = db_base.get_lottery_db().query_execute(sql_query, team_id)
    return query_result


# 返回指定赛事所有的market_id
def query_whole_markets_by_id(fixture_id):
    sql_query = ("select * from ds_sport_market_bet_info "
                 "where fixture_id = %s and provider_id = 145")
    query_result = db_base.get_data_db().query_execute(sql_query, fixture_id)
    return query_result


# 指定币种玩法选项的信息
def query_market_option_launch(match_id, market_id, currency):
    sql_query = ("select * from sport_market_option_launch "
                 "where match_id = %s and market_id = %s and "
                 "currency = %s and available = 1")
    query_result = db_base.get_lottery_db().query_execute(sql_query, match_id, market_id, currency)
    return query_result


# 指定赛事玩法信息
def query_betting_market_by_id(match_id):
    sql_query = "select * from sport_betting_market where match_id = %s"
    query_result = db_base.get_lottery_db().query_execute(sql_query, match_id)
    return query_result


# 拼接赔率bets域的数据
def query_match_market_option_by_id(fixture_id, market_id):
    sql_query = ("select * from ds_sport_market_bet_info "
                 "where provider_id = 145 and fixture_id = %s and market_id = %s")
    query_result = db_base.get_data_db().query_execute(sql_query, fixture_id, market_id)
    return query_result


# 某场赛事下的订单信息
def query_order_by_id(match_id):
    sql_query = "select * from sport_betting_order_option where match_id = %s"
    query_result = db_base.get_lottery_db().query_execute(sql_query, match_id)
    return query_result


# 获取篮球球员玩法的market_code
def query_basketball_player_market_code_by_id(source_market_id):
    sql_query = ("select * from sport_market_config "
                 "where source_market_id in %s")
    query_result = db_base.get_lottery_db().query_execute(sql_query, source_market_id)
    return query_result


# 根据球员玩法的market_code，获取赛事的球员信息
def query_match_player_by_market_code(match_id, market_code):
    sql_query = ("select * from sport_betting_market_option "
                 "where match_id = %s and market_code in %s and lable = 'UNDER'")
    query_result = db_base.get_lottery_db().query_execute(sql_query, match_id, market_code)
    return query_result


# 获取币种价格信息
def query_price_currency_info():
    query_sql = "select * from price_currency"
    query_result = db_base.get_platform_db().query_execute(query_sql)
    return query_result