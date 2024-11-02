"""
@Project ：PythonWebDriverUIFrame 
@File    ：FakerDataUtil.py
@IDE     ：PyCharm 
@Author  ：张成龙
@Date    ：2024/9/11 10:04 
@explain ：常用数据构造
"""
import random

from faker import Faker


class FakerDataUtil:

    faker = Faker("zh-CN")

    # 随机生成用户名
    @classmethod
    def faker_user_name(cls):
        """
        :return: random generate unique username
        """
        return cls.faker.unique.name()

    # 随机生成手机号
    @classmethod
    def faker_phone_number(cls):
        return cls.faker.unique.phone_number()

    # 随机生成文本信息 max_nb_chars(最大字符长度)
    @classmethod
    def faker_random_text(cls):
        """
        :return: 返回字符长度为 20 的随机文本
        """
        return cls.faker.text(max_nb_chars=20, ext_word_list=None)

    # 随机生成公司名称
    @classmethod
    def faker_company(cls):
        return cls.faker.unique.company()

    # 随机生成地址/住址信息
    @classmethod
    def faker_address(cls):
        return cls.faker.address()

    @classmethod
    def random_generate_zero_or_one(cls):
        """
        :return: 随机生成整数  0 或者 1
        """
        random_num = random.randint(0, 1)
        return random_num

    @classmethod
    def random_generate_true_or_false(cls):
        """
        :return: 随机生成 True 或者 False
        """
        result = bool(random.getrandbits(1))
        return result

    @classmethod
    def faker_email(cls):
        """
        :return: 随机生成邮箱
        """
        email = cls.faker.unique.email()
        return email

    @classmethod
    def faker_province(cls):
        """
        :return: 随机生成 省份
        """
        province = cls.faker.province()
        return province

    @classmethod
    def faker_job(cls):
        """
        :return: 随机生成职位
        """
        job = cls.faker.job()
        return job

    @classmethod
    def faker_password(cls, length=8):
        """
        :return: 随机密码
        length 长度
        special_chars 特殊字符
        digits 数字
        upper_case 大写
        lower_case 小写
        """
        password = cls.faker.unique.password(length, special_chars=True, digits=True, upper_case=True, lower_case=True)
        return password

    @classmethod
    def faker_string(cls):
        """
        :return: 随机生成字符串
        """
        pystring = cls.faker.unique.pystr()
        return pystring

    @classmethod
    def faker_number(cls):
        """
        :return: 随机生成 int 整数
        """
        pyint = cls.faker.pyint()
        return pyint















