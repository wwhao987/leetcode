import numpy as np
lst = [3,10,2,1,20]

def get_lis_length(arr):
    """
    动态规划发获取最长递增子序列长度
    :param arr: 
    :return: 
    """
    # lis[i]表示以arr[i]结尾的lis长度
    lis = np.ones(len(arr))
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                lis[i] = max(lis[j] + 1, lis[i])
    return int(lis.max())

arr = [2, 1, 5, 3, 6, 4, 8, 9, 7]
print(get_lis_length(lst))