# -*-coding:utf-8-*-
import urllib
import urllib.request
import re

data={}
data['keyword']='本子'
url_values = urllib.parse.urlencode(data)
print(url_values)
url = "http://search.jd.com/Search?"
m = 6
full_url=url+url_values+'&enc=utf-8&qrst=1&rt=1&stop=1&vt=2'+'&page='+'6'
print(full_url)
d=urllib.request.urlopen(full_url).read()
d=d.decode("utf-8",'ignore')
print(d)

f = open('e:/test.txt', 'w')
f.write(d)
f.close()
src='title="(.*?)"'

s=re.findall(src,d)
for m in s:
    print(m)

print('ok')