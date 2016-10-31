#1，将请求伪装为浏览器（其实就是请求中加个header）
# -*- coding: utf-8 -*-

import urllib.request

url = 'http://www.baidu.com/'
header = {
    'Connection':'Keep-Alive',
    'Accept':'text/html,application/xhtml+xml,*/*',
    'Accept-Language':'en-US,en;q = 0.8.zh-Hans-CN;q = 0.5,zh-Hans;q - 0.3',
    'User-Agent':'Mozilla/5.0(Windows NT 6.3;WOW64;Trident/7.0;rv:11.0) like Gecko'
}
req = urllib.request.Request(url,headers=header)

try:
    oper = urllib.request.urlopen(req,timeout=2)
except:
    print(url + '抓取失败！')

try:
    data = oper.read()
except:
    print(url + '内容读取失败')

# print(data.decode('utf-8','ignore'))
# print(data.decode())

def saveFile(date):
    savePath = 'D:\pyLearn\PyLearn\爬虫\爬虫.txt'
    file  = open(savePath,'wb')
    file.write(data)
    file.close()

saveFile(data)