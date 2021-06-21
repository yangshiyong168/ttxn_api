import requests

##获取验证码
# url='https://sit-api.ixuenong.com/api/v3_3_1/wechat/login/sendLoginCode'
# data={'tel':'g7sjeAjLVANwxt09fayllQ%3D%3D','tel_area_id':'CN'}
# res = requests.get(url,data)
# print(res.text)
##验证码登录
# url='https://sit-api.ixuenong.com/api/v3_3_1/wechat/login/vcodeLogin'
# data={'tel':'14000000000','vcode':'1111','tel_area_id':'CN'}
# res = requests.post(url,data)
# print(res.text)
# print(res.json()['data']['token'])

#教学班接口
url='https://sit-api.ixuenong.com/api/v3_3_1/wechat/notice/unreadCounts'
data={'classification':'000100020001','token':'140000000004b74ff0a44a645758f6bc0af51d6db6a'}
res = requests.get(url,data)
print(res.json())

url='https://sit-api.ixuenong.com/api/v3_3_1/wechat/schoolclass/homePageV4'
data={'classification':'000100020001','token':'140000000004b74ff0a44a645758f6bc0af51d6db6a'}
res = requests.get(url,data)
print(res.json())

url='https://sit-api.ixuenong.com/api/v3_3_1/wechat/common/recAd'
data={'category':'schoolClassHome','adCode':'000200020003','classification':'000100020001','token':'140000000004b74ff0a44a645758f6bc0af51d6db6a'}
res = requests.get(url,data)
print(res.json())

url='https://sit-api.ixuenong.com/api/v3_3_1/wechat/schoolclass/msgList'
data={'token':'140000000004b74ff0a44a645758f6bc0af51d6db6a'}
res = requests.get(url,data)
print(res.json())

url='https://sit-api.ixuenong.com/api/v3_3_1/wechat/schoolclass/tabList'
data={'classification':'000100020001','token':'140000000004b74ff0a44a645758f6bc0af51d6db6a'}
res = requests.get(url,data)
print(res.json())

url='https://sit-api.ixuenong.com/api/v3_3_1/wechat/schoolclass/myClassListV4'
data={'page':1,'classification':'000100020001','token':'140000000004b74ff0a44a645758f6bc0af51d6db6a'}
res = requests.get(url,data)
print(res.json())
#
url='https://qiyukf.com/webapi/invite/num'
data={'appKey':'140000000004b74ff0a44a645758f6bc0af51d6db6a'}
res = requests.get(url,data)
print(res.json())

