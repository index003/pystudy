
from types import prepare_class
import requests
import json
import jsonpath

class KeyDemo:

    def get(self, url, headers=None, param=None):
        return requests.get(url=url, headers=headers, params=param)


    def post(self, url, headers=None, param=None):
        return requests.post(url=url, headers=headers, data=param)

    def get_text(self, res, key):
        
        if res is not None:
            try:
                # 将res文本转换为JSON，通过jsonpath解析获取到指定的key的value值。
                text = json.loads(res)
                value = jsonpath.jsonpath(text, '$..{0}'.format(key))
                # jsonpath获取的结果是list类型的值,如果获取失败则是False
                if value:
                    # 将list转成String格式
                    if len(value) == 1:
                        return value[0]
                return value
            except Exception as e:
                return e    
        else:
            return None