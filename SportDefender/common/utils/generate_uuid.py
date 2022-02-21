import uuid


def get_tx_id():
    uuid_init = uuid.uuid4()
    uuid_str = str(uuid_init)
    tx_id = ''.join(uuid_str.split('-'))
    return tx_id