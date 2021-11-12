from db_operation import db_crud


def query_match_info_by_id(match_id):
    sql_query = "select source_match_id,category_id from sport_match_info where id = %s"
    query_result = db_crud.get_lottery_db().query_execute(sql_query, match_id)
    return query_result


def get_fixture_id_by_id(match_id):
    source_match_id = query_match_info_by_id(match_id)
    fixtureId = source_match_id[0][0]
    return fixtureId


def get_category_id_by_id(match_id):
    source_match_id = query_match_info_by_id(match_id)
    category_id = source_match_id[0][1]
    return category_id


def query_whole_markets_by_id(match_id):
    source_match_id = query_match_info_by_id(match_id)
    fixture_id = source_match_id[0][0]
    sql_query = ("select distinct market_id from ds_sport_market_bet_info "
                 f"where fixture_id = {fixture_id} and provider_id = 8")
    query_result = db_crud.get_data_db().query_execute(sql_query)
    return query_result


def query_match_market_option_by_id(fixture_id, market_id):
    sql_query = ("select bet_name, IFNULL(line,''), IFNULL(base_line,''), status, "
                 "CAST(start_price as CHAR) as start_price,"
                 "CAST(price as CHAR) as price "
                 "from ds_sport_market_bet_info where provider_id = 8 and fixture_id = %s and market_id = %s")
    query_result = db_crud.get_data_db().query_execute(sql_query, fixture_id, market_id)
    return query_result


def query_match_status_fields_by_id(match_id):
    msg_query = ("select c.source_category_id,a.league_id,a.source_match_id as fixtureID,"
                 "a.home_team_id,a.away_team_id from sport_match_info a "
                 "LEFT JOIN sport_league_info b ON a.league_id=b.id "
                 "LEFT JOIN sport_category_info c on a.category_id = c.id where a.id= %s")

    query_result = db_crud.get_lottery_db().query_execute(msg_query, match_id)
    return query_result

