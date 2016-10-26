#os.path模块
import os
path = os.path.join("c:\\music\\ap\\","mahadeva.mp3")
print(path)
#输出结果：c:\music\ap\mahadeva.mp3

path = os.path.expanduser("~")
print(path)
#输出结果：C:\Users\Lenovo

path = os.path.join(os.path.expanduser("~"),"Python")
print(path)
#输出结果：C:\Users\Lenovo\Python
'''
os.path是一个模块的引用；使用哪一个模块要看你正运行在那种平台上，
expanduser将对使用 ~来表示当前用户根目录的路径名进行扩展。
'''


#分割路径名
path = os.path.split("c\\music\\ap\\mahadeva.mp3")
print(path)
#输出结果：('c\\music\\ap', 'mahadeva.mp3')
#split 函数对一个全路径名进行分割，返回一个包含路径和文件名的 tuple。

(filepath,filename) = os.path.split("c\\music\\ap\\mahadeva.mp3")
print(filepath)
#输出结果：c\music\ap
#我们将 split 函数的返回值赋值给一个两个变量的 tuple。每个变量接收到返回 tuple 相对应的元素值。

(shortpath,extension) = os.path.splitext(filename)
print(shortpath)
#输出结果：mahadeva
print(extension)
#输出结果：.mp3
'''
os.path 也包含了一个 splitext 函数，可以用来对文件名进行分割，
并且返回一个包含了文件名和文件扩展名的 tuple。我们使用相同的技术来将它们赋值给独立的变量。 
'''


#列出目录
path = os.listdir("D:\\tools\\OFFICE2013\\KMSpico_Portable\\KMSpico Portable\\sounds\\")
print(path)
#输出结果：['affirmative.mp3', 'begin.mp3', 'complete.mp3', 'diagnostic.mp3', 'enterauthorizationcode.mp3', 'incomingtransmission.mp3', 'inputfailed.mp3', 'inputok.mp3', 'processing.mp3', 'transfer.mp3', 'verified.mp3', 'warning.mp3']

dirname = 'c://'
print(os.listdir(dirname))

print('\n')
list = [f for f in os.listdir(dirname) if os.path.isfile(os.path.join(dirname,f))]
print(list)
#输出结果：['adware.log', 'bdkv_install.log', 'CMS.zip', 'log.txt', 'STARICC.log', '\xb1\xbe\xb5\xd8\xb4\xc5\xc5\xcc (C) - \xbf\xec\xbd\xdd\xb7\xbd\xca\xbd.lnk']
'''
os.path 模块的 isfile 函数，从文件夹中将文件分离出来。isfile 接收一个路径名，
如果路径表示一个文件，则返回 1，否则为 0。
'''

print('\n')
list = [f for f in os.listdir(dirname) if os.path.isdir(os.path.join(dirname,f))]
print(list)
#输出结果：['$360Section', '$Recycle.Bin', '360SANDBOX', 'CMS', 'Documents and Settings', 'DTLFolder', 'Intel', 'MSOCache', 'oracle', 'PerfLogs', 'Program Files', 'Program Files (x86)', 'ProgramData', 'Python25', 'RavBin', 'Recovery', 'System Volume Information', 'temp', 'Users', 'Windows']
'''
os.path 还有一个 isdir 函数，当路径表示一个目录，则返回 1，否则为 0。
你可以使用它来得到一个目录下的子目录列表。
'''

def listDirectory(directory,fileExtList):
    "get list of file info objects for files of particular extension"
    fileList = [os.path.normcase(f)
                for f in os.listdir(directory)]
    fileList = [os.path.join(directory,f)
                for f in fileList
                if os.path.splitext(f)[1] in fileExtList]

'''
这里主要关注的是os.path.normcase() 方法
其功能是根据操作系统的缺省值对大小写进行标准化处理。
例如，在 Windows 和 Mac OS 下，normcase 将把整个文件名转换为小写字母；
而在 UNIX 兼容的系统下，它将返回未作修改的文件名。
'''


#Listing Directories with glob
import glob
list = glob.glob("D:\\tools\\OFFICE2013\\KMSpico_Portable\\KMSpico Portable\\sounds\\*.mp3")
print(list)
'''
输出结果：
['D:\\tools\\OFFICE2013\\KMSpico_Portable\\KMSpico Portable\\sounds\\affirmative.mp3',
'D:\\tools\\OFFICE2013\\KMSpico_Portable\\KMSpico Portable\\sounds\\begin.mp3',
'D:\\tools\\OFFICE2013\\KMSpico_Portable\\KMSpico Portable\\sounds\\complete.mp3',
'D:\\tools\\OFFICE2013\\KMSpico_Portable\\KMSpico Portable\\sounds\\diagnostic.mp3',
'D:\\tools\\OFFICE2013\\KMSpico_Portable\\KMSpico Portable\\sounds\\enterauthorizationcode.mp3',
'D:\\tools\\OFFICE2013\\KMSpico_Portable\\KMSpico Portable\\sounds\\incomingtransmission.mp3',
'D:\\tools\\OFFICE2013\\KMSpico_Portable\\KMSpico Portable\\sounds\\inputfailed.mp3',
'D:\\tools\\OFFICE2013\\KMSpico_Portable\\KMSpico Portable\\sounds\\inputok.mp3',
'D:\\tools\\OFFICE2013\\KMSpico_Portable\\KMSpico Portable\\sounds\\processing.mp3',
'D:\\tools\\OFFICE2013\\KMSpico_Portable\\KMSpico Portable\\sounds\\transfer.mp3',
'D:\\tools\\OFFICE2013\\KMSpico_Portable\\KMSpico Portable\\sounds\\verified.mp3',
'D:\\tools\\OFFICE2013\\KMSpico_Portable\\KMSpico Portable\\sounds\\warning.mp3']
'''
'''
glob 模块,选取一个通配符并且返回文件的或目录的完整路径与之匹配。
这个通配符是一个目录路径加上 "*.mp3", 它将匹配所有的 .mp3 文件。
注意返回列表的每一个元素已经包含了文件的完整路径。
'''


print('\n')
list = glob.glob("D:\\tools\\OFFICE2013\\KMSpico_Portable\\KMSpico Portable\\sounds\\i*.mp3")
print(list)
'''
输出结果：
['D:\\tools\\OFFICE2013\\KMSpico_Portable\\KMSpico Portable\\sounds\\incomingtransmission.mp3',
'D:\\tools\\OFFICE2013\\KMSpico_Portable\\KMSpico Portable\\sounds\\inputfailed.mp3',
'D:\\tools\\OFFICE2013\\KMSpico_Portable\\KMSpico Portable\\sounds\\inputok.mp3']
'''
'''
如果你要查找指定目录中所有以 "s" 开头并以 ".mp3" 结尾的文件, 也可以这么做。
'''

print('\n')
list = glob.glob("D:\\tools\\OFFICE2013\\KMSpico_Portable\\KMSpico Portable\\*\\i*.mp3")
print(list)
'''
输出结果：
['D:\\tools\\OFFICE2013\\KMSpico_Portable\\KMSpico Portable\\sounds\\incomingtransmission.mp3',
'D:\\tools\\OFFICE2013\\KMSpico_Portable\\KMSpico Portable\\sounds\\inputfailed.mp3',
'D:\\tools\\OFFICE2013\\KMSpico_Portable\\KMSpico Portable\\sounds\\inputok.mp3']
'''
'''
现在考查这种情况: 你有一个 KMSpico Portable 目录, 它包含几个子目录, 子目录中包含一些 .mp3 文件。
你可以用两个通配符仅仅调用 glob 一次立刻获得所有这些文件的一个 list。
一个通配符是 "*.mp3" （用于匹配 .mp3 文件）, 另一个通配符是 子目录名本身,
用于匹配 c:\KMSpico Portable 中的所有子目录。 这看上去很简单, 但他蕴含了强大的功能。
'''
