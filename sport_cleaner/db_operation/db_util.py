import pymysql
from db_operation import config_db_list

# 初始化数据库为fat3
env = 3


# 连接数据库
def get_db_connect():
    connections = pymysql.connect(**config_db_list.base_info[env - 1])
    return connections


# 增删改数据
def modify_execute(sql):
    connection = get_db_connect()
    cursor = connection.cursor()
    print(sql)
    cursor.execute(sql)
    connection.commit()
    print(f"Affected rows: {cursor.rowcount}")
    cursor.close()
    connection.close()


# 批量增删改
def modify_execute_list(sqls):
    connection = get_db_connect()
    cursor = connection.cursor()
    for sql in sqls:
        cursor.execute(sql)
        connection.commit()
        print(f"Affected rows: {cursor.rowcount}")
    cursor.close()
    connection.close()


# 查询数据
def query_execute(sql):
    connection = get_db_connect()
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result
