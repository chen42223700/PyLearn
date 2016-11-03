# -*- coding: utf-8 -*-

import os

li = [
    [1111,2222,3333],
    [4444,5555,6666],
    [7777,8888,9999]
]

path = "D:\\pyLearn\\PyLearn\\Day009\\"
if not os.path.exists(path):
    os.mkdir(path)

file = open(path + "file.txt","w")
string = ""
for i in li:
    for j in i:
        string += str(j) + "|"
    string = string[:-1] + "\n"
    file.write(string)
    string = ""

file2 = open(path + "file2.txt","w")
for i in li:
    for j in i:
        if len(str(j)) > 10:
            break
        string += str(j).ljust(10,' ')
    string += "\n"
    print(string)
    file2.write(string)
    string = ""


