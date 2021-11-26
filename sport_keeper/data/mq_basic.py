import json
from data import db_utils


# mq脚本用到的数据
# 根据match_id查询source_match_id,category_id
def query_match_info_by_id(match_id):
    sql_query = ("select source_match_id,"
                 "category_id, match_time, "
                 "home_team_id, "
                 "away_team_id "
                 "from sport_match_info where id = %s")
    query_result = db_utils.get_lottery_db().query_execute(sql_query, match_id)
    return query_result


# 根据team_id获得球队英文名称
def query_team_info_by_id(team_id):
    sql_query = "select * from sport_team_info where id =%s"
    query_result = db_utils.get_lottery_db().query_execute(sql_query, team_id)
    return query_result


# 返回所有的market_id
def query_whole_markets_by_id(match_id):
    source_match_id = query_match_info_by_id(match_id)
    fixture_id = source_match_id[0][0]
    sql_query = ("select distinct market_id from ds_sport_market_bet_info "
                 f"where fixture_id = {fixture_id} and provider_id = 8")
    query_result = db_utils.get_data_db().query_execute(sql_query)
    return query_result


# 拼接赔率bets域的数据
def query_match_market_option_by_id(fixture_id, market_id):
    sql_query = ("select bet_name, IFNULL(line,''), IFNULL(base_line,''), status, "
                 "CAST(start_price as CHAR) as start_price,"
                 "CAST(price as CHAR) as price "
                 "from ds_sport_market_bet_info where provider_id = 8 and fixture_id = %s and market_id = %s")
    query_result = db_utils.get_data_db().query_execute(sql_query, fixture_id, market_id)
    return query_result


# 拼接赛事状态域的数据
def query_match_status_fields_by_id(match_id):
    msg_query = ("select c.source_category_id,a.league_id,a.source_match_id as fixtureID,"
                 "a.home_team_id,a.away_team_id from sport_match_info a "
                 "LEFT JOIN sport_league_info b ON a.league_id=b.id "
                 "LEFT JOIN sport_category_info c on a.category_id = c.id where a.id= %s")

    query_result = db_utils.get_lottery_db().query_execute(msg_query, match_id)
    return query_result


# 获取篮球球员玩法的market_code
def query_basketball_player_market_code_by_id():
    source_market_id = (1069, 1070, 1071, 1072, 1073, 1074, 1075)
    sql_query = f"select market_code from sport_market_config where source_market_id in {source_market_id}"
    query_result = db_utils.get_lottery_db().query_execute(sql_query)
    return query_result


def query_match_player_by_market_code(match_id, market_code):
    sql_query = ("select extra_label from sport_betting_market_option "
                 "where match_id = %s and "
                 "market_code = %s and "
                 "label = 'UNDER'")
    query_result = db_utils.get_lottery_db().query_execute(sql_query, match_id, market_code)
    return query_result


def get_match_time(match_id):
    match_info = query_match_info_by_id(match_id)
    match_time = match_info[0][2]
    return match_time


def get_team_en_name(match_id):
    match_info = query_match_info_by_id(match_id)
    team_ids = [match_info[0][3], match_info[0][4]]
    team_en_name = []
    for team_id in team_ids:
        team_info = query_team_info_by_id(team_id)
        team_name = json.loads(team_info[0][1])
        team_en_name.append(team_name['en'])
    return team_en_name


# 返回fixtureId
def get_fixture_id_by_id(match_id):
    source_match_id = query_match_info_by_id(match_id)
    fixtureId = source_match_id[0][0]
    return fixtureId


# 返回category_id
def get_category_id_by_id(match_id):
    source_match_id = query_match_info_by_id(match_id)
    category_id = source_match_id[0][1]
    return category_id


def get_basketball_player_market_code():
    market_codes = query_basketball_player_market_code_by_id()
    player_market_codes = []
    for market_code in market_codes:
        player_market_codes.append(market_code[0])
    return player_market_codes


def get_match_basketball_player_name(match_id):
    player_market_code_list = get_basketball_player_market_code()
    match_player_list = []
    match_players = []
    for player_market_code in player_market_code_list:
        match_player_result = query_match_player_by_market_code(match_id, player_market_code)
        if match_player_result:
            match_players = match_player_result
            break
    if match_players:
        for match_player in match_players:
            slice_num = match_player[0].index('#') - 1
            match_player_list.append(match_player[0][:slice_num])
    else:
        print(f"there is not player market in the match {match_id}")

    return match_player_list


