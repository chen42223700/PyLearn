class A:
    logo = 'Logo A'

class B:
    def __init__(self):
        self.logo = 'Logo B'

a = A()
b = B()
print (a.logo)
print (b.logo)

print(A.__dict__)
print(B.__dict__)
print(a.__dict__)
print(b.__dict__)

'''
输出结果：
Logo A
Logo B
{'__doc__': None, '__weakref__': <attribute '__weakref__' of 'A' objects>, '__module__': '__main__', 'logo': 'Logo A', '__dict__': <attribute '__dict__' of 'A' objects>}
{'__doc__': None, '__init__': <function B.__init__ at 0x0037D348>, '__module__': '__main__', '__weakref__': <attribute '__weakref__' of 'B' objects>, '__dict__': <attribute '__dict__' of 'B' objects>}
{}
{'logo': 'Logo B'}
'''