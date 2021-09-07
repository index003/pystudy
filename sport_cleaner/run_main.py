from db_operation import clean_match
from admin_operation import award_pending
from db_operation import db_util
from admin_operation import config_api_info

# fat1 = 1，fat2 =2，fat3 =3， fat4=4
# 要执行脚本的时候，先指定要执行的环境

env = 3

# 分别指定数据连接的环境和admin连接的环境
db_util.env = env
config_api_info.env = env

# 删除待开奖列表数据
matchIds = award_pending.matchIds
clean_match.clean_match_list(matchIds)

# # 删除指定id赛事
# clean_match.clean_match(306)
#
# # 删除多个指定id赛事
# clean_match.clean_match([305, 306])

