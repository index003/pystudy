import pymysql
from config import db_config
from config import env_config

env = env_config.env


# 连接数据库
def get_db_connect(env):
    connections = pymysql.connect(**db_config.db_info[env])
    return connections


# 增删改数据
def modify_execute(env, sql):
    connection = get_db_connect(env)
    cursor = connection.cursor()
    print(sql)
    cursor.execute(sql)
    connection.commit()
    print(f"Affected rows: {cursor.rowcount}")
    cursor.close()
    connection.close()


# 批量增删改
def modify_execute_list(env, sqls):
    connection = get_db_connect(env)
    cursor = connection.cursor()
    for sql in sqls:
        cursor.execute(sql)
        connection.commit()
        print(f"Affected rows: {cursor.rowcount}")
    cursor.close()
    connection.close()


# 查询数据
def query_execute(env, sql):
    connection = get_db_connect(env)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result
