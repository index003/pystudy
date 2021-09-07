import requests
import json
import config_api_info
import admin_login

api_domain = config_api_info.API_DOMAIN

path = "/lottery/settlements?pageSize=20&pageNum=1&awardStatus=AWARD_PENDING"
url = api_domain + path
authorization = admin_login.admin_login()
headers = {
    "content-Type": "application/json;charset=UTF-8",
    "authorization": authorization
}
response = requests.get(url, headers=headers)
print(response.text)
response_dict = json.loads(response.text)
data_list = response_dict['data']
print(f"Total is: {data_list['total']}")

# 将列表中所有的赛事都取到
path_all = f"/lottery/settlements?pageSize={data_list['total'] - 116}&pageNum=1&awardStatus=AWARD_PENDING"
url_all = api_domain + path_all
response_all = requests.get(url_all, headers=headers)
print(response_all.text)
response_dict_all = json.loads(response_all.text)
data_list_all = response_dict_all['data']
match_list = data_list_all['list']
matchIds = []
for match in match_list:
    matchId = match['matchId']
    matchIds.append(matchId)
print(matchIds)
