import http.cookiejar
import urllib.request
'''
getOpener函数接受一个head参数，这个参数是一个字典，函数
把字典转换成元祖集合，放假opener

功能：
1.自动处理使用opener过程中遇到的Cookies
2,自动在发出的GET或POST请求中加上自定义的Header
'''
def getOpener(head):
    # 处理cookies
    cj = http.cookiejar.CookieJar()
    pro = urllib.request.HTTPCookieProcessor(cj)
    opener = urllib.request.build_opener(pro)
    header = []
    for key,values in head.items():
        elem = (key,values)
        header.append(elem)

    opener.addheaders = header
    return  opener