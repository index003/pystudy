from itertools import chain
from db_operation import db_util

db_util.env = 3

sql_order_id = f"select order_id from sport_betting_order_option where match_id = 308"
order_id = db_util.query_execute(sql_order_id)
print(order_id)
list_a = list(chain.from_iterable(order_id))
print(list_a)
if len(list_a) == 1:
    id1 = f"({list_a[0]})"
    print(id1)
else:
    tuple_a = tuple(list(chain.from_iterable(order_id)))
    print(tuple_a)
