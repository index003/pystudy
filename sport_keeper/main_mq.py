import time
from collections import namedtuple
from itertools import chain
from db_operation import db_crud
from config import env_config

env_config.env = 'fat2'


def query_match_info_by_id(match_id):
    match_info_fields = [
        "match_id", "category_id", "source_match_id"
    ]
    MatchMsg = namedtuple('MatchMsg', match_info_fields)
    sql_query = "select id,category_id,source_match_id from sport_match_info where id = %s"
    query_result = db_crud.get_lottery_db().query_execute(sql_query, match_id)
    match_msg = MatchMsg(*query_result[0])
    message_body = str(match_msg._asdict()).replace("'", '"')
    print(message_body)
    return message_body


query_match_info_by_id(1539)


def query_category_info_by_id(category_id):
    category_info_fields = [
        "category_id", "source_category_id"
    ]
    MatchMsg = namedtuple('MatchMsg', category_info_fields)
    sql_query = 'select id,source_category_id from sport_category_info where id = %s'
    query_result = db_crud.get_lottery_db().query_execute(sql_query, category_id)
    match_msg = MatchMsg(*query_result[0])
    message_body = str(match_msg._asdict()).replace("'", '"')
    print(message_body)
    return message_body


query_category_info_by_id(8)


def query_market_config(source_category_id, source_market_id):
    market_info_fields = [
        "id", "source_category_id", "source_market_id", "market_code"
    ]
    MatchMsg = namedtuple('MatchMsg', market_info_fields)
    sql_query = ("select id,source_category_id,source_market_id,market_code "
                 "from sport_market_config where source_category_id=%s and source_market_id=%s")
    query_result = db_crud.get_lottery_db().query_execute(sql_query, source_category_id, source_market_id)
    match_msg = MatchMsg(*query_result[0])
    message_body = str(match_msg._asdict()).replace("'", '"')
    print(message_body)
    return message_body


query_market_config(6046, 1)


def query_betting_market(match_id, market_code):
    betting_market_info_fields = [
        "id", "match_id", "market_code"
    ]
    MatchMsg = namedtuple('MatchMsg', betting_market_info_fields)
    sql_query = ("select id,match_id,market_code "
                 "from sport_betting_market where match_id = %s and market_code=%s")
    query_result = db_crud.get_lottery_db().query_execute(sql_query, match_id, market_code)
    match_msg = MatchMsg(*query_result[0])
    message_body = str(match_msg._asdict()).replace("'", '"')
    print(message_body)
    return message_body


query_betting_market(1539, 'FOOTBALL_1_1X2')


def query_market_options_by_market_id(market_id):
    sql_query = "select id,names from sport_betting_market_option where market_id = %s"
    query_result = db_crud.get_lottery_db().query_execute(sql_query, market_id)
    query_result_list = list(chain.from_iterable(query_result))
    print(query_result_list)

    return [
        {
            "id": 25154,
            "match_id": 168,
            "market_id": 2827,
            "market_code": "FOOTBALL_1_1X2",
            "label": "HOME",
            "extra_label": "",
            "odds": 2.000,
            "status": "OPEN"
        },
        {
            "id": 25155,
            "match_id": 168,
            "market_id": 2827,
            "market_code": "FOOTBALL_1_1X2",
            "label": "DRAW",
            "extra_label": "",
            "odds": 3.600,
            "status": "OPEN"
        },
        {
            "id": 25156,
            "match_id": 168,
            "market_id": 2827,
            "market_code": "FOOTBALL_1_1X2",
            "label": "AWAY",
            "extra_label": "",
            "odds": 3.500,
            "status": "OPEN"
        }
    ]


query_market_options_by_market_id(17884)


def get_source_option_name(option_label):
    label_source_name_config = {
        "HOME": "1",
        "DRAW": "X",
        "AWAY": "2"
    }
    return label_source_name_config[option_label]


def get_source_option_status(option_status):
    status_source_status_config = {
        "OPEN": 1,
        "SUSPENDED": 2
    }
    return status_source_status_config[option_status]


def convert_option_to_bet(market_option):
    return {
        "id": 0,
        "name": get_source_option_name(market_option['label']),
        "line": market_option['extra_label'],
        "baseline": market_option['extra_label'],
        "status": get_source_option_status(market_option['status']),
        "price": market_option['odds'],
        "lastUpdateTime": int(time.time() * 1000)
    }


def build_market_update_message(match_id, source_market_id):
    """
    构造一条包含所有玩法选项的赔率更新消息
   :param match_id: 比赛id
   :param source_market_id: 数据方玩法id
   :return: 玩法赔率更新消息
   """
    result = {
        "source": "LSPORTS"
    }

    # 设置比赛信息
    match_info = query_match_info_by_id(match_id)
    result['fixtureId'] = match_info['source_match_id']

    # 设置玩法信息
    market_info = {
        "id": source_market_id,
        "name": {}
    }
    result['markets'] = [market_info]

    # 设置选项信息
    category_info = query_category_info_by_id(match_info['category_id'])
    market_config = query_market_config(category_info['source_category_id'], source_market_id)
    betting_market = query_betting_market(match_id, market_config['market_code'])
    market_options = query_market_options_by_market_id(betting_market['id'])
    bets = [convert_option_to_bet(option) for option in market_options]
    market_info['bets'] = bets

    return str(result).replace("'", '"')

# print(build_market_update_message(1, 1))

