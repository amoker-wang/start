import requests
from requests.auth import HTTPBasicAuth
r = requests.get('https://www.taobao.com',auth=HTTPBasicAuth('username', 'password'))
print(r.text)