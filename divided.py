#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/7/15 04:01
@Author  : 朱紫宇
@File    : divided.py
@Software: PyCharm
"""
def divide( dividend: int, divisor: int):
    if divisor != 0 and (dividend>=-2**31 and dividend<= 2**31-1) and ( divisor>=-2**31 and divisor<=2**31-1):
        return int(dividend / divisor)
    if int(dividend / divisor) > 2 ** 31 - 1:
        return 2 ** 31 - 1
    if int(dividend / divisor) < -2 ** 31: return -2 ** 31

