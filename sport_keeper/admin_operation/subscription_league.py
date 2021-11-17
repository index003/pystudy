import requests
from itertools import chain
from admin_operation import admin_login
from db_operation import db_crud
from config import api_config


# 订阅联赛
def subscription_league(category_id):
    token = admin_login.admin_login()
    sql = f"select id from sport_league_info where category_id={category_id} and available=0"
    league_ids = db_crud.get_lottery_db().query_execute(sql)
    league_id_list = list(chain.from_iterable(league_ids))

    for league_id in league_id_list:
        print(league_id)
        url = api_config.get_subscription_url() + f'{league_id}'
        header = {
            'content-type': 'application/json',
            'authorization': token
        }
        data1 = {
            'grade': 'A',
            'location': 'INTERNATIONAL'
        }

        res = requests.patch(url, json=data1, headers=header)
        print(res.text)
        data2 = {
            'available': 'true'
        }
        res = requests.patch(url, json=data2, headers=header)
        print(res.text)


def subscription_league_id(league_id_list):
    token = admin_login.admin_login()
    for league_id in league_id_list:
        print(league_id)
        url = api_config.get_subscription_url() + f'{league_id}'
        header = {
            'content-type': 'application/json',
            'authorization': token
        }
        data1 = {
            'grade': 'A',
            'location': 'INTERNATIONAL'
        }

        res = requests.patch(url, json=data1, headers=header)
        print(res.text)
        data2 = {
            'available': 'true'
        }
        res = requests.patch(url, json=data2, headers=header)
        print(res.text)

