import os
import sys
import time

path1 = os.path.abspath('')   # 表示当前所处的文件夹的绝对路径
print('==path1==', path1)
path2 = os.path.abspath('../basic_knowledge')  # 表示当前所处的文件夹上一级文件夹的绝对路径
print('==path2==', path2)
now = time.strftime("%Y-%m-%d %H-%M-%S")
# public_path = os.path.dirname(os.path.abspath(sys.argv[0]))  # 获取当前运行的.py文件所在的绝对路径
public_path = os.path.dirname(__file__)  # 当前执行文件的路径 推荐使用这种方式
filename = public_path + "/report/" + now + "report.html"
# filename = os.path.join(public_path, 'report', now + 'report.html')
print('====filename======', filename)
