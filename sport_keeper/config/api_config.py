from config import env_config

env = env_config.env


# 接口域名
# admin后台主域名
def get_apidomain(env):
    return f"https://{env}-api-admin.testbitgame.com"


# 接口路径
# 获取验证码
sendopt_path = "/login/sendOtp"
# 登录admin
login_path = "/login"
# 结算管理-单关结算
settlement_path = "/lottery/settlements?pageSize=20&pageNum=1&awardStatus="
# 订阅联赛
subscription_path = "/lottery/leagues/libraryOrGrade/"
