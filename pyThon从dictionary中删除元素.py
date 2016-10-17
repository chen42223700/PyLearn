# pyThon从 dictionary 中删除元素
d = {'server': 'mpilgrim', 'uid': 'sa', 'database': 'master',42: 'douglas', 'retrycount': 3}
#del dict[key] 使用 key 从一个 dictionary 中删除独立的元素
del d[42]
#dict.clear()  clear 从一个 dictionary 中清除所有元素。