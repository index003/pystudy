import hashlib
from common.utils import upper_lower


def md5_value(match_id, source):
    source = upper_lower.switch_to_lower(source)
    string = f"matchId={match_id}&source={source}VkryuBktdSvnglZd"
    input_name = hashlib.md5()
    input_name.update(string.encode("utf-8"))
    md5_32_lower = input_name.hexdigest().lower()  # 小写32位
    # md5_32_upper = input_name.hexdigest().upper()  # 大写32位
    # md5_16_lower = input_name.hexdigest()[8:-8].lower()  # 小写16位
    # md5_16_upper = input_name.hexdigest()[8:-8].upper()  # 大写16位
    return md5_32_lower