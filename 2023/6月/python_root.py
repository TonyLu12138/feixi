#! /usr/bin/env python3
import cmath

print("计算平方根")

def root(num):
    square_root = cmath.sqrt(num)
    return square_root

R = int(input("请输入实部："))
I = int(input("请输入虚部："))

number = complex(R,I)

root_result = root(number)

print("复数的平方根：",root_result," and ",-root_result)
if root_result.real == 0:
    print("实部的平方根：",root_result.real)
else:
    print("实部的平方根：",root_result.real," and ",-root_result.real)
if root_result.imag == 0:
    print("虚部的平方根：",root_result.imag)
else:
    print("虚部的平方根：",root_result.imag," and ",-root_result.imag)
