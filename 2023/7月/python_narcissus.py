#! /usr/bin/env python3

def narcissistic_number():
    narcissistic = []
    for num in range(100,1000):
        sum_ = 0
        temp = num
        while temp >= 1:
            buffer = temp % 10
            sum_ = sum_ + buffer**3
            temp = temp - buffer
            temp = temp/10
        if sum_ == num:
            narcissistic.append(num)
    return narcissistic

print(narcissistic_number())

