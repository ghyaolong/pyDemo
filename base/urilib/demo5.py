from urllib import request,parse

url = 'http://httpbin.org/post'

headers = {
	 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
	 'Host':'httpbin.org'
}

dict = {
	'name':'Germey'
}

data = bytes(parse.urlencode(dict),encoding='utf-8')

req = request.Request(url,data,headers,method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))