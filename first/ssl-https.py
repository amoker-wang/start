import requests
r = requests.get("https://www.12306.cn",verify=False)
print(r.status_code)
