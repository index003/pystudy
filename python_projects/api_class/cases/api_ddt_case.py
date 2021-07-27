import unittest
import sys
from os.path import dirname,abspath
import yaml
project_path = dirname(dirname(abspath(__file__)))
#__file__用于获取文件的路径，abspath(__file__)获得绝对路径；
#dirname()用于获取上级目录，两个dirname()相当于获取了当前文件的上级的上级即示例中project2
sys.path.append(project_path)

from api_keyword.keyword_demo import KeyDemo

# 创建一个UnitTest测试用例管理框架
import configparser
import ddt

@ddt.ddt
class ApiCases(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.value = None
        # 实例化需要的内容
        conf = configparser.ConfigParser()
        conf.read('./config/config.ini')
        cls.url = conf.get('DEFAULT', 'url')
        cls.kd = KeyDemo() 
        
    # 测试用例
    @ddt.file_data('./data/demo.yaml')
    @ddt.unpack
    def test_01_api_demo(self, **kwargs):
        url = self.url + kwargs.get('path')
        print(url)
        # # 执行测试
        res = self.kd.get(url, kwargs.get('data'))
        print(res.text)

        ApiCases.value = self.kd.get_text(res.text, 'Name')
        print(self.value)
        self.assertEqual(first=kwargs['text'],second=self.value, msg='获取信息失败')
    # # @file_data('./data/login.yaml')
    # def test_02_value(self):
    #     print(self.value)

if __name__=='__main__':
    unittest.main()