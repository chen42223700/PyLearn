#python和java中 "=="的区别
'''
Java: str1 == str2 可以决定两个字符串变量是否指向同一块物理内存位置。
    这就做 对象同一性，在 Java 中为了比较两个字符串值，你要使用 str1.equals(str2)；
Python: str1 is str2代表对象同一性, str1 == str2 只是代表值相等，相当于java中的str1.equals(str2)
'''
