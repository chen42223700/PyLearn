#python中类属性和实例属性（java程序员的疑惑）
#详细阅读-->https://segmentfault.com/a/1190000002671941s
'''
首先请看这个例子
'''
class A():
    aaa = 10

#情形1：
obj1 = A()
obj2 = A()
print(obj1.aaa,obj2.aaa,A.aaa)

#情形2:
obj1.aaa += 2
print(obj1.aaa,obj2.aaa,A.aaa)

#情形3：
A.aaa += 3
print(obj1.aaa,obj2.aaa,A.aaa)
'''
情形1的结果：10 10 10
情形2的结果：12 10 10
情形1的结果：12 13 13
'''

'''
先说原因，Python与java不同，python中的类属性不一定是为其实例共享的

python中类属性的获取
有两种方式
一是 类.属性  e.g A.aaa
而是 实例.属性  e.g  obj1.aaa

python中属性的查找机制
python中属性的获取存在一个向上查找的机制。以上面例子来说
python中一切皆对象。从对象的角度来说，A与obj1是两个无关的对象
但是，Python通过下面的查找树建立了类对象A与实例对象obj1、obj2之间的关系
如图：
            AAA
             |
          -------
         |       |
        obj1    obj2

当调用A.aaa，直接获取其属性aaa但是情形1中调用obj1.aaa时，python按照从obj1到AAA的顺序由下到上查找属性aaa。
值得注意的是这时候obj1是没有属性aaa的，于是。python到类A中去查找，成功找到，并显示出来。

而obj1 += 2实际上包含了两个操作：属性获取和属性设置
即：obj1.aaa = obj1.aaa + 2
其中等式右侧的obj1.aaa属于属性获取，其本质就是按上述查找机制找到aaa的值，
然后运算后在赋值给等式左边的obj1.aaa 即属性设置
注意，在属性设置时，obj1实例并没有属性aaa，因此会自身动态添加一个属性aaa。

此时obj1.aaa已经不指向A.aaa了，obj1.aaa指向自身的属性aaa，

总结：
1、Python中属性的获取是按照从下到上的顺序来找属性
2、python中的类和实例是两个完全独立的对象
3、Python中的属性设置时正对对象本身进行的
'''

#以下是上述结论的实例证明
obj1 = A()
obj2 = A()

print(obj1.__dict__)
#输出结果是 {}
print(obj2.__dict__)
#输出结果是 {}

obj1.aaa += 2
obj1.aaa = 3
print(obj1.__dict__)
#输出结果是 {'aaa':3}
print(obj2.__dict__)
#输出结果是 {}
print(A.__dict__)
#输出结果是{'__module__': '__main__', 'aaa': 13, '__doc__': None}

'''
要点总结
1、理解Python是如何利用查找树的机制来模仿类及实例之间的关系
2、理解动态语言是可以动态设置属性的
'''
