import requests
import json
from config import api_config
from admin_operation import admin_login


def get_list(award_status):
    url = api_config.get_settlement_url()
    authorization = admin_login.admin_login()
    headers = {
        "content-Type": "application/json;charset=UTF-8",
        "authorization": authorization
    }

    # 先拿到列表中赛事的数量
    data = {
        'pageSize': 20,
        'pageNum': 1,
        'awardStatus': award_status
    }
    response = requests.get(url, params=data, headers=headers)
    response_dict = json.loads(response.text)
    data_list = response_dict['data']
    # print(f"Total is: {data_list['total']}")
    # 计算有多少页数据,如果列表为空，就不执行了
    if data_list['total'] == 0:
        return
    page_numbers = int(data_list['total']/20 + 1)
    print(page_numbers)

    # 将列表中所有的赛事都取到
    match_ids = []
    for page_number in range(1, page_numbers+1):
        data2 = {
            'pageSize': 20,
            'pageNum': page_number,
            'awardStatus': award_status
        }
        response_all = requests.get(url, params=data2, headers=headers)
        print(response_all.url)
        response_dict_all = json.loads(response_all.text)
        data_list_all = response_dict_all['data']
        match_list = data_list_all['list']
        for match in match_list:
            match_id = match['matchId']
            match_ids.append(match_id)
    print(match_ids)
    return match_ids
