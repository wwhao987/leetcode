#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/7/12 22:26
@Author  : 朱紫宇
@File    : twoNumAddEqualTarget.py
@Software: PyCharm
"""

def twosum(nums,target):
    for i in range(len(nums)):
        for j in range(i):
            if nums[i]+nums[j]==target:
                return [j,i]

def twoSum(nums, target):
    cnt = {}
    for idx, value in enumerate(nums):
            cnt[value] = idx
    for k,v in enumerate(nums):
        j = cnt.get(target-v)
        if j is not None and k != j:
            return [k,j]

if __name__ == '__main__':

    # nums = [2,7,11,15]
    # target = 9
    # nums = [3, 2, 4]
    # target = 6
    nums = [3, 3]
    target = 6

    # print(twoSum(nums,target))
    print(twosum(nums, target))