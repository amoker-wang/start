import requests
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac 05 X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52 .0.2743. 116 Safari/537.36'}
r = requests.get("https://www.baidu.com",headers=headers)
print(r.cookies)
for key, value in  r.cookies.items() :
    print(key + '=' + value )