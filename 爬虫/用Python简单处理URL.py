#! /usr/bin/env python
# -*- coding: utf-8 -*-
#encoding:UTF-8

import urllib
import urllib.request

'''
抓取百度上面搜索关键词为Jecvay Notes的网页，则代码如下
'''
data = {}
data['word'] = 'Jecvay Notes'

url_values = urllib.parse.urlencode(data)
'''
data是一个字典, 然后通过urllib.parse.urlencode()来将data转换为 'word=Jecvay+Notes'的字符串,
最后和url合并为full_url
'''
url = 'http://www.baidu.com/s?'
full_url = url + url_values

rsp = urllib.request.urlopen(full_url)
data = rsp.read()
print(rsp.info())
'''
输出结果是：
Content-Type: text/html
Cache-control: no-cache
Pragma: no-cache
Content-Encoding: gzip
Set-Cookie: A^`=1477320659vpVA001626960; expires=Thu,31-Dec-2026 15:59:59 GMT; path=/; domain=www.baidu.com; HttpOnly
Content-length: 1364
Connection: close

注意：Content-Encoding: gzip
以gzip方式压缩了，故直接decode（’utf-8‘）会报错
要先解压，再decode
'''

print(rsp.geturl())

# def unzip(data):
#     import gzip
#     import io
#     # from io import StringIO
#     data = io.StringIO(data)
#     gz = gzip.GzipFile(fileobj=data)
#     data = gz.read()
#     gz.close()
#     return data

# data = unzip(rsp)

data = data.decode("utf-8",'ignore')
print(data)