#python静态方法及类方法的定义
class testStatic:
    @staticmethod #静态方法要加此代码  其它特性同java
    def method():
        '''
        注，静态方法不用加self参数
        '''
        print("I'm static method")

testStatic.method()
#输出结果：I'm ststic method

class testClass:
    @classmethod   #类方法要加此代码
    def method(cls):
        '''
        注：类方法的参数是 '类对象'
        '''        
        print("I'm class method")

testClass.method()
#输出结果：I'm class method

#静态方法和实例方法的区别
class A(object):
    "This is A Class"

    @staticmethod
    def Foo1():
        print("Call Static method foo1()\n")

    @classmethod    
    def Foo2(cls):
        print("Call class method foo2()")
        print("cls.__name__ is "+cls.__name__)

A.Foo1()
A.Foo2()
'''
类方法中的参数 cls 是一个类
故可以通过cls访问类的属性
'''



#实例方法测试
class testNotStatic:
    def method(self):
        print("I'm not ststic method")

#testNotStatic.method()
#输出报错

# Traceback (most recent call last):
#   File "C:\Python25\Lib\site-packages\pythonwin\pywin\framework\scriptutils.py", line 310, in RunScript
#     exec codeObject in __main__.__dict__
#   File "C:\Users\Lenovo\Desktop\pyLearn\python静态方法的定义.py", line 15, in <module>
#     testNotStatic.method()
# TypeError: unbound method method() must be called with testNotStatic instance as first argument (got nothing instead)


#实例方法需要先实例化，才能调用
a = testNotStatic()
a.method()
#输出结果：I'm not ststic method

