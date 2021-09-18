from config import env_config
from db_operation import clean_match_function

# 配置环境 fat1，fat2，fat3,fat4,pre
env_config.env = 'fat2'

# 删除指定的赛事-单场赛事
clean_match_function.clean_match(1149)

# 删除指定的赛事-多场赛事
clean_match_function.clean_match_list([1149, 1150])
