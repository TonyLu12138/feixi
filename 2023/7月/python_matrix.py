#! /usr/bin/env python3
import numpy as np

def matrix(n):
    matrix = np.zeros((n,n),dtype=int) #创建一个nxn的0矩阵
    num = 1  #创建一个变量读数字
    row_start,row_end = 0, n-1  #定义行列
    col_start,col_end = 0, n-1
    while num <= n*n:   #判断num变量要计数到多少，也就是矩阵有多大
        for i in range(col_start, col_end + 1): #从左到右 依次将变量num的值填入矩阵
            matrix[row_start,i]=num  #填数字
            num += 1    
        row_start += 1  
        
        for i in range(row_start, row_end + 1): #从上到下 
            matrix[i,col_end]=num
            num += 1
        col_end -= 1

        for i in range(col_end, col_start-1,-1): #从右到左
            matrix[row_end,i]=num
            num += 1
        row_end -= 1

        for i in range(row_end, row_start-1,-1): #从下到上
            matrix[i,col_start]=num
            num += 1
        col_start += 1
    return matrix

n = int(input("请输入矩阵的阶数："))

print(matrix(n))
