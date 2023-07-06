#! /usr/bin/env python3

import re
import numpy as np

text = input("请输入一段文本：")
list_result = re.split(r'[?]*\s+|[.]\r+',text)
print(list_result)
list_result_unique = np.unique(list_result)  #创建一个不重复元素列表


for i in range(len(list_result_unique)):  #判断并计数
    number_ = 0
    buffer = list_result_unique[i]
    for j in range(len(list_result)):
        if list_result_unique[i] == list_result[j]:
            number_+=1
    print(list_result_unique[i],":",number_)
