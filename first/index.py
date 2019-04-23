import requests
header={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac 05 X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52 .0.2743. 116 Safari/537.36'}
data={
    'name': 'amoker.wang',
    'age': 18,
}
r =requests.get('http://httpbin.org/get',data)
print(r.json())
print(type(r.json()))