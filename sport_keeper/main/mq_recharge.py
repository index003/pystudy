from rocket import send_message
from rocket import message_body_recharge
from config import env_config

env_config.env = 'fat2'


def send_account_recharge(user_id, coin_name, amount):
    message_body = message_body_recharge.create_message_body(user_id, coin_name, amount)
    send_message.send_message_str("account_recharge", message_body)


send_account_recharge('491195673', 'USDT', 100)
