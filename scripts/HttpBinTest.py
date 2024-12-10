"""
@Project ：PythonInterfaceFrame 
@File    ：HttpBinTest.py
@IDE     ：PyCharm 
@Author  ：张成龙
@Date    ：2024/10/12 11:16 
@explain ：
"""
import logging
import os

import allure
import pytest

from api.HttpBinApi import HttpBinApi
from conftest import BASE_DIR
from utils.AllureAttachReqRespUtil import AllureAttachReqRespUtil
from utils.FakerDataUtil import FakerDataUtil


@allure.description("httpbin 接口自动化测试")
@allure.severity(allure.severity_level.BLOCKER)
class TestHttpBin:

    @pytest.mark.run(order=2)
    def test_httpbin_get(self):
        # 发送请求
        response = HttpBinApi.req_get()

        # 调用统一的Allure方法
        AllureAttachReqRespUtil.attach_request_response(response.request, response)

        # 打印日志
        logging.info("response = {}".format(response.json()))

        # 断言
        assert response.status_code == 200

    @pytest.mark.run(order=1)
    def test_httpbin_post(self):
        images_path = BASE_DIR + os.sep + "data" + os.sep + "avatar.png"

        images = open(images_path, "rb")

        response = HttpBinApi.req_post(FakerDataUtil.faker_user_name(), FakerDataUtil.faker_password(), images)
        AllureAttachReqRespUtil.attach_request_response(response.request, response)

        logging.info("response = {}".format(response.json()))

        # 断言
        assert response.status_code == 200
