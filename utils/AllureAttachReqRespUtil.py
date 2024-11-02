"""
@Project ：PythonInterfaceFrame 
@File    ：AllureAttachReqRespUtil.py
@IDE     ：PyCharm 
@Author  ：张成龙
@Date    ：2024/10/12 11:37 
@explain ：
"""
import allure


class AllureAttachReqRespUtil:

    @staticmethod
    def attach_request_response(request, response):
        # 记录请求信息
        request_info = (
            f"URL: {request.url}\n"
            f"Method: {request.method}\n"
            f"Headers: {request.headers}\n"
            f"Body: {request.body or 'No Body'}"
        )
        allure.attach(request_info, name="Request", attachment_type=allure.attachment_type.TEXT)

        # 记录响应信息
        response_time = response.elapsed.total_seconds()  # 响应时间
        response_size = len(response.content)  # 响应数据大小（字节数）

        response_info = (
            f"Status Code: {response.status_code}\n"
            f"Response Time: {response_time} seconds\n"
            f"Headers: {response.headers}\n"
            f"Body: {response.text}\n"
            f"Response Size: {response_size} bytes"
        )
        allure.attach(response_info, name="Response", attachment_type=allure.attachment_type.TEXT)
