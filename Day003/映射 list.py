#映射list
li = [1,2,3,4]
print([elem*2 for elem in li])
#输出结果是：[2,4,6,8]
'''
li 是一个将要映射的 list。Python 循环遍历 li 中的每个元素。
对于每个元素均执行如下操作, 首先临时将其值赋给变量 elem,
然后 Python 应用函数 elem*2 进行计算, 最后将计算结果追加到新list 中。 
需要注意是, 对 list 的解析并不改变原始的 list。
'''

#对list中dict的解析
params = {"server":"mpilgrim","database":"master","uid":"sa","pwd":"secret"}
print(params.items())
#输出结果是：[('server', 'mpilgrim'), ('uid', 'sa'), ('database', 'master'), ('pwd', 'secret')]
print([k for k, v in params.items()])
#输出结果是：['server', 'uid', 'database', 'pwd']
print([v for k, v in params.items()])
#输出结果是：['mpilgrim', 'sa', 'master', 'secret']
print(["%s = %s" % (k,v) for k,v in params.items()])
#输出结果是：['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']

