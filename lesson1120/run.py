# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : run.py
# @author   : 沙陌 Matongxue_2
# @Time     : 2022/11/20 16:34
# @Copyright: 北京码同学
import unittest
from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    # 这是咱测试执行的入口
    # 在这里要去组织和管理我要执行的测试用例
    suite = unittest.defaultTestLoader.discover('lesson1120','test_*.py')

    # 定义一个执行器
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    # 上面这个执行结果太过简陋，我们可以借助第三方的HTMLTestRunner执行器，帮我们生成html的测试报告
    with open(file='testreport.html',mode='wb') as f:
        HTMLTestRunner(f,title='测试报告',description='码同学测试报告').run(suite)
