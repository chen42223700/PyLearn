def buildConnectionString(params):
    """Build a connection string from a dictionary of parameters.

    Returns string."""
    return ";".join(["%s=%s" % (k, v) for k, v in params.items()])

if __name__ == "__main__":
    '''
    关于 name == "__main__"的注释
    所有的模块都有一个内置属性__name__。一个模块的__name__的值要看我们是如何人应用
    模块。
    ①：如归是import模块，那么__name__的值通常为模块的文件名，
    不带路径或者文件扩展名。
    ②：如果像一个标准的程序直接运行模块，此时__name__的值将是一个缺省值__main__。
    '''
    myParams = {"server":"mpilgrim", \
                "database":"master", \
                "uid":"sa", \
                "pwd":"secret" \
                }
    buildConnectionString(myParams)

#以下是关于__name__ == "__main__"的例子
print (__name__)
#直接运行 print __name__ 执行结果是 __main__
import odbchelper
print (odbchelper.__name__)
#运行结果是 odbchelper 为模块的文件名