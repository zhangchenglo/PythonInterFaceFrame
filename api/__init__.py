"""
@Project ：PythonInterfaceFrame 
@File    ：__init__.py.py
@IDE     ：PyCharm 
@Author  ：张成龙
@Date    ：2024/10/12 10:09 
@explain ：
"""
import logging
import time

from conftest import init_log_config
from utils.LoadEnvParamsUtil import LoadEnvParamsUtil

init_log_config()
logging.info("log at {}".format(time.strftime('%Y-%m-%d %H:%M:%S')))

SYSTEM_URL = LoadEnvParamsUtil.get_env_params("BASE_URL")