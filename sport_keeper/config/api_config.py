from config import env_config


# 接口域名
# admin后台主域名
def get_domain():

    if 'fat' in env_config.env:
        domain = f"https://{env_config.env}-api-admin.testbitgame.com"
    elif 'pre' in env_config.env:
        domain = "https://api-admin.prebitgame.com"
    else:
        domain = "https://api-admin.bitgame.com"
    return domain


# 接口路径
# 获取验证码
def get_sendopt_url():
    return get_domain() + "/login/sendOtp"


# 登录admin
def get_login_url():
    return get_domain() + "/login"


# 结算管理-单关结算
def get_settlement_path():
    return get_domain() + "/lottery/settlements?pageSize=20&pageNum=1&awardStatus="


# 订阅联赛
def get_subscription_path():
    return get_domain() + "/lottery/leagues/libraryOrGrade/"
