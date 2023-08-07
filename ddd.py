#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/6/26 23:22
@Author  : 朱紫宇
@File    : ddd.py
@Software: PyCharm
"""


# Python implementation
# to demonstrate working
# of Cassini’s Identity

# Returns (-1)^n

"""
https://blog.csdn.net/hzf0701/article/details/117359478?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522168779252916800222893203%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=168779252916800222893203&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-1-117359478-null-null.142^v88^control,239^v2^insert_chatgpt&utm_term=%E4%BD%8D%E8%BF%90%E7%AE%97&spm=1018.2226.3001.4187
n>>1 表示数被除2不取余

比如1的二进制是1
2得二进制是10
3的二进制是11

10右移一位变成了1。十进制来看就是2除2变成了1。

11右移一位也变成了1。十进制来看就是3除2被去掉余数变成了1。

在来类比十进制的数。
十进制的100右移一位变成10，是被除10。

所以二进制右移一位就是被除二

同理:
八进制右移一位就是除8
十六进制右移一位就是除16
"""
def cassini(n):
    """
    n&1==1:判断最后以为是否是1，如果是表示右移一位是1，
    n>>1
    删除操作：n>>=1
    :param n:
    :return:
    """

    return -1 if (n >> 1) else 1

# Driver program

n = 5
print(cassini(n))

# This code is contributed
# by Anant Agarwal.
