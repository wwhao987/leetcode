#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/26 22:03
# @Author  : 朱紫宇
# @File    : Fibonacci.py
# @Software: PyCharm
# 0,1,1,2,3
def fibonacci(n):
    """
    time complex:o(N)
    space complex:O(1)
    :param n:
    :return:
    """
    a = 0
    b = 1
    if n < 0:
        return "error"
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n + 1):
            a, b = b, a + b
            # c=a+b
            # a=b
            # b=c
        return b


# recursive

def fib(n):
    """
    time complex:exponential
    space complex:O(N)
    :param n:
    :return:
    """
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


# dynamic programing
def fib_dy(n):
    """
    space complex changed time
        Time complexity: O(n) for given n
        Auxiliary space: O(n)
    :param n:
    :return:
    """
    f = [0, 1]
    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f[n]


# a approach of matrix
# Fibonacci Series using
# Optimized Method

# function that returns nth
# Fibonacci number


def fibs(n):
    F = [[1, 1],
         [1, 0]]
    if (n == 0):
        return 0
    power(F, n - 1)

    return F[0][0]


def multiply(F, M):
    x = (F[0][0] * M[0][0] +
         F[0][1] * M[1][0])
    y = (F[0][0] * M[0][1] +
         F[0][1] * M[1][1])
    z = (F[1][0] * M[0][0] +
         F[1][1] * M[1][0])
    w = (F[1][0] * M[0][1] +
         F[1][1] * M[1][1])

    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w


# Optimized version of
# power() in method 4


def power(F, n):
    if (n == 0 or n == 1):
        return
    M = [[1, 1],
         [1, 0]]

    power(F, n // 2)
    multiply(F, F)

    if (n % 2 != 0):
        multiply(F, M)


# formula
def fib_formula(n):
    """
    o(log(n))
    Auxiliary Space: O(Log n) if we consider the function call stack size, otherwise O(1).
    :param n:
    :return:
    """
    if n <= 1:
        return n
    return int(1 / (5 ** 0.5) * (((1 + 5 ** 0.5) / 2) ** n - (((1 - 5 ** 0.5) / 2) ** n)))


if __name__ == '__main__':
    n = 7
    print(f"base of for loop:{fibonacci(n)}")
    print(f"base of recursive:{fib(n)}")
    print(f"base of dynamic:{fib_dy(n)}")
    print(f"base of matrix:{fibs(n)}")
    print(f"base of formula:{fib_formula(n)}")
