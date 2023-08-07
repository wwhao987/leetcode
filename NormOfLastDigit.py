#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/26 22:55
# @Author  : 朱紫宇
# @File    : NormOfLastDigit.py
# @Software: PyCharm
# Python3 program to demonstrate divisibility
# of Fibonacci numbers.
MAX = 10;

# indexes variable stores index of number
# that is divisible by 2, 3, 5 and 8
arr = [0] * (MAX);
index1 = [0] * (MAX);
index2 = [0] * (MAX);
index3 = [0] * (MAX);
index4 = [0] * (MAX);

# storing fibonacci numbers
arr[0] = 0;
arr[1] = 1;
for i in range(2, MAX):
	arr[i] = arr[i - 1] + arr[i - 2];

# c1 keeps track of number of index
# of number divisible by 2 and others
# c2, c3 and c4 for 3, 5 and 8
c1, c2, c3, c4 = 0, 0, 0, 0

# separating fibonacci number into
# their respective array
for i in range(MAX):
	if (arr[i] % 2 == 0):
		index1[c1] = i;
		c1 += 1;
	if (arr[i] % 3 == 0):
		index2[c2] = i;
		c2 += 1;
	if (arr[i] % 5 == 0):
		index3[c3] = i;
		c3 += 1;
	if (arr[i] % 8 == 0):
		index4[c4] = i;
		c4 += 1;

# printing index arrays
print("Index of Fibonacci numbers",
		"divisible by 2 are :");
for i in range(c1):
	print(index1[i], end = " ");
print("");

print("Index of Fibonacci number",
		"divisible by 3 are :");
for i in range(c2):
	print(index2[i], end = " ");
print("");

print("Index of Fibonacci number",
		"divisible by 5 are :");
for i in range(c3):
	print(index3[i], end = " ");
print("");

print("Index of Fibonacci number",
		"divisible by 8 are :");
for i in range(c4):
	print(index4[i], end = " ");
print("");

# This code is contributed by mits

# Python3 program to demonstrate that sequence of last
# digits of Fibonacci numbers repeats after 60.


if __name__ == '__main__':
    max = 10
    arr = [0 for i in range(max)]
    arr[0] = 0
    arr[1] = 1

    # storing Fibonacci numbers
    for i in range(2, max):
        arr[i] = arr[i - 1] + arr[i - 2]

    # Traversing through store numbers
    for i in range(1, max - 1):

        # Since first two number are 0 and 1
        # so, if any two consecutive number encounter 0 and 1
        # at their unit place, then it clearly means that
        # number is repeating/ since we just have to find
        # the sum of previous two number
        if ((arr[i] % 10 == 0) and (arr[i + 1] % 10 == 1)):
            break

    print("Sequence is repeating after index", i)

# This code is contributed by
# Sanjit_Prasad
### TODO