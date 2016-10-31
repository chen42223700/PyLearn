# -*- coding: utf-8 -*-

import re
import urllib.request
import urllib

from collections import deque

queue = deque()  #记录待爬的url
visited = set()  #记录已经爬过的url

url = 'http://news.dbanotes.net'  #入口页面

queue.append(url)
cnt = 0

while queue:
    url = queue.popleft() #队首元素出队
    visited |= {url}   #visited = visited | {url} 标记为已访问

    print('已经抓取：'+str(cnt)+'    正在抓取<----   '+ url)
    cnt += 1
    try:
        urlopen = urllib.request.urlopen(url,timeout=2)#超市时间为2s
    except:
        print(url + "抓取失败！")
        continue

    if 'html' not in urlopen.getheader('Content-Type'):
        continue

    # 避免程序异常终止，用try ...catch处理异常
    try:
        data = urlopen.read().decode('utf-8')
    except:
        continue

    # 正则表达式提取页面中所有队列，并判断是否已经访问过，然后加入待爬队列
    linker = re.compile('href="(.+?)"')
    for x in linker.findall(data):
        if 'http' in x and x not in visited:
            queue.append(x)
            print('加入队列 --->    ' +   x)



