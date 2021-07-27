import unittest
import yaml
import sys
from os.path import dirname,abspath
import ddt

project_path = dirname(dirname(abspath(__file__)))
#__file__用于获取文件的路径，abspath(__file__)获得绝对路径；
#dirname()用于获取上级目录，两个dirname()相当于获取了当前文件的上级的上级即示例中project2
sys.path.append(project_path)

# f = open('./data/login.yaml')
# print(yaml.safe_load(f))
@ddt.ddt
class MyDdt_test(unittest.TestCase):
    @ddt.file_data('../data/demo.yaml')
    def test1(self, num):
        self.assertTrue(num > 2)

if __name__=='__main__':
    unittest.main()