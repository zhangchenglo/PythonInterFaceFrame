"""
@Project ：PythonWebDriverUIFrame 
@File    ：LoadEnvParamsUtil.py
@IDE     ：PyCharm 
@Author  ：张成龙
@Date    ：2024/9/11 10:06 
@explain ：读取系统 .env 文件参数 value 值
"""
import os

from dotenv import load_dotenv, set_key


# 安装方式 pip install python-dotenv


class LoadEnvParamsUtil:

    @classmethod
    def get_env_params(cls, params):
        load_dotenv()  # 加载env变量
        return os.environ.get(params)

    @classmethod
    def set_env_params(cls, params, value):
        # 检查 .env 文件是否存在，如果不存在则创建
        env_file = '.env'
        if not os.path.exists(env_file):
            with open(env_file, 'w') as f:
                pass  # 创建空的 .env 文件

        load_dotenv()
        set_key(env_file, params, value, quote_mode='never')
        print(f"{params} 已写入 env 文件")
