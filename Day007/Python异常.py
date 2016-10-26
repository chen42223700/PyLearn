#Python 使用 try...except 来处理异常，使用 raise 来引发异常。
'''
使用不存在的字典关键字 将引发 KeyError 异常。 
搜索列表中不存在的值 将引发 ValueError 异常。 
调用不存在的方法 将引发 AttributeError 异常。 
引用不存在的变量 将引发 NameError 异常。 
未强制转换就混用数据类型 将引发 TypeError 异常
'''

#打开一个不存在的文件
#fsock = open("/notthere","r")
#报错
'''
Traceback (innermost last):
  File "<interactive input>", line 1, in ?
IOError: [Errno 2] No such file or directory: '/notthere'
'''

try:
    fsock = open("/notthere","r")
except IOError:
    print("The file doesn't exist,exiting gracefully")
print("This Line will always print")
