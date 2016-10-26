#python文件处理

#打开文件
f = open("D:\\tools\\OFFICE2013\\KMSpico_Portable\\KMSpico Portable\\sounds\\affirmative.mp3","rb")
print(f)
# 输出结果：
#<open file 'D:\tools\OFFICE2013\KMSpico_Portable\KMSpico Portable\sounds\affirmative.mp3', mode 'r' at 0x0722EDA0>

print(f.mode)
# 输出结果：
#r
#D:\tools\OFFICE2013\KMSpico_Portable\KMSpico Portable\sounds\affirmative.mp3

print(f.name)
# 输出结果：
#D:\tools\OFFICE2013\KMSpico_Portable\KMSpico Portable\sounds\affirmative.mp3

#读取文件
print(f.tell())
# 输出结果：0
'''
一个文件对象维护它所打开文件的状态。文件对象的 tell 方法告诉你在打开文件中的当前位置。
因为我们还没有对这个文件做任何事，当前位置为 0，它是文件的开始处。
'''

f.seek(-128,2)
print(f.tell())
# 输出结果：4416
'''
文件对象的 seek 方法在打开文件中移动到另一个位置。
第二个参数指出第一个参数是什么意思：
0 表示移动到一个绝对位置 （从文件开始算起），
1 表示移到一个相对位置 （从当前位置算起），
2 表示对于文件尾的一个相对位置。
'''

f.seek(0)
tagDate = f.read()
'''
read 方法从打开文件中读取指定个数的字节，并且返回含有读取数据的字符串。
可选参数指定了读取的最大字节数。如果没有指定参数，read 将读到文件末尾。
（我们本可以在这里简单地说一下 read() ，因为我们确切地知道在文件的何处，事实上，我们读的是最后 128 个字节。）
读出的数据赋给变量 tagData，并且当前的位置根据所读的字节数作了修改。
'''
print(tagDate+"\n")
print(f.tell())



#关闭文件
print(f.closed)
# 输出结果：False
'''
文件对象的 closed 属性表示对象是否打开或关闭了文件。
'''
f.close()
'''
调用文件对象的 close 方法。这样就释放掉你加在文件上的锁 （如果有的话），
刷新被缓冲的系统确实还未写入的输出 （如果有的话），并且释放系统资源。
'''
print(f.closed)
# 输出结果：True


#写入文件
logfile = open('test.log','w')
logfile.write('test succeeded')
logfile.close()
detail = file('test.log').read()
#file 是 open 的同义语。 它用一行打开文件, 读取内容, 并打印它们。
print(detail)
# 输出结果：test succeeded

logfile = open('test.log','a')
logfile.write('\nline 2')
logfile.close()
detail = file('test.log').read()
print(detail)
# 输出结果：
#test succeeded
#line 2

'''
"a" 参数的意思是为追加目的打开文件。
实际上即使文件不存在你也可以这样做, 因为以追加方式打开一文件时, 如果需要的话会创建文件。
但是追加操作 从不 损坏文件的现有内容。
'''
