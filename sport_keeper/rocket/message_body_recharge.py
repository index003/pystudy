import json
import uuid


def get_tx_id():
    uuid_init = uuid.uuid4()
    uuid_str = str(uuid_init)
    tx_id = ''.join(uuid_str.split('-'))
    return tx_id


def create_message_body(user_id, coin_name, amount):

    message_body = {

        "userId": user_id,
        "coinName": coin_name,
        "txId": get_tx_id(),
        "amount": amount
    }
    return json.dumps(message_body)
