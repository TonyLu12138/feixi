#! /usr/bin/env python3

def compare_list(lista, listb):
    element = []
    for i in lista:
        if i in listb and i not in element:
            element.append(i)
    return element

lista = list(input("请输入列表a的元素，元素之间用空格隔开：").split())
listb = list(input("请输入列表b的元素，元素之间用空格隔开：").split())

print(compare_list(lista,listb))
