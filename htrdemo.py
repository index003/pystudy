#!/usr/bin/python3
# encoding:utf-8
'''

'''
import unittest
import HTMLTestRunner
import os
import time
 
class HtmlReport(unittest.TestCase):
  def test_1(self):
    print('test_1错误')
    self.assertEqual(1, 2,'说明错误')
  def test_2(self):
    print('test_2正确')
    self.assertEqual(1, 1)
  def test_3(self):
    print('test_3错误')
    self.assertEqual(2, 3)
if __name__=='__main__':
  now = time.strftime("%Y-%m-%d %H%M%S", time.localtime(time.time()))
  localpath = os.getcwd()
  print('本文件目录位置：'+localpath)
  filepath = os.path.join(localpath,'Report',now +'.html')
  print('报告存放路径  ：'+filepath)
   
  ts = unittest.TestSuite()#实例化
  #按类加载全部testxxx测试用例
  ts.addTest(unittest.TestLoader().loadTestsFromTestCase(HtmlReport))
  #按函数加载testxxx测试用例
  #ts.addTest(HtmlReport('test_1'))
  #打开文件位置，如果没有则新建一个文件
  filename = open(filepath,'wb')
  htmlroport = HTMLTestRunner.HTMLTestRunner(stream=filename,title='标题XXX报告',description='XXX报告XX描述',tester='测试人员XXX')
  htmlroport.run(ts)