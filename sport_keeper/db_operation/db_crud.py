import pymysql
from config import db_config
from config import env_config


# 连接数据库
def get_db_connect():
    connections = pymysql.connect(**db_config.db_info[env_config.env])
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
def query_execute(sql, *params):
    connection = get_db_connect()
    cursor = connection.cursor()
    cursor.execute(sql, [*params])
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result
