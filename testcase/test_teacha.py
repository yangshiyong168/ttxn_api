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

    def test_get_01(self):
        """获取教学课接口1"""
        data = dateChangeDict(filename, "teach_class", 1)  ##从excel表格里读取接口的数据
        data[5]['token'] = self.token
        res = apiRequests(data[3], data[4], data[5], self.head)  ##发送接口请求
        print(res.json())
        assert res.json().get('msg') == data[6]
