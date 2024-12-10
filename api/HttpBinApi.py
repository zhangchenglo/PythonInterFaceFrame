"""
@Project ：PythonInterfaceFrame 
@File    ：HttpBinApi.py
@IDE     ：PyCharm 
@Author  ：张成龙
@Date    ：2024/10/12 11:14 
@explain ：
"""

import allure
import requests

from api import SYSTEM_URL
from utils.LoadEnvParamsUtil import LoadEnvParamsUtil


class HttpBinApi:

    @classmethod
    @allure.step("发送get请求")
    def req_get(cls):
        response = requests.get(SYSTEM_URL + "/get")
        return response

    @classmethod
    @allure.step("发送post请求")
    def req_post(cls, username, password, image):
        headers = {
            "Cookie": "SESSION=" + LoadEnvParamsUtil.get_env_params("SESSION")
        }

        body = {
            "name": username,
            "pwd": password
        }

        files = [
            (
                "image", image
            )
        ]

        response = requests.post(SYSTEM_URL + "/post", headers=headers, data=body, files=files)
        return response
