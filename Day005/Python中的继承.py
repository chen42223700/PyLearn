#Python中的继承
from UserDict import UserDict

class FileInfo(UserDict):
    "store files metadata"
    def __init__(self,filename = None):
        UserDict.__init__(self)    #注1
        self["name"]= filename
'''
这就是 FileInfo 继承自UserDict的类.
在 Python 中，类的继承只是简单地列在类名后面的小括号里。不象在 Java 中有一个特殊的象 extends 的关键字。
Python 支持多重继承。在类名后面的小括号中，你可以列出许多你想要的类名，以逗号分隔。

__init__ 在类的实例创建后被立即调用。 类似java中的构造函数

习惯上，任何 Python 类方法的第一个参数（对当前实例的引用）都叫做 self。
这个参数扮演着 C++ 或 Java 中的保留字 this 的角色，但 self 在 Python 中并不是一个保留字，它只是一个命名习惯。
虽然如此，也请除了 self 之外不要使用其它的名字，这是一个非常坚固的习惯。


注1：这里与java有很大不同：
在java中，向上造型会自动执行父类和子类的构造方法
在python中，必须显示地调用在父类中的适合方法。否则父类中的构造__init__方法不会被执行
'''