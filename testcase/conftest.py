
import time,os,sys
from datetime import datetime

import pytest,allure
from py.xml import html

# sys.path.append("F:\\automation")
sys.path.append('../../')

def pytest_configure(config):
    """操作Environment"""
    config._metadata["项目名称"] = "微站H5接口测试"  # 添加接口项目名称
    config._metadata['接口地址'] = 'https://sit-api.ixuenong.com/api/v3_3_1/wechat' # 添加接口地址
    config._metadata.pop("JAVA_HOME") # 删除Java_Home
    config._metadata.pop("Packages")  # 删除Packages
    config._metadata.pop("Platform")  # 删除Platform
    config._metadata.pop("Plugins")  # 删除Plugins
    config._metadata.pop("Python")  # 删除Python

@pytest.mark.optionalhook
def pytest_html_results_summary(prefix):
    """添加测试数据人员信息"""
    prefix.extend([html.p("所属部门: 产研中心")])
    prefix.extend([html.p("测试人员: 张三")])


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(2, html.th('Description'))
    cells.insert(3, html.th('Time', class_='sortable time', col='time'))
    cells.pop()

@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.description))
    cells.insert(3, html.td(datetime.utcnow(), class_='col-time'))
    cells.pop()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
    report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")   #设置编码显示中文

