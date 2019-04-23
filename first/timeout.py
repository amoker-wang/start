import requests
r = requests.get('https://www.taobao.com',timeout=1)
print(r.text)