from collections import deque
'''
相比起List deque完成队列的功能更有效率
因为list在队首使用insert 和pop(0)都是效率比较低的
'''
queue = deque(["Eric","Jone","Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue.popleft())     #队首元素出队  输出结果Eric
print(queue)    #输出结果   deque(['Jone', 'Michael', 'Terry', 'Graham'])

'''
在Python爬虫中，为了不重负那些已经爬过的页面，我们需要把爬过的页面的url放在集合中
在每次要爬一个url之前，先看集合里是否存在待爬的url，不存在，我们先把url放入集合中，然后
再去爬这个页面
'''


