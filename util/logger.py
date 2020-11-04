# @Author: 夭夭
# @Time: 五月 25, 2020

import os.path
from util.config import Config
import logging
import os.path
import time

class Logger(object):
    def __init__(self):
        '''
        指定保存日志的路径，日志级别，以及调用文件
        将日志存入到指定的文件中
        '''
        cf = Config()
        # 日志存放位置
        self.log_dir = cf.get_value('log.conf','basiclog','log_dir')
        # 日志输出格式
        self.format = cf.get_value('log.conf','basiclog','format')
        #创建一个logger
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        cur_date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        package_path = os.path.abspath('..')
        file_path = os.path.join(package_path,self.log_dir)
        file_name = cur_date + '.log'
        log_file = os.path.join(file_path,file_name)
        # 设置一个文件处理器
        fh = logging.FileHandler(log_file)
        fh.setLevel(logging.INFO)
        # 定义一个输出到控制台的handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        # 定义handler的输出格式
        formatter = logging.Formatter(self.format)
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加到handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)


    def getlog(self):
        return self.logger