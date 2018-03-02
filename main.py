#!/usr/bin/python
# coding=utf-8
import func
path = "E:\\workspace\\python_workspace\\CodeCounter\\test\\main.cpp"

if __name__ == '__main__': 
    f = func.getFileReadObj(path)
    lines = f.readlines()
    f.close()
    print(len(lines)) #总行数
    for l in lines:
        print(l)
    # print(lines)