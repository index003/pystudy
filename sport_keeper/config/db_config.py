from config import env_config


# lottery 数据库配置信息
lottery_info = {
    # fat1 数据库连接信息
    'fat1': {
        'host': '172.16.4.11',
        'port': 3306,
        'user': 'wuchangzheng',
        'passwd': 'JnbbSQj4kW6fLFDfZxlg',
        'db': 'sport-lottery',
        'charset': 'utf8'
    },
    # fat2 数据库连接信息
    'fat2': {
        'host': '172.16.4.21',
        'port': 3306,
        'user': 'wuchangzheng',
        'passwd': 'JnbbSQj4kW6fLFDfZxlg',
        'db': 'sport-lottery',
        'charset': 'utf8'
    },
    # fat3 数据库连接信息
    'fat3': {
        'host': '172.16.4.31',
        'port': 3306,
        'user': 'wuchangzheng',
        'passwd': 'JnbbSQj4kW6fLFDfZxlg',
        'db': 'sport-lottery',
        'charset': 'utf8'
    },
    # fat4 数据库连接信息
    'fat4': {
        'host': '172.16.4.41',
        'port': 3306,
        'user': 'wuchangzheng',
        'passwd': '4SowuxTVU5pcE0pjb0uM',
        'db': 'sport-lottery',
        'charset': 'utf8'
    },
    # game1 数据库连接信息
    'game1': {
        'host': '172.16.4.81',
        'port': 3306,
        'user': 'wuchangzheng',
        'passwd': 'JnbbSQj4kW6fLFDfZxlg',
        'db': 'sport-lottery',
        'charset': 'utf8'
    },
    # pre 数据库连接信息
    'pre': {
        'host': '172.16.4.41',
        'port': 3306,
        'user': 'test',
        'passwd': 'JnbbSQj4kW6fLFDfZxlg',
        'db': 'sport-lottery',
        'charset': 'utf8'
    }
}


def get_lottery_info():
    return lottery_info[env_config.env]


# data 数据库配置信息
data_info = {
    # fat1 数据库连接信息
    'fat1': {
        'host': '172.16.4.11',
        'port': 3306,
        'user': 'wuchangzheng',
        'passwd': 'JnbbSQj4kW6fLFDfZxlg',
        'db': 'sport-data',
        'charset': 'utf8'
    },
    # fat2 数据库连接信息
    'fat2': {
        'host': '172.16.4.21',
        'port': 3306,
        'user': 'wuchangzheng',
        'passwd': 'JnbbSQj4kW6fLFDfZxlg',
        'db': 'sport-data',
        'charset': 'utf8'
    },
    # fat3 数据库连接信息
    'fat3': {
        'host': '172.16.4.31',
        'port': 3306,
        'user': 'wuchangzheng',
        'passwd': 'JnbbSQj4kW6fLFDfZxlg',
        'db': 'sport-data',
        'charset': 'utf8'
    },
    # fat4 数据库连接信息
    'fat4': {
        'host': '172.16.4.41',
        'port': 3306,
        'user': 'wuchangzheng',
        'passwd': '4SowuxTVU5pcE0pjb0uM',
        'db': 'sport-data',
        'charset': 'utf8'
    },
    # game1 数据库连接信息
    'game1': {
        'host': '172.16.4.81',
        'port': 3306,
        'user': 'wuchangzheng',
        'passwd': 'JnbbSQj4kW6fLFDfZxlg',
        'db': 'sport-data',
        'charset': 'utf8'
    },
    # pre 数据库连接信息
    'pre': {
        'host': '172.16.4.41',
        'port': 3306,
        'user': 'test',
        'passwd': 'JnbbSQj4kW6fLFDfZxlg',
        'db': 'sport-data',
        'charset': 'utf8'
    }
}


def get_data_info():
    return data_info[env_config.env]
