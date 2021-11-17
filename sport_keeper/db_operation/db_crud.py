import pymysql
from config import db_config


class DatabaseRepository(object):

    def __init__(self, conn_info):
        self.conn_info = conn_info

    # 连接数据库
    def get_db_connect(self):
        connections = pymysql.connect(**self.conn_info)
        return connections

    # 增删改数据
    def modify_execute(self, sql):
        connection = self.get_db_connect()
        cursor = connection.cursor()
        print(sql)
        cursor.execute(sql)
        connection.commit()
        print(f"Affected rows: {cursor.rowcount}")
        cursor.close()
        connection.close()

    # 批量增删改
    def modify_execute_list(self, sqls):
        connection = self.get_db_connect()
        cursor = connection.cursor()
        for sql in sqls:
            cursor.execute(sql)
            connection.commit()
            print(f"Affected rows: {cursor.rowcount}")
        cursor.close()
        connection.close()

    # 查询数据
    def query_execute(self, sql, *params):
        connection = self.get_db_connect()
        cursor = connection.cursor()
        cursor.execute(sql, [*params])
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        return result


def get_lottery_db():
    return DatabaseRepository(db_config.get_lottery_info())


def get_data_db():
    return DatabaseRepository(db_config.get_data_info())
