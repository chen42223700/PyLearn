import re
def getXSRF(data):
    cer = re._compile('name = "_xsrf" value = "(.*)"',flags = 0)
    strlist = cer.findall(data)
    return  strlist[0]

