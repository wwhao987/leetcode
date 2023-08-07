
# str1 = 'ABCDGH'
# str2 = 'AEDFHR'
# str1 = 'ABC'
# str2 = 'AC'
str2 = 'GEBEOCFUFTSXDIXTIGSIEEHKCHZ'
str1 = 'DFLILRJQFNXZ'
# str1 = [1, 1, 4, 3]
# str2 = [1, 1, 3, 4]
def lms(s1,s2):
    """_summary_

    Args:
        s1 (_type_): _description_
        s2 (_type_): _description_
    """
    if len(s1)==0 and len(s2)==0:
        return 0
    n,m = len(s1),len(s2)
    cnt = 0
    for  i in range(n):
        for j in range(m):
            if s1[i]==s2[j]:
                cnt+=1
    return cnt

print(lms(str1,str2))