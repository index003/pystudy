from common.data.query_core import db_base
from common.data import sport_data_sql
from common.utils import std_out


def get_order_id_by_id(match_id):
    order_info = sport_data_sql.query_order_by_id(match_id)
    order_ids = std_out.format_sql_result(order_info, [1])
    return order_ids


def delete_order_option_by_id(order_id):
    sql_query = f"delete from sport_betting_order_option where order_id in {order_id}"
    db_base.get_lottery_db().modify_execute(sql_query)


def delete_order_by_id(order_id):
    sql_query = f"delete from sport_betting_order where id in {order_id}"
    db_base.get_lottery_db().modify_execute(sql_query)
