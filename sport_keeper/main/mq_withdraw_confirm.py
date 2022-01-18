import json
from rocket import send_message
from config import env_config
from rocket import message_body_recharge

env_config.env = 'fat1'
order_no = input()
txid = message_body_recharge.get_tx_id()
message_body = {
    "code": 0,
    "msg": '',
    # "orderNo": "W1642477229916A90CG1002",
    "orderNo": f"{order_no}",
    "txId": f"{txid}"
}

# "orderNo": 提币订单
send_message.send_message_str("account_withdraw_confirm", json.dumps(message_body))

