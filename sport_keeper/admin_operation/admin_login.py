import json
import requests
from config import api_config
from config import env_config

env = env_config.env


# 登录admin
def admin_login(env):
    api_domain = api_config.get_apidomain(env)
    path = api_config.sendopt_path
    url = api_domain + path
    print(url)
    data = {
        "account": "admin"
    }
    response = requests.get(url, params=data)
    rspCode = json.loads(response.text)['rspCode']
    print(f"rspCode = {rspCode}")

    path = api_config.login_path
    url = api_domain + path

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
    print(f"token = {token}")
    return token
