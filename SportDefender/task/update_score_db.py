from common.data.query_core import db_base


def update_score_db_name_mapping(origin_name, std_name, source):
    sql_insert = ('INSERT INTO sport_player_name_mapping '
                  '(league_name, category_code, origin_name, name,source, is_deleted)'
                  f' VALUES ("NBA", "BASKETBALL", "{origin_name}", "{std_name}", "{source}",0)')
    db_base.get_score_db().modify_execute(sql_insert)
