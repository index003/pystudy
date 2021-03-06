from common.config import env_config


# db 数据库配置信息
def db_base_info(env, db):
    db_info = {
        # fat1 数据库连接信息
        'fat1': {
            'host': '172.16.4.11',
            'port': 3306,
            'user': 'wuchangzheng',
            'passwd': 'JnbbSQj4kW6fLFDfZxlg',
            'db': db,
            'charset': 'utf8'
        },
        # fat2 数据库连接信息
        'fat2': {
            'host': '172.16.4.21',
            'port': 3306,
            'user': 'wuchangzheng',
            'passwd': 'JnbbSQj4kW6fLFDfZxlg',
            'db': db,
            'charset': 'utf8'
        },
        # fat3 数据库连接信息
        'fat3': {
            'host': '172.16.4.31',
            'port': 3306,
            'user': 'wuchangzheng',
            'passwd': 'JnbbSQj4kW6fLFDfZxlg',
            'db': db,
            'charset': 'utf8'
        },
        # fat4 数据库连接信息
        'fat4': {
            'host': '172.16.4.41',
            'port': 3306,
            'user': 'wuchangzheng',
            'passwd': '4SowuxTVU5pcE0pjb0uM',
            'db': db,
            'charset': 'utf8'
        },
        # game1 数据库连接信息
        'game1': {
            'host': '172.16.4.81',
            'port': 3306,
            'user': 'wuchangzheng',
            'passwd': 'JnbbSQj4kW6fLFDfZxlg',
            'db': db,
            'charset': 'utf8'
        },
        # pre 数据库连接信息
        'pre': {
            'host': '172.16.4.41',
            'port': 3306,
            'user': 'test',
            'passwd': 'JnbbSQj4kW6fLFDfZxlg',
            'db': db,
            'charset': 'utf8'
        }
    }
    return db_info[env]


def get_lottery_info():
    sport_lottery_db = db_base_info(env_config.env, 'sport-lottery')
    return sport_lottery_db


def get_data_info():
    sport_data_db = db_base_info(env_config.env, 'sport-data')
    return sport_data_db


def get_platform_info():
    platform_db = db_base_info(env_config.env, 'db_platform')
    return platform_db


def get_score_info():
    score_db = db_base_info(env_config.env, 'sport_score')
    return score_db

