#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/26 23:02
# @Author  : 朱紫宇
# @File    : NonConsectiveFibnaciiNumber.py
# @Software: PyCharm
# Python program for Zeckendorf's theorem. It finds
# representation of n as sum of non-neighbouring
# Fibonacci Numbers.

# Returns the greatest Fibonacci Number smaller than
# or equal to n.
# 0 1 1 2 3 5 8 13 21 30
# 30-21=9
# n =9
def nearestSmallerEqFib(n):
        """
        1) Let n be input number

        2) While n >= 0
             a) Find the greatest Fibonacci Number smaller than n.
                Let this number be 'f'.  Print 'f'
             b) n = n - f
        :param n:
        :return:
        """

        if (n == 0 or n == 1):
            return n

        # Finds the greatest Fibonacci Number smaller
        # than n.
        f1, f2, f3 = 0, 1, 1
        while (f3 <= n):
            f1 = f2;
            f2 = f3;
            f3 = f1 + f2;
        return f2;


# Prints Fibonacci Representation of n using
# greedy algorithm
def printFibRepresntation(n):
    while (n > 0):
        # Find the greates Fibonacci Number smaller
        # than or equal to n
        f = nearestSmallerEqFib(n);

        # Print the found fibonacci number
        print(f, end=" ")

        # Reduce n
        n = n - f #9,8,1


# Driver code test above functions
n = 30
print("Non-neighbouring Fibonacci Representation of", n, "is")
printFibRepresntation(n)
