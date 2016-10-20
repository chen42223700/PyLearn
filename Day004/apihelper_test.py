from apihelper import info
li = []
info(li)
'''
info 函数的设计意图是提供给工作在 Python IDE 中的开发人员使用，
它可以使用任何含有函数或者方法的对象（比如模块，含有函数，又比如list，含有方法）
作为参数，并打印出对象的所有函数和它们的 doc string

由于返回结果太多，省略结果
结果是List所有可调用方法的__doc__
'''

import odbchelper_re
info(odbchelper_re)
'''
输出结果：
buildConnectionString Build a connection string from a dictionary Returns string.
'''

info(odbchelper_re,30)
'''
输出结果：
buildConnectionString          Build a connection string from a dictionary Returns string.
'''
'''
输出结果：
buildConnectionString          Build a connection string from a dictionary Returns string.
'''

info(odbchelper_re,30,0)
'''
输出结果：
buildConnectionString          Build a connection string from a dictionary
    
    Returns string.
'''


