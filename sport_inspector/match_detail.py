import requests
import json
import config

api_domain = config.API_DOMAIN
path = "/lottery/platform/v2/matches/1074?lang=zh-Hant&launchType=CENTRALIZED"
url = api_domain + path

response = requests.get(url)
# 将字符串形式转换为json格式，字典类型
response_dic = json.loads(response.text)
rspCode = response_dic['rspCode']
if rspCode == "0000":
    print("pass")
else:
    print(rspCode)
