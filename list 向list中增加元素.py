#list 向 list 中增加元素(list.append(object),list.insert(index,object),list.extend(list))
li = ['a', 'b', 'mpilgrim', 'z', 'example']
li.append("new")
print (li)
#输出是['a', 'b', 'mpilgrim', 'z', 'example', 'new']

li.insert(2,"new")
print (li)
#输出是['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new']
'''
insert 将单个元素插入到 list 中。数值参数是插入点的索引。
请注意, list 中的元素不必唯一, 现在有两个独立的元素具有 'new' 这个值,
li[2] 和 li[6]。
'''

li.extend(["two","elements"])
print (li)
#输出是['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new', 'two', 'elements']
'''
extend 用来连接 list。请注意不要使用多个参数来调用 extend,
要使用一个 list 参数进行调用。
'''

#extend (扩展) 与 append (追加)的差别
#extend
li = ['a', 'b', 'c']
li.extend(['d', 'e', 'f'])
print (li)
#输出是 ['a', 'b', 'c', 'd', 'e', 'f']

#append
li = ['a', 'b', 'c']
li.append(['d', 'e', 'f'])
print (li)
#输出是 ['a', 'b', 'c', ['d', 'e', 'f']]
'''
1  Lists 的两个方法 extend 和 append 看起来类似, 但实际上完全不同。 extend 接受一个参数, 这个参数总是一个 list, 并且添加这个 list 中的每个元素到原 list 中。
2  在这里 list 中有 3 个元素 ('a', 'b' , 'c'), 并且使用另一个有 3 个元素 ('d', 'e' , 'f') 的 list 扩展之, 因此新的 list 中有 6 个元素。
3  另一方面, append 接受一个参数, 这个参数可以是任何数据类型, 并且简单地追加到 list 的尾部。 在这里使用一个含有 3 个元素的 list 参数调用 append 方法。
4  原来包含 3 个元素的 list 现在包含 4 个元素。 为什么是 4 个元素呢? 因为刚刚追加的最后一个元素 本身是个 list。 List 可以包含任何类型的数据, 也包括其他的 list。 这或许是您所要的结果, 或许不是。 如果您的意图是 extend, 请不要使用 append

'''


