def fibnacc(n):
    dp =[]
    if n<=2:
        return n
    dp[0],dp[1],dp[2]=0,1,2
    
    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]
        
    return dp[n]


        
print(fibnacc(4))
