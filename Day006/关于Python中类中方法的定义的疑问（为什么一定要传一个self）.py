#-*- encoding:utf-8 -*-
import sys
sys.setdefaultencoding("utf8")
#关于Python中类中方法的定义的疑问（为什么一定要传一个self）
'''
类的方法与普通的函数只有一个特别的区别————它们必须有一个额外的第一个参数名称，
但你在调用这个方法时不必为这个参数赋值，Python会提供这个值，
这个变量通常指对象本身，按照惯例它的名字是self。

虽然我们可以给这个参数任何名称，但是强烈建议使用self这个名称。

举一个例子解释这个现象
我们定义了一个类MyClass和一个这个类的实例MyObject，
当我们调用MyObject.method(arg1,arg2)时，
Python自动转为MyClass.method(MyObject,arg1,arg2)
————这就是self的原理

总结：
这就意味这如果你有一个不需要参数的方法，你还是得给这个方法定义一个self参数

可以联系之前类属性和实例属性的例子来看，
Python中实例化一个对象，实例中除了原类中__init__中的操作外，并无其他属性
实例.方法  实际上是去找类中的方法  类.方法
此时，类中就需要一个参数，指代是哪一个实例调的方法
即，第一个方法时代表实例的
'''

#实例

#没有self就会报错
#class Testself:
#    def testself():
#        print('Hello self')
#p = Testself()
#p.testself()

# 输出结果:
# Traceback (most recent call last):
#   File "C:\Python25\Lib\site-packages\pythonwin\pywin\framework\scriptutils.py", line 310, in RunScript
#     exec codeObject in __main__.__dict__
#   File "C:\Users\Lenovo\Desktop\pyLearn\关于Python中类中方法的定义的疑问（为什么一定要传一个self）.py", line 39, in <module>
#     p.testself()
# TypeError: testself() takes no arguments (1 given)

#有self能正常输出
class Testself:
    def testself(self):
        print('Hello self')

p = Testself()
p.testself()
#输出结果：Hello self

'''
把p实例手动送进去，也能正常输出
'''
Testself.testself(p)
#输出结果：Hello self

def testself1():
    print("I Don't need self")

p.testself = testself1
'''
在p.testself = testself1之前
实例p是没有testself属性的，故他会到类中寻找这个testself属性
而执行p.testself = testself1之后
p实例增加了testself属性且指向testself1 故不会到类中寻找testself属性
'''
p.testself()




