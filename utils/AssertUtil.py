"""
@Project ：PythonWebDriverUIFrame 
@File    ：AssertUtil.py
@IDE     ：PyCharm 
@Author  ：张成龙
@Date    ：2024/9/11 10:03 
@explain ：断言
"""


class AssertUtil:

    """
        assert 实际值 存在于期望结果之内
    """

    @classmethod
    def assert_real_in_expect(cls, real, expect):
        """
        :param real:  实际结果
        :param expect:  期望结果
        :return: 返回元素值
        """
        assert real in expect, f"Assertion failed: '{real}' not found in '{expect}'"
        return f"'{real}' found in '{expect}'"

    """
        assert 实际值 相等于 期望结果
    """

    @classmethod
    def assert_real_equal_expect(cls, real, expect):
        """
        :param real: 实际结果
        :param expect: 期望结果
        :return: 返回元素值
        """
        assert real == expect, f"Assertion failed: '{real}' not equal to '{expect}'"
        return f"'{real}' equal to '{expect}'"


