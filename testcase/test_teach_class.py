#coding=utf-8
import pytest,os,json,allure,sys
sys.path.append("C:\\automation")
from ttxn_api.Public.framework import *
from ttxn_api.Config.Api_Data import *


class Test_Courses(object):
    """约课/上课模块接口"""

    @pytest.fixture(scope='function', autouse=True)
    def get_token(self, token):
        self.token = token
        self.head = {}

    def test_get_teach_class_01(self):
        """获取教学课接口1"""
        data = dateChangeDict(filename, "teach_class", 1)  ##从excel表格里读取接口的数据
        data[5]['token'] = self.token
        res = apiRequests(data[3], data[4], data[5], self.head)  ##发送接口请求
        print(res.json())
        assert res.json().get('msg') == data[6]

    def test_get_teach_class_02(self):
        """获取教学课接口2"""
        data = dateChangeDict(filename, "teach_class", 2)  ##从excel表格里读取接口的数据
        # data[5]['token'] = self.token
        res = apiRequests(data[3], data[4], data[5], self.head)  ##发送接口请求
        print(res.json())
        assert res.json().get('msg') == data[6]

    def test_get_teach_class_03(self):
        """获取教学课接口3"""
        data = dateChangeDict(filename, "teach_class", 3)  ##从excel表格里读取接口的数据
        # data[5]['token'] = self.token
        res = apiRequests(data[3], data[4], data[5], self.head)  ##发送接口请求
        print(res.json())
        assert res.json().get('msg') == data[6]

    def test_get_teach_class_04(self):
        """获取教学课接口4"""
        data = dateChangeDict(filename, "teach_class", 4)  ##从excel表格里读取接口的数据
        data[5]['token'] = self.token
        res = apiRequests(data[3], data[4], data[5], self.head)  ##发送接口请求
        print(res.json())
        assert res.json().get('msg') == data[6]

    def test_get_teach_class_05(self):
        """获取教学课接口5"""
        data = dateChangeDict(filename, "teach_class", 5)  ##从excel表格里读取接口的数据
        data[5]['token'] =  self.token
        res = apiRequests(data[3], data[4], data[5], self.head)  ##发送接口请求
        print(res.json())
        assert res.json().get('msg') == data[6]

    def test_get_teach_class_06(self):
        """获取教学课接口6"""
        data = dateChangeDict(filename, "teach_class", 6)  ##从excel表格里读取接口的数据
        data[5]['token'] =  self.token
        res = apiRequests(data[3], data[4], data[5], self.head)  ##发送接口请求
        print(res.json())
        assert res.json().get('msg') == data[6]




if __name__ == '__main__':
    pytest.main()