import json

from common.data import sport_data_sql
from common.utils import std_out


# 返回赛事相关信息
def get_match_info_by_id(match_id, info):
    match_info = sport_data_sql.query_match_info_by_id(match_id)
    if info == 'fixture_id':
        fixtureId = std_out.format_sql_result(match_info, [10])
        return fixtureId[0]
    elif info == 'category_id':
        category_id = std_out.format_sql_result(match_info, [1])
        return category_id[0]
    elif info == 'league_id':
        league_id = std_out.format_sql_result(match_info, [2])
        return league_id[0]
    elif info == 'match_time':
        match_time = std_out.format_sql_result(match_info, [11])
        return str(match_time[0])
    elif info == 'team_id':
        team_ids_result = std_out.format_sql_result(match_info, [7, 8])
        team_ids = team_ids_result[0]
        return team_ids
    else:
        print("get_match_info_by_id Wrong")


# 返回category_code
def get_category_info_by_id(match_id, info):
    category_id = get_match_info_by_id(match_id, 'category_id')
    category_info = sport_data_sql.query_category_info_by_id(category_id)
    if info == 'category_code':
        category_code = std_out.format_sql_result(category_info, [2])
        return category_code[0]
    elif info == 'source_category_id':
        source_category_id = std_out.format_sql_result(category_info, [4])
        return source_category_id[0]
    else:
        print("get_category_info_by_id Wrong")


# 根据league_id获取联赛的源id
def get_league_source_id_by_id(match_id):
    league_id = get_match_info_by_id(match_id, 'league_id')
    league_info = sport_data_sql.query_league_info_by_league_id(league_id)
    source_league_id = std_out.format_sql_result(league_info, [6])
    return source_league_id[0]


def get_team_info_by_id(match_id, info):
    team_ids = get_match_info_by_id(match_id, 'team_id')
    print(team_ids)
    if info == 'team_name':
        team_en_name = []
        for team_id in team_ids:
            team_names_info = sport_data_sql.query_team_info_by_id(team_id)
            team_name = std_out.format_sql_result(team_names_info, [4])
            team_en_name.append(team_name[0])
        return team_en_name
    elif info == 'source_team_id':
        source_team_ids = []
        for team_id in team_ids:
            source_team_info = sport_data_sql.query_team_source_info_by_id(team_id)
            source_team_id = std_out.format_sql_result(source_team_info, [7])
            source_team_ids.append(source_team_id[0])
        print(source_team_ids)
        return source_team_ids
    else:
        print("get_team_info_by_id WRONG")


# 返回指定赛事的联赛的英文名称
def get_league_en_name_by_id(match_id):
    league_id = get_match_info_by_id(match_id, 'league_id')
    league_en_name_info = sport_data_sql.query_league_en_names_by_id(league_id)
    league_en_name = std_out.format_sql_result(league_en_name_info, [4])
    return league_en_name[0]


# 返回指定赛事所有的market_id
def get_whole_match_markets(match_id):
    fixture_id = get_match_info_by_id(match_id, 'fixture_id')
    market_bet_info = sport_data_sql.query_whole_markets_by_id(fixture_id)
    markets = list(set(std_out.format_sql_result(market_bet_info, [2])))
    return markets


# 拼接赔率bets域的数据
def get_match_market_option_by_id(fixture_id, market_id):
    market_option_info = sport_data_sql.query_match_market_option_by_id(fixture_id, market_id)
    market_option = std_out.format_sql_result(market_option_info, [7, 8, 9, 10, 11, 12])
    format_option = std_out.format_decimal(market_option)
    return format_option


# 获取篮球球员玩法的market_code
def get_basketball_player_market_code():
    source_market_id = (1069, 1070, 1071, 1072, 1073, 1074, 1075)
    market_info = sport_data_sql.query_basketball_player_market_code_by_id(source_market_id)
    market_code = std_out.format_sql_result(market_info, [1])
    return market_code


# 获取赛事篮球玩法的球员名称
def get_match_basketball_player_name(match_id):
    player_market_code = tuple(get_basketball_player_market_code())
    match_player_info = sport_data_sql.query_match_player_by_market_code(match_id, player_market_code)
    if match_player_info:
        match_player = list(set(std_out.format_sql_result(match_player_info, 6)))
    else:
        print(f"there is not player market in the match {match_id}")
    return match_player


def get_odds_list(match_id, market_id, currency):
    option_info = sport_data_sql.query_market_option_launch(match_id, market_id, currency)
    odds_info = std_out.format_sql_result(option_info, [9])
    final_odds = std_out.format_decimal(odds_info)
    return final_odds


def get_market_info_by_id(match_id):
    market_info = sport_data_sql.query_betting_market_by_id(match_id)
    market_id_name = std_out.format_sql_result(market_info, [0, 3])
    market_list = []
    for item in market_id_name:
        market_list.append(item[0])
        market_list.append(json.loads(item[1])['zh-Hans'])
    return market_list
