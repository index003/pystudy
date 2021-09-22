from config import env_config


# 接口域名
# admin后台主域名
def get_admin_domain():

    if 'fat' in env_config.env:
        domain = f"https://{env_config.env}-api-admin.testbitgame.com"
    elif 'game' in env_config.env:
        domain = f"https://{env_config.env}-api-admin.testbitgame.com"
    elif 'pre' in env_config.env:
        domain = "https://api-admin.prebitgame.com"
    else:
        domain = "https://api-admin.bitgame.com"
    return domain


# 前台主域名
def get_front_domain():
    if 'fat' in env_config.env:
        domain = f"https://{env_config.env}-api.testbitgame.com"
    elif 'game' in env_config.env:
        domain = f"https://{env_config.env}-api.testbitgame.com"
    elif 'pre' in env_config.env:
        domain = "https://api.prebitgame.com"
    else:
        domain = "https://api.bitgame.com"
    return domain


# 后台接口路径
# 获取验证码
def get_sendopt_url():
    return get_admin_domain() + "/login/sendOtp"


# 登录admin
def get_login_url():
    return get_admin_domain() + "/login"


# 结算管理-单关结算
def get_settlement_url():
    return get_admin_domain() + "/lottery/settlements"


# 订阅联赛
def get_subscription_url():
    return get_admin_domain() + "/lottery/leagues/libraryOrGrade/"


# 前台接口路径
# 首页菜单
def get_home_menus_url():
    return get_front_domain() + "/lottery/platform/menus"


# 首页类别
def get_home_category_url():
    return get_front_domain() + "/lottery/platform/v2/matches"


#
def get_match_detail_url():
    return get_front_domain() + "/lottery/platform/v2/matches/"

