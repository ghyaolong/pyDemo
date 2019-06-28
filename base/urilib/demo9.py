from urllib.parse import urlencode

params = {
	'name':'germey',
	'age':22
}


base_url = 'http://www.baidu.com?'
url = base_url + urlencode(params)
print(url)

from urllib.parse import parse_qs

query = 'name=germey&age=22'
print(parse_qs(query))


from urllib.parse import parse_qsl

query = 'name=germey&age=22'
print(parse_qsl(query))


from urllib.parse import quote

keyword = '壁纸'
url = 'https://www.baidu.coms?wd='+quote(keyword)
print(url)


from urllib.parse import unquote

url = 'https://www.baidu.coms?wd=%E5%A3%81%E7%BA%B8'
print(unquote(url))
