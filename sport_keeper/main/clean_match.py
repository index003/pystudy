from admin import settlement_list
from config import env_config
from data import clean_match

# 配置环境 fat1，fat2，fat3,fat4,pre,prod
env_config.env = 'fat2'


# 删除指定赛事，可以单个，如1149，也可以多个,如[1149, 1150]
def clean_match_by_id(match_ids):
    if isinstance(match_ids, list):
        clean_match.clean_match_list(match_ids)
    else:
        clean_match.clean_match(match_ids)


# 删除admin后台-结算管理-单关结算-列表中所有的数据
# FIRST_CHECK -- 待结算, AWARD_PENDING -- 待开奖
def clean_match_settlement_list(award_status):
    match_ids = settlement_list.get_list(award_status)
    clean_match.clean_match_list(match_ids)


clean_match_by_id([1535])
# clean_match_by_id([1886, 1887, 1888, 1889])
