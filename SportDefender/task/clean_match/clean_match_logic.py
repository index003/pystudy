import os
from common.data.query_core import db_base
from common.data import clean_match_data

current_path = os.path.dirname(__file__)


# 删除单个赛事
def clean_match(match_id):
    clean_match_list([match_id])


# 删除多个赛事
def clean_match_list(match_ids):
    if not match_ids:
        return
    with open(current_path + './clean_match.sql', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for match_id in match_ids:
            for sql in lines:
                sql_r = sql.format(match_id)
                db_base.get_lottery_db().modify_execute(sql_r)
            clean_match_order(match_id)


# 删除赛事订单
def clean_match_order(match_id):
    # 删除订单单独处理
    order_id_list = clean_match_data.get_order_id_by_id(match_id)
    # 判断是否有订单，有就删除，没有就不用处理了
    if order_id_list:
        if len(order_id_list) == 1:
            delete_id = f"({order_id_list[0]})"
        else:
            # 将list变成元组
            delete_id = tuple(order_id_list)

        clean_match_data.delete_order_option_by_id(delete_id)
        clean_match_data.delete_order_by_id(delete_id)
    else:
        print(f"No orders of this match （id = {match_id}）")
