from config import env_config
from admin_operation import settlement_list
from db_operation import clean_match_function

# 配置环境 fat1，fat2，fat3,fat4,pre
env_config.env = 'fat2'

#
match_ids = settlement_list.get_list("FIRST_CHECK")
clean_match_function.clean_match_list(match_ids)
