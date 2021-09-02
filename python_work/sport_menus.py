import requests
import json

url = "https://fat3-api.testbitgame.com/lottery/platform/menus?lang=zh-Hant&type=0&launchType=CENTRALIZED"
response = requests.get(url)
# 将字符串形式转换为json格式，字典类型
response_dic = json.loads(response.text)
data_list = response_dic['data']
for menu_data in data_list:
    if menu_data['count'] != 0:
        print(f"'categoryId = '{menu_data['categoryId']}")
        print(f"'categoryCode = '{menu_data['categoryCode']}")
        print(f"'categoryName = '{menu_data['categoryName']}")
        print(f"'count = '{menu_data['count']}")
        print(f"'sportType = '{menu_data['sportType']}")

