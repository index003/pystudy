import requests
import json
from config import env_config
from config import api_config
from admin_operation import admin_login

env = env_config.env


def get_list(env, award_status):
    api_domain = api_config.get_apidomain(env)
    path = api_config.settlement_path + award_status
    url = api_domain + path
    print(url)
    authorization = admin_login.admin_login(env)
    headers = {
        "content-Type": "application/json;charset=UTF-8",
        "authorization": authorization
    }
    response = requests.get(url, headers=headers)
    response_dict = json.loads(response.text)
    data_list = response_dict['data']
    print(f"Total is: {data_list['total']}")

    # 将列表中所有的赛事都取到
    path = api_config.settlement_path + award_status
    # path_all = f"/lottery/settlements?pageSize={data_list['total']}&pageNum=1&awardStatus=FIRST_CHECK"
    url_all = api_domain + path
    response_all = requests.get(url_all, headers=headers)
    response_dict_all = json.loads(response_all.text)
    data_list_all = response_dict_all['data']
    match_list = data_list_all['list']
    match_ids = []
    for match in match_list:
        match_id = match['matchId']
        match_ids.append(match_id)
    print(match_ids)
    return match_ids
