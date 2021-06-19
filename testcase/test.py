import requests

url='http://dev-api.ixuenong.com/app/login/vcodeRegister'
data={'tel':'14000000000','vcode':'1111'}
headers={'Content-Type':'application/json'}
res = requests.get(url,data,headers=headers)
print(res.text)
print(res.cookies)


