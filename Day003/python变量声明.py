#变量的赋值
'''
主要是list和tuple的赋值比java增加便捷
特别是可以一次赋多值和连续值赋值
'''
#一次赋多值
v = ('a','b','c')
(x,y,z) = v
print(x)
print(y)
print(z)
#输出结果：a  b  c


#连续值赋值
(MONDAY, TUESDAY, WEDNESDAY, THUSDAY, FRIDAY, SATURDAY, SUNDAY) = range(1,8)
print(MONDAY)
print(TUESDAY)
print(SUNDAY)
#输出结果：1  2  7
