import db_util


def clean_match(match_id):
    clean_match_list([match_id])


def clean_match_list(match_ids):
    with open('clean_match.sql', 'r', encoding='utf-8') as f:
        for match_id in match_ids:
            lines = f.readlines()
            for sql in lines:
                sql_r = sql.format(match_id)
                db_util.modify_execute(sql_r)
