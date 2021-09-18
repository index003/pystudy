import requests
from itertools import chain
from admin_operation import admin_login
from db_operation import db_crud
from config import env_config
from config import api_config


env = env_config.env


def subscription_league(env, category_id):
    api_domain = api_config.get_apidomain(env)
    token = admin_login.admin_login(env)
    sql = f"select id from sport_league_info where category_id={category_id} and available=0"
    league_ids = db_crud.query_execute(env, sql)
    league_id_list = list(chain.from_iterable(league_ids))

    for league_id in league_id_list:
        print(league_id)
        path = api_config.subscription_path + f"{league_id}"
        url = api_domain + path
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
