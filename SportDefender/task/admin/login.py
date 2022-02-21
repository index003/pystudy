import json
import requests
from common.config import api_config


# 登录admin,返回token
def admin_login():
    url = api_config.get_sendopt_url()
    print(url)
    data = {
        "account": "admin"
    }
    response = requests.get(url, params=data)
    rsp_code = json.loads(response.text)['rspCode']
    print(f"rsp_code = {rsp_code}")

    url = api_config.get_login_url()
    data = {
        "account": "admin",
        "password": "123456",
        "otpCode": "123456"
    }
    data = json.dumps(data)

    headers = {
        "content-Type": "application/json;charset=UTF-8",
    }

    response = requests.post(url, data=data, headers=headers)
    token = json.loads(response.text)['data']['token']
    # print(f"token = {token}")
    return token
