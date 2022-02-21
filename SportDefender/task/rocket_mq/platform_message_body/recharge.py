import json
from common.utils import generate_uuid
from common.utils import upper_lower


def create_message_body(user_id, coin_name, amount):
    tx_id = generate_uuid.get_tx_id()
    coin_name = upper_lower.switch_to_upper(coin_name)
    message_body = {

        "userId": user_id,
        "coinName": coin_name,
        "txId": tx_id,
        "amount": amount
    }
    return json.dumps(message_body)
