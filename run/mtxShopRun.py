# @Author: 夭夭
# @Time: 五月 28, 2020

import unittest
import os
import sys

from testSuite.testScript_fanshe import TestRunScript

file_path = os.path.abspath(os.path.join(os.getcwd(),'..'))
sys.path.append(file_path)
from tool import htmlTestRunner
import time


class TestRunner(object):
    def __init__(self):
        self.suite = unittest.TestSuite()
        self.suite = unittest.TestLoader().loadTestsFromTestCase(TestRunScript)

    def startRun(self):

        now = time.strftime('%Y-%m-%d_%H_%M_%S')
        file_name ='../report/'+'mtxshop' +now+'.html'
        fb = open(file_name, 'wb')
        runner = htmlTestRunner.HTMLTestRunner(stream=fb, title='mtxshop',description='mtxshop')
        runner.run(self.suite)
        fb.close()


if __name__ == '__main__':
    # 执行用例
    run = TestRunner()
    run.startRun()