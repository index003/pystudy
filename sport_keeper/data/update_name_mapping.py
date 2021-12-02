import sys

import db_utils


def insert_function(origin_name, std_name, source):
    sql_insert = ('INSERT INTO sport_player_name_mapping '
                  '(league_name, category_code, origin_name, name,source, is_deleted)'
                  f' VALUES ("NBA", "BASKETBALL", "{origin_name}", "{std_name}", "{source}",0)')
    db_utils.get_score_db().modify_execute(sql_insert)


def update_mapping(source_id):
    if source_id == 1:
        source_info = ["espn", "ESPN"]
    elif source_id == 2:
        source_info = ["hupu", "HUPU"]
    elif source_id == 3:
        source_info = ["skysports", "SKYSPORTS"]
    else:
        print("the source is not exist, please check it!")
        sys.exit()
    file_source = f'./{source_info[0]}.txt'
    source = source_info[1]

    with open(file_source, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for item in lines:
            item_list = item.split('+')
            std_name = item_list[0]
            origin_name = item_list[1].replace("\n", "")
            insert_function(origin_name, std_name, source)


# source_id: 1 espn 2 hupu 3 skysports
update_mapping(4)
