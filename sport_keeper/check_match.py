from front_operation import inspect_content
from config import env_config

# 配置环境 fat1，fat2，fat3,fat4,pre,prod
env_config.env = 'prod'


# 赛事巡检
def match_check():
    inspect_content.get_match_result()


match_check()
