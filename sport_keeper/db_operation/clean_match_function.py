from itertools import chain
from db_operation import db_crud


def clean_match(env, match_id):
    clean_match_list(env, [match_id])


def clean_match_list(env, match_ids):
    if not match_ids:
        return
    with open('./db_operation/clean_match.sql', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for match_id in match_ids:
            for sql in lines:
                sql_r = sql.format(match_id)
                db_crud.modify_execute(env, sql_r)
            clean_match_order(env, match_id)


def clean_match_order(env, match_id):
    # 删除订单单独处理
    sql_order_id = f"select order_id from sport_betting_order_option where match_id = {match_id}"
    order_id = db_crud.query_execute(env, sql_order_id)
    # 判断是否有订单，有就删除，没有就不用处理了
    if order_id:
        # 将原始结果变成list
        order_id_list = list(chain.from_iterable(order_id))
        # 如果只有一个订单，直接从列表中取出来用
        if len(order_id_list) == 1:
            delete_id = f"({order_id_list[0]})"
        else:
            # 将list变成元组
            delete_id = tuple(order_id_list)

        sql_delete_option_order = f"delete from sport_betting_order_option where order_id in {delete_id}"
        db_crud.modify_execute(env, sql_delete_option_order)
        sql_delete_order = f"delete from sport_betting_order where id in {delete_id}"
        db_crud.modify_execute(env, sql_delete_order)
    else:
        print(f"No orders of this match （id = {match_id}）")
