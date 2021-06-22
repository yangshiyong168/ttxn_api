
import time,os,sys
import pytest,allure
from py.xml import html

sys.path.append("F:\\automation")
sys.path.append('../../')

def pytest_configure(config):
    # 添加接口地址与项目名称
    config._metadata["项目名称"] = "微站H5接口测试"
    config._metadata['接口地址'] = 'https://sit-api.ixuenong.com/api/v3_3_1/wechat'
    # 删除Java_Home
    config._metadata.pop("JAVA_HOME")

@pytest.mark.optionalhook
def pytest_html_results_summary(prefix):
    prefix.extend([html.p("所属部门: 产研中心")])
    prefix.extend([html.p("测试人员: 张三")])

