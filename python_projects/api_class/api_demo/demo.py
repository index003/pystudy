
import os
import sys
from os.path import dirname,abspath
project_path = dirname(dirname(abspath(__file__)))
#__file__用于获取文件的路径，abspath(__file__)获得绝对路径；
#dirname()用于获取上级目录，两个dirname()相当于获取了当前文件的上级的上级即示例中project2

sys.path.append(project_path)

from api_keyword.keyword_demo import KeyDemo
import configparser
import yaml

# 实例化需要的内容
conf = configparser.ConfigParser()
kd = KeyDemo()

# 创建data
# file = open('./data/login.yaml', 'r')
# # data = yaml.load(file, yaml.FullLoader)
# data = yaml.safe_load(file)

with open('./data/login.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

print(data)
print(type(data))
print(data['path'])
print(type(data['path']))
print(data['data'])
print(type(data['data']))

# 测试数据
conf.read('./config/config.ini')
# print(conf.get('DEFAULT', 'url'))
url = conf.get('DEFAULT', 'url') + data['path']

# localpath = public_path = os.path.dirname(__file__)  # 当前执行文件的路径 推荐使用这种方式
# print('本文件目录位置：' + localpath)

# 执行测试
res = kd.get(url, data['data'])
print(res.text)