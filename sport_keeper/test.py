from config import env_config
from admin_operation import settlement_list

env_config.env = 'fat3'
kkk = settlement_list.get_list('FIRST_CHECK')
print(kkk)
