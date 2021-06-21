#coding=utf-8
import  pytest,os,json,allure
from ttxn_api.Public.framework import *

class Test_Api_Login(object):
    """登录模块接口"""

    @classmethod
    def setup_class(cls):
        cls.head = {}

    @classmethod
    def teardown_class(cls):
        pass


    def test_password_login(self):
        """正确的密码可以正常登录"""
        data_1 = dateChangeDict(filename, "login", 1)  ##从excel表格里读取接口的数据
        res_1 = apiRequests(data_1[3], data_1[4], data_1[5], self.head)  ##发送接口请求
        data_2 = dateChangeDict(filename, "login", 2)  ##从excel表格里读取接口的数据
        res_2 = apiRequests(data_2[3], data_2[4], data_2[5], self.head)  ##发送接口请求
        print(res_2.json())
        assert res_2.json()['msg']=='成功'
        token = res_2.json()["data"]["token"]
        writExcel(filename, 'token', line=1, row=0, data=token)


    def test_error_password_login(self):
        """错误的验证码无法登录"""
        data_1 = dateChangeDict(filename, "login", 1)  ##从excel表格里读取接口的数据
        res_1 = apiRequests(data_1[3], data_1[4], data_1[5], self.head)  ##发送接口请求
        data_2 = dateChangeDict(filename, "login", 3)  ##从excel表格里读取接口的数据
        res_2 = apiRequests(data_2[3], data_2[4], data_2[5], self.head)  ##发送接口请求
        print(res_2.json())
        assert res_2.json()['msg'] == '验证码错误'


    def test_not_inpot_password_login(self):
        """不输入密码无法登录"""
        data_1 = dateChangeDict(filename, "login", 1)  ##从excel表格里读取接口的数据
        res_1 = apiRequests(data_1[3], data_1[4], data_1[5], self.head)  ##发送接口请求
        data_2 = dateChangeDict(filename, "login", 4)  ##从excel表格里读取接口的数据
        res_2 = apiRequests(data_2[3], data_2[4], data_2[5], self.head)  ##发送接口请求
        print(res_2.json())
        assert res_2.json()['msg'] == '验证码错误'


if __name__ == '__main__':
    pytest.main()


