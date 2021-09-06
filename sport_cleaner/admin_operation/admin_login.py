import json
import requests
import api_info

api_domain = api_info.API_DOMAIN


# 登录admin
def admin_login():
    path = "/login/sendOtp"
    url = api_domain + path
    data = {
        "account": "admin"
    }
    response = requests.get(url, params=data)
    rspCode = json.loads(response.text)['rspCode']
    print(f"rspCode = {rspCode}")

    path = "/login"
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
