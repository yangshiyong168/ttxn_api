import requests

url='https://sit-api.ixuenong.com/api/v3_3_1/wechat/login/sendLoginCode'
data={'tel':'g7sjeAjLVANwxt09fayllQ%3D%3D','tel_area_id':'CN'}
res = requests.get(url,data)
print(res.text)

url='https://sit-api.ixuenong.com/api/v3_3_1/wechat/login/vcodeLogin'
data={'tel':'14000000000','vcode':'1111','tel_area_id':'CN'}
res = requests.post(url,data)
print(res.text)
print(res.json()['data']['token'])


