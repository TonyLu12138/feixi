#! /usr/bin/env python3
pi = 3.14

print("计算图形面积")
print("输入1计算圆形")
print("输入2计算矩形")
print("输入3计算正方形")

def circle(r):
    return pi*r*r

def rectangle(a,b):
    return a*b

def square(a):
    return a*a

def cul():
    num = int(input("请选择："))
    if num == 1:
        r = float(input("请输入圆的半径：r= "))
        str1 = str(input("请输入单位："))
        print("圆的面积为 ", circle(r),str1)
    elif num == 2:
        a = float(input("请输入矩形的长：a= "))
        b = float(input("请输入矩形的宽：b= "))
        str1 = str(input("请输入单位："))
        print("矩形的面积为", rectangle(a,b),str1)
    elif num == 3:
        a = float(input("请输入正方形的边长：a= "))
        str1 = str(input("请输入单位："))
        print("正方形的面积为 ", square(a),str1)
    else:
        print("非法输入")
        cul()
cul()

