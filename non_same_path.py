def uniquePaths( m: int, n: int) -> int:
    import numpy as np
    print([1]*n)
    print([1]+[0]*(n-1))
    dp = [[1]*n] + [[1]+[0] * (n-1) for _ in range(m-1)]
    print(dp)
    # for i in range(m)
    # dp = np.zeros((m,n))
    # dp[0][0]=1
    for i in range(1,m):
        for j in range(1,n):
            dp[i][j]=dp[i-1][j]+dp[i][j-1]
    return dp[-1][-1]
    
    
if __name__=="__main__":

    a = uniquePaths(3,7)
    print(a)