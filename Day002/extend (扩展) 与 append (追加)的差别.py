# 1,extend(扩展)
li = ['a', 'b', 'c']
li.extend(['d', 'e', 'f'])
print(li)
#输出结果：['a', 'b', 'c', 'd', 'e', 'f']

# 2,append（追加）
li = ['a', 'b', 'c']
li.append(['d', 'e', 'f'])
print (li)
#输出结果：['a', 'b', 'c', ['d', 'e', 'f']]
'''
extend 接受的参数总是一个 list, 并且添加这个 list 中的每个元素到原 list 中。
在这里 list 中有 3 个元素 ('a', 'b' , 'c'), 并且使用另一个有 3 个元素 ('d', 'e' , 'f') 的 list 扩展之,
因此新的 list 中有 6 个元素。
另一方面, append 的参数可以是任何数据类型, 并且简单地追加到 list 的尾部。
在这里使用一个含有 3 个元素的 list 参数调用 append 方法。
只是把list作为一个整体加入到li尾部。

注！！！append可以使用认可参数类型
'''
