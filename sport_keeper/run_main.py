from config import env_config
from admin_operation import settlement_list, subscription_league
from db_operation import clean_match_function

# 配置环境 fat1，fat2，fat3,fat4,pre
env_config.env = 'game1'


# 删除指定赛事，可以单个，如1149，也可以多个,如[1149, 1150]
def clean_match_by_id(match_ids):
    if isinstance(match_ids, list):
        clean_match_function.clean_match_list(match_ids)
    else:
        clean_match_function.clean_match(match_ids)


# 删除admin后台-结算管理-单关结算-列表中所有的数据
# FIRST_CHECK -- 待结算, AWARD_PENDING -- 待开奖
def clean_match_settlement_list(award_status):
    match_ids = settlement_list.get_list(award_status)
    clean_match_function.clean_match_list(match_ids)


# 订阅联赛
def sub_league(category_id):
    subscription_league.subscription_league(category_id)


# sub_league(209)
# clean_match_by_id(423)
# clean_match_by_id([1845, 1838])
# clean_match_settlement_list('AWARD_PENDING')
# clean_match_settlement_list('FIRST_CHECK')

