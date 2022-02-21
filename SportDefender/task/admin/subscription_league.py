import requests
from task.admin import login
from common.config import api_config
from common.data import sub_league_data


# 订阅联赛
# 按类别订阅联赛
def subscription_league(category_id):
    token = login.admin_login()
    league_id_list = sub_league_data.get_subscription_league(category_id)

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


# 按联赛列表订阅
def subscription_league_id(league_id_list):
    token = login.admin_login()
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

