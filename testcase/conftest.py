
import pytest,sys

# sys.path.append("F:\\automation")
sys.path.append('../../')
from ttxn_api.Config.Api_Data import filename
from ttxn_api.Public.framework import dateChangeDict, apiRequests


@pytest.fixture(scope='module', autouse=True)
def token():
    global token
    head={}
    data_1 = dateChangeDict(filename, "login", 1)  ##从excel表格里读取接口的数据
    res_1 = apiRequests(data_1[3], data_1[4], data_1[5], head)  ##发送接口请求
    data_2 = dateChangeDict(filename, "login", 2)  ##从excel表格里读取接口的数据
    res_2 = apiRequests(data_2[3], data_2[4], data_2[5], head)  ##发送接口请求
    token = res_2.json()["data"]["token"]
    print(token)
    yield token
    pass ## 执行teardown_class的内容

