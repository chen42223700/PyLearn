#python中set方法
seq = [1,2,3,1,2,3,'a','hello','a','word']
seq_set = set(seq)
print(seq_set)
#输出结果：set(['a', 1, 2, 3, 'word', 'hello'])

str = 'hello world'
str_set = set(str)
str_set
#输出结果：set([' ', 'e', 'd', 'h', 'l', 'o', 'r', 'w'])

#in/not in,len操作
flag = 'h' in str_set
print(flag)
#输出结果：True

flag = 'a' in str_set
print(flag)
#输出结果：False

length = len(str_set)
print(length)
#输出结果：8

#set的增删操作
s = set()
print(s)
#输出结果：set([])

s.add('x')
#向s中增加元素'x'
print(s)
#输出结果：set(['x'])

s.remove('x')
#从s中删除元素'x'，如果不存在则引发KeyError
print(s)
#输出结果：set([])

seq_set.discard(1)
#如果在set中存在元素1则删除
print(seq_set)
#输出结果：set(['a', 2, 3, 'word', 'hello'])

seq_set.pop()
#删除并返回set中第一个的元素，如果为空则引发KeyEror
print(seq_set)
#输出结果：set([2, 3, 'word', 'hello'])

seq_set.clear()
#删除set中所有元素
print(seq_set)
#输出结果：set([])


#集合操作
set1 = set([1,2])
set2 = set([2,3])

set3 = set1.union(set2)
#求set1和set2的合集
#同 set1|set2
print(set3)
#输出结果：set([1, 2, 3])

set3 = set1.intersection(set2)
#求set1和set2的并集
#同 set1&set2
print(set3)
#输出结果：set([2])

set3 = set1.difference(set2)
#求set1和set2的差集 ：返回一个新的set包含set1中有但是set2中没有的元素
#同 set1-set2
print(set3)
#输出结果：set([1])

set3 = set1.symmetric_difference(set2)
#不知道什么集：返回两个集合中不重复的元素
#同 set1^set2
print(set3)
#输出结果：set([1,3])
