import requests
import json
url = "https://fat3-api.testbitgame.com/lottery/platform/v2/matches?type=1&subType=0&categoryId=8&lang=zh-Hant&launchType=CENTRALIZED"

response = requests.get(url)
# 将字符串形式转换为json格式，字典类型
response_dic = json.loads(response.text)

data_list = response_dic['data']
for object_data in data_list:
    leaguage_info_list = object_data['leagueInfoList']
    for leaguage_info in leaguage_info_list:
        match_info_list = leaguage_info['matchInfoList']
        for match_info in match_info_list:
            print(f"match_id = {match_info['id']}")

