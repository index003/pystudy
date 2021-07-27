'''
import sys

from os.path import dirname,abspath

project_path = dirname(dirname(abspath(__file__)))

#__file__用于获取文件的路径，abspath(__file__)获得绝对路径；

#dirname()用于获取上级目录，两个dirname()相当于获取了当前文件的上级的上级即示例中project2

sys.path.append(project_path+r'\module')

#路径拼接成D:\05_test_software\mudule

from calulater import *
'''
