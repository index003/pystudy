from task.rocket_mq.mq_requset import send_message
from task.rocket_mq.platform_message_body import recharge
from common.config import env_config

env_config.env = 'fat1'


def send_account_recharge(user_id, coin_name, amount):
    message_body = recharge.create_message_body(user_id, coin_name, amount)
    send_message.send_message_str("account_recharge", message_body)


send_account_recharge('609420462', 'USDT', 250)
