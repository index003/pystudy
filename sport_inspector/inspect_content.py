import requests
import json
import config


# 获取赛事首页类别菜单信息，返回类别的详细信息
def get_home_menus():
    api_domain = config.API_DOMAIN
    path = "/lottery/platform/menus?lang=zh-Hant&type=0&launchType=CENTRALIZED"
    url = api_domain + path
    response = requests.get(url)
    # 将字符串形式转换为json格式，字典类型
    response_dic = json.loads(response.text)
    return response_dic['data']


# 获取类别信息的category id,列表形式，不包括自定赛事
def get_home_menus_category_id(data):
    category_list = []
    for category in data:
        if category['count'] != 0 and category['categoryId'] not in [212, 213, 214]:
            category_list.append(category['categoryId'])
    return category_list


# 展示赛事首页类别菜单信息
def show_home_menus_result(data):
    for menu_data in data:
        if menu_data['count'] != 0 and menu_data['categoryId'] not in [212]:
            print(f"'categoryId' = {menu_data['categoryId']}")
            print(f"'categoryCode' = {menu_data['categoryCode']}")
            print(f"'categoryName' = {menu_data['categoryName']}")
            print(f"'count' = {menu_data['count']}")
            print(f"'sportType = {menu_data['sportType']}")


# 查询类别下所有的赛事
def get_home_category_all_match(category_id):
    api_domain = config.API_DOMAIN
    path = f"/lottery/platform/v2/matches?type=0&subType=0&categoryId={category_id}&lang=zh-Hant&launchType=CENTRALIZED"
    url = api_domain + path
    response = requests.get(url)
    # 将字符串形式转换为json格式，字典类型
    response_dic = json.loads(response.text)
    match_ids = []
    for object_data in response_dic['data']:
        leaguage_info_list = object_data['leagueInfoList']
        for leaguage_info in leaguage_info_list:
            match_info_list = leaguage_info['matchInfoList']
            for match_info in match_info_list:
                match_ids.append(f"{match_info['id']}")
    return match_ids


def get_match_detail(match_id):
    api_domain = config.API_DOMAIN
    path = f"/lottery/platform/v2/matches/{match_id}?lang=zh-Hant&launchType=CENTRALIZED"
    url = api_domain + path
    response = requests.get(url)
    # 将字符串形式转换为json格式，字典类型
    response_dic = json.loads(response.text)
    rspCode = response_dic['rspCode']
    if rspCode == "0000":
        print("pass")
    else:
        print(rspCode)


def get_category_ids():
    menu_list = get_home_menus()
    # show_home_menus_result(menu_list)
    return get_home_menus_category_id(menu_list)


def get_match_result():
    match_ids = []
    for category_id in get_category_ids():
        match_ids.append(get_home_category_all_match(category_id))

    for match_id in match_ids:
        if isinstance(match_id, list):
            for match_id_temp in match_id:
                get_match_detail(match_id_temp)
        else:
            get_match_detail(match_id)


get_match_result()
