#!/usr/bin/env python3

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

bool1 = True
print("输入1,x和y相加")
print("输入2,x和y相减")
print("输入3,x和y相减")
print("输入4,x和y相除")
intlist = [1,2,3,4]
while bool1:
    str1 = str(input("是否开始计算[Y/y]"))
    if str1 == "Y" or str1 == "y":
        num=int(input("请输入:[1/2/3/4]"))
        if num not in intlist:
            print("非法输入")
        else:
            print("请输入x和y的值")
            x = int(input("x= "))
            y = int(input("y= "))
               
            if num == 1:
                if y < 0:
                    print(x," + ","(",y,")"," = ",add(x,y))
                else:
                    print(x," + ",y," = ",add(x,y))
            elif num == 2:
                if y < 0:
                    print(x," - ","(",y,")"," = ",sub(x,y))
                else:
                    print(x," - ",y," = ",sub(x,y))
            elif num == 3:
                if y < 0:
                    print(x," * ","(",y,")"," = ",mul(x,y))
                else:
                    print(x," * ",y," = ",mul(x,y))
            elif num == 4:
                if y != 0:
                    if y < 0:
                        print(x," / ","(",y,")"," = ",div(x,y))
                    else:
                        print(x," / ",y," = ",div(x,y))
                elif x > 0:
                    print(x," / ",y," = ","+∞")
                elif x < 0:
                    print(x," / ",y," = ","-∞")
    else:
        bool1 = False
print("计算结束")
