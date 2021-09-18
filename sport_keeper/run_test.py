from config import env_config
from db_operation import db_crud
from db_operation import clean_match_function
from admin_operation import admin_login
from admin_operation import settlement_list
from admin_operation import subscription_league
env = 'fat4'
env_config.env = env

# sql = 'select * from sport_match_info where id = 1149'
# res = db_crud.query_execute(env, sql)
# print(res)

# clean_match_function.clean_match(env, 1149)
# admin_login.admin_login()

# res = settlement_list.get_list(env, "FIRST_CHECK")
# res = settlement_list.get_list(env, "AWARD_PENDING")
# print(res)
subscription_league.subscription_league(env, 202)



