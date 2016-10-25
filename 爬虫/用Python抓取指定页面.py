#实现url下载功能
# 1，关键方法
from  urllib import request
'''
注！！！
在python2.x中有urllib2模块，故直接import urllib2即可
而在python3.x中urllib3.x中 urllib2已经合并到urllib中的5个子模块中
本环境是python3.x

以下是对python3.x下该模块的总结
官方文档：
a new urllib package was created. It consists of code from
urllib, urllib2, urlparse, and robotparser. The old
modules have all been removed. The new package has five submodules:
urllib.parse, urllib.request, urllib.response,
urllib.error, and urllib.robotparser. The
urllib.request.urlopen() function uses the url opener from
urllib2. (Note that the unittests have not been renamed for the
beta, but they will be renamed in the future.)

3.0版本中已经将urllib2、urlparse、和robotparser并入了urllib中，
并且修改urllib模块，其中包含5个子模块，即是help()中看到的那五个名字。

为了今后使用方便，在此将每个包中包含的方法列举如下：
 urllib.error: ContentTooShortError; HTTPError; URLError

urllib.parse: parse_qs; parse_qsl; quote; quote_from_bytes; quote_plus; unquote unquote_plus; unquote_to_bytes; urldefrag; urlencode; urljoin; urlparse; urlsplit; urlunparse; urlunsplit

urllib.request: AbstractBasicAuthHandler; AbstractDigestAuthHandler; BaseHandler; CatheFTPHandler; FTPHandler; FancyURLopener; FileHandler; HTTPBasicAuthHandler; HTTPCookieProcessor; HTTPDefaultErrorHandler; HTTPDigestAuthHandler; HTTPErrorProcessorl; HTTPHandler; HTTPPasswordMgr; HTTPPasswordMgrWithDefaultRealm; HTTPRedirectHandler; HTTPSHandler;OpenerDirector;ProxyBasicAuthHandler ProxyDigestAuthHandler; ProxyHandler; Request; URLopener; UnknowHandler; build_opener; getproxies; install_opener; pathname2url; url2pathname; urlcleanup; urlopen; urlretrieve;

urllib.response: addbase; addclosehook; addinfo; addinfourl;

urllib.robotparser: RobotFileParser
'''

#直接请求
#该方法会下载传入的网页并返回给response
url = 'http://baidu.com'
response = request.urlopen(url)

#获取状态码，如果是200表示获取成功
print(response.getcode())

#读取内容
cont = response.read()
print(cont)

#urlopen()简介
#urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False)
'''
该函数返回一个http.client.HTTPResponse对象，
'''
a = request.urlopen(url)
print(type(a))
print(a.geturl())
print(a.info())