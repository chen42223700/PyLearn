#getattr()介绍

li = ["Larry","Curly"]
print(li.pop)
'''
输出结果：
<built-in method pop of list object at 010DF884>
'''

print(getattr(li,"pop"))
'''
输出结果：
<built-in method pop of list object at 010DF884>
'''

'''
li.pop和getattr(li,"pop")都是获取对pop方法的引用。
getattr可以返回任何对象的任何属性。
在这个例子中，对象是一个 list，属性是 pop 方法。
'''


'''
在下面的例子中：
getattr 的返回值 是 方法，然后你就可以调用它就像直接使用 li.append("Moe") 一样。
但是实际上你没有直接调用函数；只是以字符串形式指定了函数名称。
理论上，getattr 可以作用于元组，但是由于 元组没有方法，
所以不管你指定什么属性名称 getattr 都会引发一个异常。

个人理解，getattr可以返回指定属性的"引用"，通过这个"引用"，我们可以访问所任何属性
'''
getattr(li,"append")("Moe")
print(li)
'''
输出结果：
["Larry", "Curly", "Moe"]
'''

'''
getattr同样可作用于模块
'''
import odbchelper_re
print(getattr(odbchelper_re,"buildConnectionString"))
'''
输出结果：
<function buildConnectionString at 0x07132330>
'''
