from urllib.parse import urlparse

result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result),result)

from urllib.parse import urlunparse

data = ['http','www.baidu.com','index.html','user','a=6','comment']
print(urlunparse(data))

from urllib.parse import urlsplit


result = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
print(result)




from urllib.parse import urlunsplit

data=['http','www.baidu.com','index.html','a=6','comment']
print(urlunsplit(data))