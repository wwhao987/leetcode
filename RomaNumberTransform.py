#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/7/12 23:01
@Author  : 朱紫宇
@File    : RomaNumberTransform.py
@Software: PyCharm
"""


def romanToInt(s: str):
    roma = {"I": 1, "V": 5, "X": 10, "L": 50,
           "C": 100, "D": 500, "M": 1000,
           }
    ans = 0
    n = len(s)
    # sp={
    #     "IV": 4,
    #     "IX": 9, "XL": 40, "XC": 90,
    #     "CD": 400, "CM": 900
    # }
    for i in range(n - 1):
        if roma[s[i + 1]] > roma[s[i]]:
            ans = ans - roma[s[i]]
        else:
            ans = ans + roma[s[i]]
    ans = ans + roma[s[n - 1]]
    return ans

class Solution:

    SYMBOL_VALUES = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    def romanToInt(self, s: str) -> int:
        ans = 0
        n = len(s)
        for i, ch in enumerate(s):
            value = Solution.SYMBOL_VALUES[ch]
            if i < n - 1 and value < Solution.SYMBOL_VALUES[s[i + 1]]:
                ans -= value
            else:
                ans += value
        return ans


def a(s):
    roma = {"I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000,
            }
    ans = 0
    n = len(s)
    for i in range(n):
        if i<n-1 and roma[s[i]]<roma[s[i+1]]:
            ans-=roma[s[i]]
        else:
            ans+=roma[s[i]]
    return  ans






if __name__ == '__main__':
    # s = "III"
    # print(romanToInt(s))
    s = "MCMXCIV"
    # slu=Solution()
    # print(slu.romanToInt(s))
    print(a(s))