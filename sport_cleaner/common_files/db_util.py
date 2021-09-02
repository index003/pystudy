import pymysql

# 初始化数据库为fat3
env = 3


# 连接数据库
def get_db_connect():
    if env == 1:
        connections = pymysql.connect(
            host='172.16.4.11',
            port=3306,
            user='wuchangzheng',
            passwd='JnbbSQj4kW6fLFDfZxlg',
            db='sport-lottery',
            charset='utf8'
        )
    elif env == 2:
        connections = pymysql.connect(
            host='172.16.4.21',
            port=3306,
            user='wuchangzheng',
            passwd='JnbbSQj4kW6fLFDfZxlg',
            db='sport-lottery',
            charset='utf8'
        )
    elif env == 3:
        connections = pymysql.connect(
            host='172.16.4.31',
            port=3306,
            user='wuchangzheng',
            passwd='JnbbSQj4kW6fLFDfZxlg',
            db='sport-lottery',
            charset='utf8'
        )
    elif env == 4:
        connections = pymysql.connect(
            host='172.16.4.41',
            port=3306,
            user='wuchangzheng',
            passwd='4SowuxTVU5pcE0pjb0uM',
            db='sport-lottery',
            charset='utf8'
        )
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
