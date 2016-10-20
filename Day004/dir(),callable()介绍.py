#dir 介绍
'''
dir 函数返回任意对象的属性和方法列表，包括模块对象、函数对象、字符串对象、列表对象、字典对象 …… 相当多的东西。
'''

li = []
#print(dir(li))
'''
输出结果太多省略
结果是：list的所有属性和方法
'''

import odbchelper_re
print(dir(odbchelper_re))
'''
输出结果：
['__author__', '__builtins__', '__copyright__', '__date__', '__doc__', '__file__', '__license__', '__name__', '__version__', 'buildConnectionString']
odbchelper_re 是一个模块，
所以 dir(odbchelper) 返回模块中定义的所有部件的列表，包括内置的属性，
例如 __name__，__doc__, 以及其它你所定义的属性和方法
'''



#callable介绍
import string
print(string.punctuation)
'''
输出结果是：
!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
'''

print(callable(string.punctuation))
'''
输出结果是：
False
'''

print(str.join)
'''
输出结果是：
<method 'join' of 'str' objects>
'''

print(callable(str.join))
'''
输出结果是：
True
'''
