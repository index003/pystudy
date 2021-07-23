#!/usr/bin/env python3.8

import unittest
from HTMLTestRunner import HTMLTestRunner
import time

# 定义测试用例的目录为当前目录
test_dir = './'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

if __name__ == "__main__":
    # 按照一定的格式获取当前的时间
    now = time.strftime("%Y-%m-%d %H-%M-%S")

    # 定义报告存放路径
    filename = './' + now + 'test_result.html'

    # 使用上下文管理器with open，会自动释放文件句柄
    with open(filename, 'wb') as wf:
        # 定义测试报告
        runner = HTMLTestRunner(
            stream=wf,
             title="用户交易接口测试报告",
             description="测试用例执行情况："
        )
        runner.run(discover)
