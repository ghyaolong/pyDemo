import http.cookiejar, urllib.request

filename = 'cookies1.txt'
cookie = http.cookiejar.LWPCookieJar(filename)
cookie.load(filename=filename,ignore_discard=True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
print(response.read().decode('utf-8'))
cookie.save(filename)
