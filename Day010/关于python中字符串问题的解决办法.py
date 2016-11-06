# -*- coding: utf-8 -*-

'''
关于 python一些问题的解决办法
'''
# 1,将字符串类型，list格式的字符穿转换为list
length = '["aaa","str","10"]'

list = []
lst = i.replace("[","").replace("]","").replace('"',"").split(",")
list.append(lst)
print("整理后length为："+str(list))

# 2，将查询语句中的查询字段取出来放入list中
sql = "select aaa,bbb from student"
chksql = sql.split()

n = []
for i in chksql:
    if i == 'from':
        break
    n.append(i)
        
word = n.pop()
print(word)
