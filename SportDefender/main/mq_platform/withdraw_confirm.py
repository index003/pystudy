from common.config import env_config
from task.rocket_mq.platform_message_body import withdraw
from task.rocket_mq.mq_requset import send_message

env_config.env = 'fat1'


# "orderNo": 提币订单
def send_withdraw_confirm(order_id):
    message_body = withdraw.create_message_body(order_id)
    send_message.send_message_str("account_withdraw_confirm", message_body)


send_withdraw_confirm('W1642477229916A90CG1002')
