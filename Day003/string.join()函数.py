'''
python  string.join(seq)
语法  'sep'.join(seq)
参数说明：
sep:分割码
seq:要连接的元素序列、字符串、元组、字典

返回值：返回一个已分隔符sep连接各个元素后生成的的字符串（注意！！！返回的是字符串）
'''

#1.对序列进行操作

seq1 = ['hello','good','boy','doiido']
print(' '.join(seq1))
#返回结果是: hello good boy doiido


#2,对字符串进行操作
seq2 = "hello good boy doiido"
print(':'.join(seq2))
#返回结果是: h:e:l:l:o: :g:o:o:d: :b:o:y: :d:o:i:i:d:o

#3,对元组进行操作
seq3 = ('hello','good','boy','doiido')
print(':'.join(seq3))
#返回结果是：hello:good:boy:doiido

#4,对字典进行操作
seq4 = {'hello':1,'good':2,'boy':3,'doiido':4}
print(':'.join(seq4))
#返回结果是：boy:good:doiido:hello


#os.path.join  常用于合并目录
import os
print(os.path.join('/hello/','good/boy/','doiido'))
#返回结果是：/hello/good/boy/doiido

