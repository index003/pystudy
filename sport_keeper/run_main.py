from config import env_config
from admin_operation import settlement_list, subscription_league
from db_operation import clean_match_function
from rocket_mq import rocket
from rocket_mq import match_status
from front_operation import inspect_content

# 配置环境 fat1，fat2，fat3,fat4,pre,prod
env_config.env = 'fat4'


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


# 推送mq消息
def sub_mq(topic, message):
    rocket.send_message_str(topic, message)


# mq消息体
def get_message_body(match_id, status):
    return match_status.match_status_msg(match_id, status)


# 赛事巡检
def match_check():
    inspect_content.get_match_result()


# sub_league(205)
# clean_match_by_id(1279)
# clean_match_by_id([1064, 1111, 1162, 1181, 1216, 1236, 1246, 1269, 1323, 1335, 1365])
# settlement_list.get_list('FIRST_CHECK')
# clean_match_settlement_list('AWARD_PENDING')
# clean_match_settlement_list('FIRST_CHECK')

# message_body = get_message_body(1164, 3)
# sub_mq('match_metadata_update', message_body)

# match_check()
