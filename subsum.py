#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/7/15 03:17
@Author  : 朱紫宇
@File    : subsum.py
@Software: PyCharm
"""
def maxSubArray(nums):
    """
    maxsubArray sum :
    Args:
        nums:
    f(i)=max{f(i−1)+nums[i],nums[i]}
    Returns:

    """
    current_value=0
    max_sum = nums[0]
    for i in range(len(nums)):
        current_value = max(current_value+nums[i],nums[i])
        max_sum = max(max_sum,current_value)
    return  max_sum

if __name__ == '__main__':

    # print(maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4]))
    # print(maxSubArray(nums = [1]))
    print(maxSubArray(nums = [5,4,-1,7,8]))