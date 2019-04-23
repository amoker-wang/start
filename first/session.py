import requests
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac 05 X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52 .0.2743. 116 Safari/537.36'}
# requests.get("https://httpbin.org/cookies/set/number/123456789",headers=headers)
# r = requests.get("https://httpbin.org/cookies",headers=headers)
#
#print(r.text)
s = requests.Session()
s.get('https://httpbin.org/cookies/set/number/789748')
r = s.get("https://httpbin.org/cookies")
print(r.text)