def info(object,spacing = 10,collapse = 1):
    """
    print method and doc strings
    Takes methods and doc strings
    """
    methodList = [method for method in dir(object) if callable(getattr(object,method))]
    processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
    print ("\n".join(["%s %s" %
                        (method.ljust(spacing),
                         processFunc(str(getattr(object,method).__doc__)))
                     for method in methodList]))


if __name__ == "__main__":
    print (info.__doc__)


# 使用可选参数和命名参数
'''
Python 允许函数参数有缺省值；如果调用函数时不使用参数，参数将获得它的缺省值。
此外，通过使用命名参数还可以以任意顺序指定参数
'''
'''
如上例所示：
def info(object, spacing=10, collapse=1):
spacing 和 collapse 是可选参数，因为它们已经定义了缺省值。
object 是必备参数，因为它没有指定缺省值。
如果调用 info 时只指定一个参数，那么 spacing 缺省为 10 ，collapse 缺省为 1。
如果调用 info 时指定两个参数，collapse 依然默认为 1。

假如你要指定 collapse 的值，但是又想要接受 spacing 的缺省值。
在绝大部分语言中，就需要重写该方法了了。
但是在 Python 中，参数可以通过名称以任意顺序指定。
'''

#e.g
#info(odbchelper)
'''
只使用一个参数，spacing 使用缺省值 10 ，collapse 使用缺省值 1。
'''

#info(odbchelper, 12)
'''
使用两个参数，collapse 使用缺省值 1。
'''

#info(odbchelper, collapse=0)
'''
这里你显式命名了 collapse 并指定了它的值。spacing 将依然使用它的缺省值 10。
'''

#info(spacing=15, object=odbchelper) 
'''
必备参数 (例如 object，没有指定缺省值) 也可以采用命名参数的方式,
而且命名参数可以以任意顺序出现。
'''
