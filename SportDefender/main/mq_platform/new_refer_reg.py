import json

from rocket import send_message
from config import env_config

env_config.env = 'fat1'

message_body = {
    "referUserId": "KWZ5",
    "userId": 265281547,
    "regIp": "172.16.6.29"
}
# referUserId:邀请码
# userId：被推荐用户
# regIp：被推荐用户ip

send_message.send_message_str("activity_refer_reg", json.dumps(message_body))
