import urllib.request

response = urllib.request.urlopen('https://www.python.org')
#print(response.read().decode('utf8'))
print(type(response))
print(response.status)
print(response.getheaders())
