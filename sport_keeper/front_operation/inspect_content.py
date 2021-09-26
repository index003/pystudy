import time

import requests
import json
from config import api_config


# 获取赛事首页类别菜单信息，返回类别的详细信息
def get_home_menus():
    url = api_config.get_home_menus_url()
    print(url)
    request_data = {
        'lang': 'zh-Hant',
        'type': 0,
        'launchType': 'CENTRALIZED'
    }
    response = requests.get(url, params=request_data)
    # 将字符串形式转换为json格式，字典类型
    response_dic = json.loads(response.text)
    return response_dic['data']


# 获取类别信息的category id,列表形式，不包括自定赛事
def get_home_menus_category_id(data):
    category_list = []
    for category in data:
        if category['count'] != 0 and category['categoryId'] not in [8, 212, 213, 214]:
            category_list.append(category['categoryId'])
    print(category_list)
    return category_list


# 展示赛事首页类别菜单信息
def show_home_menus_result(data):
    for menu_data in data:
        if menu_data['count'] != 0:
            print(f"'categoryId' = {menu_data['categoryId']}")
            print(f"'categoryCode' = {menu_data['categoryCode']}")
            print(f"'categoryName' = {menu_data['categoryName']}")
            print(f"'count' = {menu_data['count']}")
            print(f"'sportType = {menu_data['sportType']}")


# 查询类别下所有的赛事
def get_home_category_all_match(category_id):
    print("category_id", category_id)
    url = api_config.get_home_category_url()
    request_data = {
        'type': 0,
        'subType': 0,
        'categoryId': category_id,
        'lang': 'zh-Hans',
        'launchType': 'CENTRALIZED'
    }
    response = requests.get(url, params=request_data)
    # 将字符串形式转换为json格式，字典类型
    response_dic = json.loads(response.text)
    match_ids = []
    for object_data in response_dic['data']:
        leaguage_info_list = object_data['leagueInfoList']
        for leaguage_info in leaguage_info_list:
            match_info_list = leaguage_info['matchInfoList']
            for match_info in match_info_list:
                match_ids.append(match_info['id'])
    return match_ids


def get_match_detail(match_id):
    url = api_config.get_match_detail_url() + f"{match_id}"
    request_data = {
        'lang': 'zh-Hant',
        'launchType': 'CENTRALIZED'
    }
    response = requests.get(url, params=request_data)
    # 将字符串形式转换为json格式，字典类型
    response_dic = json.loads(response.text)
    rspCode = response_dic['rspCode']
    if rspCode == "0000":
        print(f"{match_id} pass")
    else:
        print(f"{match_id} {rspCode}")


def get_category_ids():
    menu_list = get_home_menus()
    return get_home_menus_category_id(menu_list)


def get_match_result():
    match_ids = []
    for category_id in get_category_ids():
        match_ids.append(get_home_category_all_match(category_id))
    for match_id in match_ids:
        time.sleep(1)
        if isinstance(match_id, list):
            for match_id_temp in match_id:
                time.sleep(1)
                get_match_detail(match_id_temp)
        else:
            get_match_detail(match_id)
