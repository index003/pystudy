import time


def time_to_unix(str_time):
    # 先转换为时间数组
    time_array = time.strptime(str_time, "%Y-%m-%d %H:%M:%S")
    # 转换为时间戳
    time_stamp = int(time.mktime(time_array)) * 1000
    return time_stamp