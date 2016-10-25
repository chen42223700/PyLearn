#关于Python重载方法的测试
class testOverload:
    def a(self):
        print(1)
    def a(self,obj2):
        print(2)

a = testOverload()
a.a(1)
#输出结果：2

a.a()
#输出报错：

# Traceback (most recent call last):
# File "C:\Python25\Lib\site-packages\pythonwin\pywin\framework\scriptutils.py", line 310, in RunScript
#     exec codeObject in __main__.__dict__
#   File "C:\Users\Lenovo\Desktop\pyLearn\testOverload.py", line 9, in <module>
#     a.a()
# TypeError: a() takes exactly 2 arguments (1 given)
#
# 在第二次def a(self,obj2):时，新的a方法已经覆盖了原a方法，此时已经没有对a(self)的引用了！
# 结论：
# Python没有重载

