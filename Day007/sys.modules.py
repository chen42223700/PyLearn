#sys.modules
import sys
print ('\n'.join(sys.modules.keys()))
'''
这个sys模块包含了系统级的信息，例如正在运行的python版本（sys.version 或 s.version_info）
以及最大运行递归的深度(sys.getrecursionlimit()和sys.setrecursionlimit())

sys.modules是一个字典，它包含了从Python开始运行起，被导入的所有模块对象。
请注意除了你的程序导入的模块外还有其它模块。Python在启动时预先装入了一些模块，如果你在一个PythonIDR的环境下，
sys.modules包含了你在IDE中运行的所有程序所导入的所有模块
'''

import fileinfo
print ('\n'.join(sys.modules.keys()))
print('\n')
print(fileinfo)
#输出结果：<module 'fileinfo' from 'C:\Users\Lenovo\Desktop\pyLearn\fileinfo.py'>ules['fileinfo'])
print(sys.modules['fileinfo'])
#输出结果：<module 'fileinfo' from 'C:\Users\Lenovo\Desktop\pyLearn\fileinfo.py'>ules['fileinfo'])


#__module__类属性
from fileinfo import MP3FileInfo
print('\n')
print(MP3FileInfo.__module__)
#输出结果：fileinfo
#每个 Python 类拥有一个内置的 类属性 __module__，它定义了这个类的模块的名字。
print(sys.modules[MP3FileInfo.__module__])
#输出结果：<module 'fileinfo' from 'C:\Users\Lenovo\Desktop\pyLearn\fileinfo.py'>ules['fileinfo'])


#fileinfo.py 中的 sys.modules
def getFileInfoClass(filename,module = sys.modules[FileInfo.__module__]):
    "get File info class from filename extension"
    subclass = "%sFileInfo" % os.path.splitext(filename)[1].upper()[1:]
    return hasattr(module,subclass) and getattr(module,subclass) or FileInfo
'''
值得注意的是这句代码：
return hasattr(module,subclass) and getattr(module,subclass) or FileInfo
它的意思是:
If this module has the class named by subclass then return it, otherwise return the base class FileInfo 
'''
