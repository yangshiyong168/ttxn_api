#coding=utf-8
import pytest,os,json,allure,sys
from ddkt_api.Public.framework import *
sys.path.append("C:\\automation")

class Test_Courses(object):
    """约课/上课模块接口"""

    @classmethod
    def setup_class(cls):
        cls.head = {"ddversion": ddversion, "ddclient": ddclient}
        data = readExcel(filename, "token", 1)
        cls.head["ddtoken"] = data[0]

    @classmethod
    def teardown_class(cls):
        pass

    def test_get_class_list_ad(self):
        """获取上课列表广告接口"""
        data = readExcel(filename, "yueke_attendClass", 1)  ##从excel表格里读取接口的数据
        req_data = encryption(filename, "yueke_attendClass", 1)  ##获取需要传输的参数
        res = apiRequests(data[3], data[4], req_data, self.head)  ##发送接口请求
        assert data[6] in res.text



if __name__ == '__main__':
    pytest.main()