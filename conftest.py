"""
@Project ：PythonInterfaceFrame 
@File    ：conftest.py
@IDE     ：PyCharm 
@Author  ：张成龙
@Date    ：2024/10/12 10:09 
@explain ：
"""
import os.path
import logging
import os
from logging import handlers

# 项目根路径
# BASE_DIR = os.path.dirname(__file__)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


# 配置日志文件
# 初始化日志配置
def init_log_config():
    # 创建日志器
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # 创建控制台处理器
    sh = logging.StreamHandler()

    # 创建文件处理器
    # 文件路径
    log_path = BASE_DIR + os.sep + "log" + os.sep + "log.log"

    fh = logging.handlers.TimedRotatingFileHandler(log_path, when="midnight", interval=1,
                                                   backupCount=7, encoding="UTF-8")
    # 创建格式化器
    f = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    formatter = logging.Formatter(f)

    # 把格式化处理器添加到处理器当中
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)

    # 把处理器添加到日志器当中
    logger.addHandler(sh)
    logger.addHandler(fh)