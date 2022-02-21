import json
from common.utils import generate_uuid


def create_message_body(order_no):
    tx_id = generate_uuid.get_tx_id()
    message_body = {
        "code": 0,
        "msg": '',
        # "orderNo": "W1642477229916A90CG1002",
        "orderNo": order_no,
        "txId": tx_id
    }
    return json.dumps(message_body)
